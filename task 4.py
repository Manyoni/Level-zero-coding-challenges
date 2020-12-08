def test_number_3(x,y):
    if x == 3 or y == 3 and x+y  == 3:
        return True
    else:
        return False

a = int(input("Please enter the first number to test if it returns true or false"))
b = int(input("Please enter the second number to test if it returns true or false"))

y = test_number_3(a,b)
print (y)
