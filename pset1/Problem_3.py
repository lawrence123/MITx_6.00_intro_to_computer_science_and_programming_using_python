# Problem 3
# 15.0/15.0 points (graded)
# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

# Longest substring in alphabetical order is: abc
# Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.

s_len = len(s) -1
val = 0
char_temp = ''
char_out = ''
char_high = 'a'
for i in s:
    if not char_temp:
        char_temp = i
    if ord(i) > ord(char_high):
        char_high = i    
    if s_len != val:
        val += 1
        if ord(i) <= ord(s[val]):
            char_temp = char_temp + s[val]
            if len(char_temp) > len(char_out):
                char_out = char_temp
        elif ord(i) > ord(s[val]):
            if len(char_temp) > len(char_out):
                char_out = char_temp
            char_temp = ''
if ord(i) < ord(char_high) and len(char_temp) == len(char_out) and len(char_temp) == 1:
    char_out = char_high
elif len(char_out) < len(char_temp) and len(char_temp) != 1 :
    char_out = char_temp
print("Longest substring in alphabetical order is: " + char_out)