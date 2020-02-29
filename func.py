def get_result_from_img_src(img_el):
  print(img_el.get_attribute("src"))
  img_file_name = img_el.get_attribute("src").split('/')[-1]
  return_value = int(img_file_name.split('-')[0])
  if return_value == 20:
    return_value = '2 ROLLS'
  else:
    if return_value == 40:
      return_value = '4 ROLLS'
    else:
      if return_value == 50:
        return_value = 'CHANCE'
  
  return return_value

def get_validate_date_string(date_time_string):
  print(date_time_string)
  str_array = date_time_string.split(' ')
  str_array[1] = filter(str.isdigit, str(str_array[1]))
  str_array.pop()
  return ' '.join(str_array)

def check_visibility(class_name):
  print(class_name)
  return class_name.find('show') > -1
