# is this a comment..?

# numbers perform operations direcrtly
# varibals declare itself

a = 5 + 6

print(a)
print("\n")


# int() fnction can change numerical strings into numbers

b = "25"

c = int(b) / 5

print(c)
print("\n")

# nubers done -------------------------------


# sting-----------------------------------------
a = "05"

print("hi &a $a")
print('if you can escape \'this\' then why you need 2 quotation\n')


# sting manuplation---------------------------------

a = "string 1 " + "string 2 "
print(a + "one more")
print("\n")

a = 567

b = 100 + a
c = "100" + str(a)

# can't print with stings without turning into strings
print("this is non sting output " + str(b) + " and thats not " + c + "\n")

# concatnation - adding 2 strings

a = "a large string"

b = a.split(" ")


# b = ['a', 'large', 'string']
#  array (list)
print(b)

# in short b = "a large string".split(" ")[1]

# 1 th array (list) element
print(b[1])
print("\n")

# boolean---------------------------------

#  = assign
#  == compare

a = 5 == 5

print(a)
a = 5 != 5
print(a)

# compare types also

a = 5 == "5"

print(a)

# list ===================================== sasta array
# array hi he

a = [1, 45, "squid", ["jay", "shree", "ram"]]
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[3][1])

# size will increase as you add numbers

'''
# taking input with input("string") function
nameinput = input("what's your name ?\n")
print("your name is " + nameinput)

yourage = int(input("your age is : "))
# typecasting

# condional operatos

if yourage > 18:
    print("you are an adult..!!\n")
    print("you birth year is :" + str(2021 - yourage))
else:
    print("kid..! ")
    print("your birth year is " + str(2021 - yourage))
'''
vakya = "Skill level: Beginner Level"

print(vakya.upper())
print(vakya.lower())
print(vakya.find("nn"))
# case sensitive
print(vakya.replace('Beginner', 'Learning'))
#print(vakya.replace(old , new , count))


# a**b is a^b
# a%b is same as C/cpp

# or for logical or
# and for logical ir

if len("nameinput") < 3:
    print("you are lazy")
else:
    print('just why..?')

a = 0
i = 0


def loopnumber():
    try:
        temp = input("how many times you want to run loop")
        return int(temp)
    except ValueError:
        print("please input a number")
        loopnumber()
    except TypeError:
        print("enter a number greater than 0")


numbers = loopnumber()

# while i < 2:
#     if i == 0:
#         i = + 1
#         for r in range(numbers):
#             a = +1
#             x = 1
#             while x < a:
#                 print("#")
#                 x += 1
#         print("%\n")
#     else:
#         for r in range(numbers):
#             a = -1
#             x = a
#             while x < 0:
#                 print("#")
#                 x -= 1
#             print("%\n")
