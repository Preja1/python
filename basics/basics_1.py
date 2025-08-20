#Variables in python

name="Preja Budhathoki"

# schoolName=""
# SchoolName=""
# Schoolname=""
#snake case is used

school_name="Euro school"

print(name)

# Indentation In Python
# if True:
# if True:
# pass


# name = input("Enter Any Name \n")
# school_name = input("Enter Your School name \n")

# print(name)
# print(school_name)


# Loops In Python

# List In Python
# students_name = ["Rita", "Sita", "Gita"]

# for student in students_name: # for loop
# print(student)


# for index, student in enumerate(students_name): # for loop
# print(index,student)


students_name = []

# Task 1
# Ask 5 students name from input and display them afterwards



# students_name.append(name)


# Numbers

# val_1_i=int(1.22)
# val_2_f=float(1.22343)

# val_1 = complex(1,2)
# val_2 = complex(2,3)

# breakpoint()
# print()

# Implicit (Default Behaviour) / Explicit (Overriden Behaviour)


# strings are immutable

# name = "Ram Bahadur"
# address = 'Kapan, Budhanilkantha'

# num = str(123456)
# arr = str([1,2,3])

# methods in string


# Lists in python

nums = []
students=[]
for i in range(5):
    name = input(f"Enter the name of student{i+1} : ")
    students.append(name)
    # students.extend(name)
    

print("List of 5 students:")
for j in students:
    print(j)
