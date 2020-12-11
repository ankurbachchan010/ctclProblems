def oneAway(string1, string2):
    dict_char = {}
    for char in string1:
        if char in dict_char:
            dict_char[char] += 1
        else:
            dict_char[char] = 1
    for char in string2:
        if char in dict_char:
            dict_char[char] += 1
        else:
            dict_char[char] = 1
    print(dict_char)
    if len(dict_char) == max(len(string1),len(string2)) or len(dict_char) == max(len(string1),len(string2))+1:
        return True
    else:
        return False

string1 = "pele"
string2 = "beka"
print(oneAway(string1, string2))