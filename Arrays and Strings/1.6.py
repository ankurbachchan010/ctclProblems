def str_cmp(string):
  str_dict = {}
  for char in string:
    if char in str_dict:
      str_dict[char] += 1
    else:
      str_dict[char] = 1
  print(str_dict)
  new_str = ''
  for char in str_dict:
    new_str += char
    new_str += str(str_dict[char])
  print(len(string))
  print(len(new_str))
  if len(string)<=len(new_str):
    return string
  else:
    return new_str

print(str_cmp('aabbc'))