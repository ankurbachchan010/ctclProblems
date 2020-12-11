def permutation(s1,s2):
    if len(s1)!= len(s2):
        return False
    else:
        check = [0] * 26
        s3 = s1.upper()
        s4 = s2.upper()
        for i in range(len(s1)):
            check[ord(s3[i]) - 65] += 1
            check[ord(s4[i]) - 65] -= 1
        if all(i == 0 for i in check):
            return True
        else:
            return False

s1 = "samirchutiya"
s2 = "chutiyasamira"
print(permutation(s1,s2))