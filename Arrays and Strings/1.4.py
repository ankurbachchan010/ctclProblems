def check(str):
    char_dict = {}
    for char in str:
        char_dict[char] = 0
    flag = True
    for char in str:
        if char in char_dict:
            char_dict[char] += 1
    for value in char_dict:
        if char_dict[value] % 2 == 1:
            if flag:
                flag = False
            else:
                return False
    return True
test = 'Not a Palindrome'
string = test.replace(" ", "")
print(check(string))
