#Question1

Data = []
for i in range(10):
    a = int(input("Enter Number"))
    Data.append(a)
print(Data)

for i in Data:
    print(i)


#Question3

Data = []
for i in range(5):
    a = int(input("Enter integer"))
    Data.append(a)

Data1 = []
for i in Data:
    i = i * i
    Data1.append(i)
print(Data1)



        str(i).isdigit():
        Int.append(i)
    elif str(i).:
        print(i)


#Question4
List = ["apple" , 1 , "name" , "hello" , 2.2 , 4, "qwerty"]
Int = []
String = []
Float = []
for i in List:
    if isinstance(i,int):
        Int.append(i)


    elif isinstance(i,str):
        String.append(i)


    else:
        Float.append(i)



print("Float list = " + str(Float))
print("Int list = " + str(Int))
print("String List = " + str(String))

#Question5

Odd_numbers = []
Even_numbers = []

for i in range(1,101):
    if i%2==0:
        Even_numbers.append(i)
    else:
        Odd_numbers.append(i)

print(Even_numbers)

#Question-6

for i in range(0,4):
    for i in range(0,i+1):
        print("*", end=" ")
    print()


#Question7

Dic = {"name" : "Prink" , "Age" : "20"
      }
for i in Dic:
    Dic.get(i)
    print(i)


 #Question8
l = []

for i in range(0,5):
     num = int(input("Enter the number"))
     l.append(num)


l2 = []
a = int(input("Enter the value"))
x = l.index(2)
x = l.remove(2)
print(l)
