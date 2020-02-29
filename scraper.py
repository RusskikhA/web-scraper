import csv
import time

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from func import get_result_from_img_src
from func import get_validate_date_string
from func import check_visibility

## Input dealer

## Test purpose
# dealer = 'Valerija'
# default_url = 'https://www.livegametracker.com/monopoly/?period=month?dealer&dealer=Valerija'

dealer = raw_input("Enter dealer : ") 
url = 'https://www.livegametracker.com/monopoly/?period=month?dealer&dealer=%s'%(dealer)

## Open browser

browser = webdriver.Chrome('./driver/chromedriver')
browser.maximize_window()
browser.get(url)
## Test purpose
# browser.get(default_url)

pagination_btns = browser.find_elements_by_class_name('paginate_button')
print(len(pagination_btns))
page_number = int(pagination_btns[-2].find_element_by_tag_name('a').get_attribute("innerHTML"))
print(page_number)
next_btn = pagination_btns[-1]

## Remove popup
time.sleep(3)
popup_el = browser.find_element_by_id('popupModal')
if bool(popup_el) & check_visibility(popup_el.get_attribute("class")):
  print('Removing popup modal...')
  close_btn = browser.find_element_by_xpath('//*[@id="popupModal"]/div/div/div[1]/button')
  if (close_btn):
    try:
      WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="popupModal"]/div/div/div[1]/button'))
      )
    except:
      print('Cant close popup')
    finally:
      close_btn.click()

## Write csv

with open('data/result.csv', mode='wb') as result_file:
  result_csv_writer = csv.writer(result_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

  result_csv_writer.writerow(['Dealer', 'Date', 'Time','Result'])

  ## loop through pagination
  for pagination_table in range(page_number):
    next_btn = browser.find_element_by_id('monopoly-spins_next')
    try:
      WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'monopoly-spins'))
      )
    except:
      print('Network error.')
      browser.quit()
    finally:
      ## Get table data
      table = browser.find_element_by_id('monopoly-spins')
      
      ## Get row data in single page

      # try:
      rows = table.find_elements_by_tag_name('tr')
      for row in rows:
        rowData = row.find_elements_by_tag_name('td')
        if (len(rowData)):
          date_time = rowData[1].get_attribute("innerHTML")
          date_object = datetime.strptime(get_validate_date_string(date_time), '%B %d %Y %H:%M')
          date_info = date_object.strftime('%Y%m%d')
          time_info = date_object.strftime('%H:%M')
          el_image = rowData[2].find_elements_by_tag_name('img')
          result_info = '-'
          if (len(el_image)):
            result_info = get_result_from_img_src(el_image[0])

          result_csv_writer.writerow([dealer, date_info, time_info, result_info])

      # except:
      #   print('No rows')
      # finally:
      #   print('************* Pass geting row')

    try:
      WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'monopoly-spins_next'))
      )
    except:
      print('Network error.')
      # browser.quit()
    finally:
      next_btn.click()
      time.sleep(3)