

#Questioin1

a = input("Enter First name")
b = input("Enter Middle name")
c = input("Enter Last name")
List = []
List.append(a)
List.append(b)
List.append(c)
print(List)



#Question2

d = "google"
e = "apple"
f = "facebook"
g = "microsoft"
h = "tesla"

List.append(d)
List.append(e)
List.append(f)
List.append(g)
List.append(h)
print(List)

#Question 3

Data = ["Mohali" , "Delhi" , "Mohali" , "Mohali"]
print(Data.count("Mohali"))

#Question 4

Number = [1,9,10,3,8,2,5]
Number.sort()
print(Number)

#Question 5

a = [1,5,7,8]
b = [2,3,6]
c = a + b
c.sort()
print(c)


Question 6

#Stack
stack = ["rahul" , "sanjeev" , "akbar"]
stack.append("simran")
stack.append("sanjeev")
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)

#Queue
from collections import deque
queue = deque(["Rahul" , "sanjeev" , "akbar"])
print(queue)
queue.append("simran")
print(queue)
queue.append("vani")
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)