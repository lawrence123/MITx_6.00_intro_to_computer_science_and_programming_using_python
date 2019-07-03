# Problem 2
# 10.0/10.0 points (graded)
# Assume s is a string of lower case characters.

# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

# Number of times bob occurs is: 2

count = 0
bobs = 0
str_len = len(s)

for i in s:
    if i == 'b' and str_len != count + 1:
        val2 = count + 1
        if s[val2] == 'o' and str_len != val2 + 1:
            val3 = val2 + 1
            if s[val3] == 'b':
                bobs += 1
    count += 1

print("Number of times bob occurs is: " + str(bobs))