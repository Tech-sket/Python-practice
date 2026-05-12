#Reverse a string using loop
text=input("Enter the string")
reverse=""
for i in text:
    reverse=i+reverse
    print(reverse)
    