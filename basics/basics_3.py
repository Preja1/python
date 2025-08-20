# Dictionary is represented as dict

# Dictionary declaration
# Mutable

user = dict(
first_name = "Sagar",
middle_name = "",
last_name = "Sedai",
username = "sagarsedai"
) # func builtins

address = {
"country": "",
"state":"",
"local_level":"",
"ward":"",
"street":"",
"house_no":"",
'zip':0,
} # value init

user.update(key="key1") # takes keyword arguments

# # Getting value of key in dict

# # Throws exception / error if not key is present
fname = user["first_name"] # we're pretty sure that key exists
print(fname)
print(user["key"] )
# # Just attempt to get some value for any key

uname = user.get("username","No Username")
print(uname)

# # Setting Values in dict key
# # This is safe

address["country"] = "Nepal"
print(address["country"])

address["state"] = "Bagmati"

address.update(
state = "Bagmati",
local_level="Xyz",
ward="12",
street="ABC",
house_no="1232",
zip = 44600,
)
print(user)
print(address)



# #List
# student_1=dict(name="",address="")
# student_2=dict(name="",address="")
# student_3=dict(name="",address="")
# students=list()
# student_1.update(name="Preja",address="Godawari")
# students.append(student_1)

# student_2.update(name="Junu",address="thimi")
# students.append(student_2)

# student_3.update(name="Satishna",address="Bhaktapur")
# students.append(student_3)

# print(students)


# student=[]
# students=list()


# for i in range(5):
#     name=input(f"Enter your name:")
#     address=input(f"Enter your address:")
#     student=dict(name=name,address=address)
#     students.append(student)

# for j in range(5):
#     print(f"Name: {students[j]['name']}, Address: {students[j]['address']}")



