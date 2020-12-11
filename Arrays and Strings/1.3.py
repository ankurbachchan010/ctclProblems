def urlify(s, l):
    str = ''
    string = ''
    print(string.join(s))
    for i in range(l):
        if s[i] == ' ':
            str += '%20'
            # str.append('%20')
        else:
            # str.append(s[i])
            str += s[i]

    print(string.join(str))
    return str

str = "Mr John Smith"
len = 13
result = urlify(str, len)
print(result)
