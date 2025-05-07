
print("***********************************SVIT COLLAGE OF TENCHNOLOGY********************************************")
Clas=str(input("enter the class of student"))
Department=str(input("enter the department of student"))
Studname=str(input("enter the Student name"))

print(" 1open \n 2obc \n 3SC/NT")

cast=int(input("enter the cast"))
if(cast==1):

    paid=int(input("enter the fee you have to paid now"))
    if(paid<=50000):
        fee=50000
        print("total fee",fee)
        rem=50000-paid
        print("rem fee is",rem)
        print("******************************you have successfully paid fees***********************************")
    else:
        print("your fees  amount is not  too much")
elif(cast==2):

    paid = int(input("enter the fee you have to paid now"))
    if (paid <= 30000):
        fee = 30000
        print("total fee",fee)
        rem = 30000 - paid
        print("rem fee is", rem)
        print("*******************************you have successfully paid fees***********************************")
    else:
        print(" your fees amount is not too much")

elif(cast==3):

    paid = int(input("enter the fee you have to paid now"))
    if (paid <= 10000):
        fee = 10000
        print("total fee",fee)
        rem = 10000 - paid
        print("rem fee is", rem)
        print("*******************************you have successfully paid fees************************************")
    else:
        print(" your fees amount is not too much")
else:
    print("this is not mention")


