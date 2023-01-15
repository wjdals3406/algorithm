reports = {x : 0 for x in [0,1,2]}
print(reports)

result = 0 #read는 되는데 write는 안됨
def func():
    print(result)
    
func()

result = 0
def func():
    result += 1
    
func()
