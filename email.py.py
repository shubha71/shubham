'''write a py program to accept email id and count th occurance of @ symbol'''
str=input("Enter the string: ")
count=0
for i in range(len(str)):
    #ch=str[i].lower()
    if(str[i]=='@'):
        count=count+1
print(count)
