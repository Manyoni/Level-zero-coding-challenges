def printing_common_vowels(str1,str2):
    a = list(set(str1)&set(str2))
    vowels=0
    for i in a:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
            print ("the common letters in this string are :",i)

first_input_string=input("Enter first string:")
second_input_string=input("Enter second string:")   

b = printing_common_vowels(first_input_string,second_input_string)
print (b)
