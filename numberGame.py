


def MyNumber():
    count = 0
    for i in range(0,100):
        count += 1
        print(count)
        if(i % 3 == 0):
            print("fizz")
        elif(i % 5 == 0):
            print("buzz")
        elif(i % 3 == 0 and i % 5 == 0):
            print("fizzbuzz")
    
        
MyNumber()
   
