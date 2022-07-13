num = input()
strlist = list(num)
strlist.sort()

sum = 0
idx = 0
for x in strlist:
    if x >= '0' and x <= '9':
        sum += int(x)
    else:
        idx = strlist.index(x)
        break
        
newnum = "".join(strlist[idx:])
print(newnum + str(sum))
#isdigit ½áº¸±â