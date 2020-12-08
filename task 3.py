def compare_two_numbers(x,y):
    if x==65 or y == 65 or (x+y) == 65:
        print ("True")
    else:
        print("False")

a = int(input("Please enter the first number input a whole number"))
b = int(input("Please enter the second number input a whole number"))

compare_two_numbers(a,b)