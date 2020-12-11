def isRotate(s1, s2):
  if len(s1) == len(s2) and len(s1)>0:
    s1s1 = s1 + s1
    return isSubstring(s1s1, s2)
  return False


def isSubstring(s1, s2):
  if s2 in s1:
    return True
  else:
    return False

print(isRotate('waterbottle', 'erbottlewat'))