"""
Arithmetic Operators ( + ,-,*, / , % ,** )
Relational / Comparison Operators ( == , != , > , < , >= , <= )
Assignment Operators ( = , +=,-= ,*= , /= , %= ,**= )
Logical Operators ( not , and , or )
"""
#Arithmetic Operators ( + ,-,*, / , % ,** )
a = 5
b = 7

sum = a + b 
sub = b - a 
mul = a * b
div = a / b
module = a  % b  # find out reminder
power = a  ** b  
print("Sum of a and b is " , sum) 
print("Dif of a and b is " , sub) 
print("mul of a and b is " , mul) 
print("div of a and b is " , div) 
print("module of a and b is " , module) 
print("power of a and b is " , power) 


#relational / Comparison Operators ( == , != , > , < , >= , <= ) return boolean value True or false
print("relational Operators")

print(a == b) # False
print(a != b) # True
print(a  > b) # Dalse
print(a  >= b) # False
print(a  <= b) # True
print(a  < b) # True

# Assignment Operators ( = , +=,-= ,*= , /= , %= ,**= )
print("Assignment Operators")
c = 50 
print("Value of c is ",c)

#+=
num =10
print ("value of num is ", num)
num1 = num+10
print ("value of num1 is ", num1)
num += 10
print ("value of num is ", num)


# -=

num =10
print ("value of num is ", num)
num1 = num+10
print ("value of num1 is ", num1)
num += 10
print ("value of num is ", num)

# *= 
num =5
print ("value of num is ", num)
num1 = num*5
print ("value of num1 is ", num1)
num *= 5
print ("value of num is ", num)

#  %=
num =5
print ("value of num is ", num)
num1 = num%5
print ("value of num1 is ", num1)
num  %=5
print ("value of num is ", num)

#  %=
num =5
print ("value of num is ", num)
num1 = num**5
print ("value of num1 is ", num1)
num  **=5
print ("value of num is ", num)


# Logical Operators ( not , and , or )  all are Boolean value return  True or False

# not
print("Logical Operators")
print("Not Operators")
print(not(False)) # return True
print(not(True)) # return True
d = 10
e = 20
print(not False)
print(not (d > e))

print("And Operators")
value1 = True
value2  = True
print ("and operator", value1 and value2)

value1 = True
value2  = False
print ("and operator", value1 and value2)


print("OR Operators")
value1 = True
value2  = False
print ("Or operator", value1 or value2)

value1 = True
value2  = True
print ("Or operator", value1 or value2)

f = 5
g =6


print (" check gi grateo then f", (g==f) or (g > f) or (g<f)) 