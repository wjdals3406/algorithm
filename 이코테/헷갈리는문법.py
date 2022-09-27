result = 0 #read는 되지만 write는 안된다
def func():
    print(result)
    
func()

result = 0
def func():
    result += 1
    
func()