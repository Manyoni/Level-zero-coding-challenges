def area_of_triangle(x,y,z):
    s = (1/2)*(x+y+z)
    Area = (s*(s-x)*(s-y)*(s-z))**(1/2)
    return Area

a =8
b =10
c =9

print ("The area of a triangle is ",area_of_triangle(a,b,c))

