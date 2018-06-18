
#Question-1

a = int(input("Enter year to check it is leap year or not"))
if((a%4) == 0):
    {
        print("Yes it is leap year")
    }
else:
    {
        print("no it is not a leap year")

    }


#Question-2

a = int(input("Enter Length of box"))
b = int(input("Enter Width of box"))
if(a == b):
    print("Box is  square")
else:
    print("Box is Rectagle")



#Question-3
a = int(input("Enter age of First Person"))
b = int(input("Enter age of Seconed Person"))
c = int(input("Enter age of third Person"))
if (a>b):
    if(a>c):
      print("a is greater than b and c")
elif(b>a):
    if(b>c):
        print("B is greater than a and c")
    else:
         print("c is greater")



#Question4
a = int(input("Enter number"))
if(a<=200) :

    if(a>=180 and a<=200):
        print("Congratulations! You won a [Chocolates]")
    elif(a>=121 and a<=151):
        print("Congratulations! You won a [Book]")
    elif(a>=51 and a<=150):
        print("Congratulations! You won a [Wooden Dog]")
    else:
        print("Sorry! No Prize this Time")
else:
    print("Enter value leass than 200")



#Question5

Quantity = int(input("Enter Quantity of the Product"))
TotalCost = Quantity*100
print(TotalCost)
if (TotalCost>1000):
    TotalCost = TotalCost - (18/100)
    print("Total Cost for User after Discount of 10% =",TotalCost)
else:
    print("Toatl Cost for User = ",TotalCost)