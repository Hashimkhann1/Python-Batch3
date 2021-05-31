name = []
age = []
phone_number = []
address = []
con = ""
while con=='y':
    name.append(input("enter name"))
    age.append(input("enter age"))
    phone_number.append(input("enter phone number"))
    address.append(input("enter addres"))
    print("enter y for contiue or n for close")
    con = input("")
students_data=[]
for a in range(len(name)):
    students_data.append({"name":name[a],"age":age[a],"phone_number":phone_number[a],"address":address[a]})
print(students_data)