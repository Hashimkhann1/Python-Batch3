def search(num,list):
    for a in range(len(list)):
        if num==list[a]:
            print(a)
list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]
number = int(input("enter the number to find the index"))
search(number,list1)
print("your entered number is",number)