# -*- coding: utf-8 -*-
n = input()
sum = int(n[0])

for i in range(len(n)-1):
    if sum == 0 or int(n[i+1]) == 0: #00123, 0123 
        sum += int(n[i+1])
    else:
        sum = sum * int(n[i+1])
print(sum)
    
    
    

        
                
        
        