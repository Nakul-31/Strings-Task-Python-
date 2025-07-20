#question 1:
print("\nQus-1")

input_str = input("Enter a string: ")

if len(input_str) < 2:
    print("not a valid string")
else:
    result = input_str[:2] + input_str[-2:]
    print("Result:", result)

print("\n-------------------")
print("\n-------------------")




#question 2:
print("\nQus-2")

str1 = input("enter first string: ")
str2 = input("enter second string: ")


if len(str1) > 0 and len(str2) > 0:
   
    new_str1 = str2[0] + str1[1:]
    new_str2 = str1[0] + str2[1:]
    

    result = new_str1 + " " + new_str2
    print("result:", result)
else:
    print("both strings must have atleast one character")


print("\n-------------------")
print("\n-------------------")




#question 3:
print("\nQus-3")

s = input("enter a string: ")

if len(s) < 3:
    result = s
elif s.endswith("ing"):
    result = s + "ly"
else:
    result = s + "ing"

print("result:", result)

