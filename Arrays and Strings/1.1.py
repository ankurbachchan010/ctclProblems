
def unique(s1):
    counter = 0
    for i in range(len(s1)):
        for j in range(i+1,len(s1)):
            if s1[i] == s1[j]:
                counter+=1
            else:
                continue
    if counter == 0:
        return "Unique"
    else:
        return "Not Unique"

s1 = "phone"

result  = unique(s1)
print (result)