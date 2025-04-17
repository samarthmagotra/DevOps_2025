
## A
first = 7
second = 44.3
print(first+second)
print(first * second)
print(second/first)

## B
a = 8
a = 17
a = 9
b = 6
c = a+b
b = c+a
b = 8
print("B",a,b,c)

## C
print("C", "john",'john')

## D
my_number = 5+5
print("result is: "+ str(my_number))

## E
x = 5
y = 2.36
print (x+ int(y) )

## F
#1. Create two variables named X and Y.
X = 2
Y = 7
#2. Print “BIG” if X is bigger than Y.
#3. Print “small” if X is smaller than Y.
if X > Y:
    print("BIG")
else:
    print("small")

## G
#1. Create a variable and initialize it with a number 1-4.
#2. Create 4 conditions (if-elif) which will check the variable.
#3. Print the season name accordingly:
#- 1 = summer
#- 2 = winter
#- 3 = fall
#- 4 = spring

season = 4
if season == 1:
    print('summer')
elif season == 2:
    print('winter')
elif season == 3:
    print('fall')
elif season == 4:
    print('spring')
else:
    print("Unknown input !")

## H
#Fix the following code without changing a or b:
a = 8
b = "123"
print(a+int(b))