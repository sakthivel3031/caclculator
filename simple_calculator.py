import math

print("\t\t\tSIMPLE CALCULATOR............\n")
print("\n")
wh=int(input("Press 1 to start..........."))
while(wh==1):
    print("\t1.ADDITION\n\t2.SUBRACTION\n\t3.MULTIPLICATION\n\t4.DIVISION\n\t5.MODULO\n\t6.SQUARE_ROOT\n\t7.SQUARE\n")
    choice =int(input("enter your choice : "))
    if (choice==1):
        a=int(input("Enter the first number : "))
        b=int(input("Enter the second number : "))
        c=a+b
        print("the answer is : ",c)
    elif(choice==2):
        a=int(input("Enter the first number : "))
        b=int(input("Enter the second number : "))
        c=a-b
        print("the answer is : ",c)
    elif(choice==3):
        a=int(input("Enter the first number : "))
        b=int(input("Enter the second number : "))
        c=a*b
        print("the answer is : ",c)
    elif(choice==4):
        a=int(input("Enter the first number : "))
        b=int(input("Enter the second number : "))
        c=a/b
        print("the answer is : ",c)
    elif(choice==5):
        a=int(input("Enter the first number : "))
        b=int(input("Enter the second number : "))
        c=a%b
        print("the answer is : ",c)
    elif(choice==6):
        s=int(input("enter the number : "))
        sq=math.sqrt(s)
        print("the answer is : ",sq)
    elif(choice==7):
        sr=int(input("enter the number : "))
        srt=sr**2
        print("the asnwer is : ",srt)
    else:
        print("enter the valid choice............")
    wg=int(input("press o to exit and 1 to coninue : "))
    if(wg==1):
        continue
    else:
        break
    

