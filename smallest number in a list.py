#smallest number in a list
number=[3,5,2,8,1]
smallest=number[0]
for i in number:
    if i<smallest:
        smallest=i
        print("smallest number is ",smallest)