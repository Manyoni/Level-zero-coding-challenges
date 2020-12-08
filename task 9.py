t =0
for i in range(0,1000):
    if (i%3==0 or i%5==0):
        t = t+i
        
print ("Sum of multiples of 3 and 5 =",t)