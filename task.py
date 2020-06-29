# 1.) Create three variables in a single line and assign different values to them and make sure their data types are different. Like one is int, another one is float and the last one is a string.

# program

x,y,z=10,10.5,"string"
print (x,y,z)


# 2.) Create a variable of value type complex and swap it with another variable whose value is an intege.

# program

x,y=10,10+7j
print (x,y)
x,y=y,x
print (x,y)

# 3.) Swap two numbers using the third variable as the result name and do the same task without using any third variable.

# program (a)

x,y=10,11
print (x,y)
result = x
x = y
y = result
print (x,y)

# program (b)
x,y=12,13
print(x,y)
x,y=y,x
print(x,y)

# 4.) Write a program to print the value given by the user by using both Python 2.x and Python 3.x Version.

# program 2.x

x = input('user value: ')
print x

# program 3.x

x = input('user value: ')
print (x)

# 5.a) Ask the user to enter any 2 numbers in between 1-10 and add both of them to another variable call z

# program (a)

x = int(input('Please enter a number between 1-10: '))
y = int(input('Please enter another number between 1-10: '))
z = x+y
print(f'Sum of your given number {x} and {y} is: {z}')


# 5.b) Use z for adding 30 into it and print the final result by using variable results

# program (b)
x = int(input('Please enter a number between 1-10: '))
y = int(input('Please enter another number between 1-10: '))
z = x+y+30
result = z
print(result)

# 6.) Write a program to check the data type of the entered values. HINT: Printed output should say -  The input value data type is: int/float/string/etc

x = eval(input('Please enter any value: '))
print(f'the data type of your entered value is {type(x)}')

# 7.) If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ again. Will it change the value. If Yes then Why?

# Ans- Yes it is going to change the value, we can overright any variable value it will replace its data type also 


