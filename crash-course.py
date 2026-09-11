import math

# comment

# here
# is
# a
# comment

print("hello, world!")

# VARIABLE DECLARATIONS AND DATA TYPES

a = 4 # integer
b = 5.5 # float
c = "CSAEA" # string
d = False # boolean

print(a,b,c,d)

# OPERATORS
# + - / * % ** //
# += -= /=

e = 3 ** 3
print(e)
e += 7
print(e)

# f-strings

print(f"e is equal to {e}")

e -= 6.5
e += 5.1

print(f"wait nevermind e is equal to {e}")

#C COMPARISONS (booleans, which always return true or false)
# < > <= >= == !=

print(4 < 5)
print(7 == 4)
print(1 != 4)

isEqual = "yes" == "yes"
print(isEqual)

# LOGICAL OPERATORS
# In order of precedence not    and    or
f = False
t = True

print(not f) #true
print(f and t) #false
print(t or t) #true
print(f or t and not f) #true

# CASTING ()

g = int(5.5474833746)
print(g)

# STRINGS

s1 = "Goodnight"
s2 = " and "
s3 = "Goodbye"
end = s1 + s2 + s3 # concatenation with +
end += ", Cowboy." # add to the variable

print(end + "\n")

# MATH LIBRARY using 
#max, min, square root

print(math.sqrt(14))
print(math.ceil(3.65))
print(math.floor(8.94))
print(math.pow(2,4))

# CONDITIONALS

# if elif else

t = True
f = False

if 1 > 1 and 1 == 1:
    print("you reached the first condition")
elif 6 == 7 or 3 != 3:
    print("Reached 2nd condition")
elif 9 != 9:
    print("third condition")
else:
    print("reached else")

# LIST
# A list can hold any data type, and can grow and shrink

#index  0   1   2  3   4 ~
nums = [34, 52, 3, 64, 31]

print(nums)
print(nums[2])
print(nums[1])
print(nums[4])
print(nums[-2])

print(nums[0] + nums[2])

nums[0] = 128
print(nums)

# LIST METHODS
# specail build-in methods

words = []

words.append("JOE BLOWS")
words.append("JOB FROM LOES")
words.append("BIG ASS NOSE")
words.append("TERRIBLE WORD")
print(words)

words.remove("TERRIBLE WORD")
words.insert(3,"GARDEN HOSE")
length = len(words)
print(words)
print(length)

import time

for i in range(100):
    print(words)
    time.sleep(0.001)

