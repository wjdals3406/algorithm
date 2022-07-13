num = input()
divide = len(num)//2

sum1 = 0
sum2 = 0
for i in range(divide):
    sum1 += int(num[i])
    sum2 += int(num[i+divide])
if(sum1 == sum2):
    print("LUCKY")
else :
    print("READY")
    
#코드 줄이기