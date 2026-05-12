#largest number in a list
number=[3,5,2,8,1]
largest=number[0]
for i in number:
    if i>largest:
        largest=i
        print("largest number is ",largest)
        