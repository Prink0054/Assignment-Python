"""
#Question1

radius = float(input("Enter no."))
def area(rad):
    area = 3.14 * rad * rad
    return area
ar = area(radius)
print(ar)


#Question2

n = 6
def perfect(n):
    sum = 0
    for i in range(1,n):
         if(n%i == 0):
            sum = sum + i
    if(sum == n):
        return True
    else:
        return False
print(perfect(n))
for i in range(1,1001):
        if (perfect(i)) == True:
            print(i)


#Question3
def mul_table(n, i=1):
    print (n*i)
    if i != 10:
        mul_table(n,i+1)
mul_table(13)



#Question4
def power(a,b):
    if b==1:
        return a
    else:
        return a* power(a,b-1)
a = int(input("Enter a:"))
b = int(input("Enter b:"))
print("Result:", power(a,b))




#Question5
Dic = {
}

def factorial():
    f = 1
    for i in range(1,11):
        f = f * i
        Dic[i] = f
    print("Factorial of 10 =" ,f)

factorial()
print(Dic)

"""