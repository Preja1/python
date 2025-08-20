# Create a dictionary with 3 key-value pairs of student names and marks.
students=dict(
    Ram=90,
    Shyam=85,
    Hari=75
)
student= {
    "Sita":65,
    "Rita":98,
    "Laxmi":77
}
print(students)
print(student)

# Add a new key-value pair to an existing dictionary.
students.update(Sital=95)
print("New key-value pair:",students)

# Update the value of an existing key in a dictionary.
student["Hari"]=80
print("Update the value of an existing key:",students)

# Delete a key from the dictionary.
del students["Hari"]
print("After delete students:",students)

# Check if a key exists in the dictionary.
if "Ram"is students:
    print(" Ram exists in the student dictionary.")

# Loop through all keys and values in a dictionary.
for key,values in students.items():
    print(f"{key}=>{values}")

# Count the frequency of each character in a given string using a dictionary.
frequency={}
for char in students:
    if char in frequency:
        frequency[char]+=1
    else:
        frequency[char]=1

print("Count frequency of each character of students:")
for char,count in frequency.items():
    print(f"{char}:{count}")

# Merge two dictionaries into one.
students.update(student)
print("Merge two dictionaries:",students)

# Get the key with the highest value in a dictionary.
higehest_key=None
higehest_vlaues=0
for key,values in students.items():
    if values>higehest_vlaues:
        higehest_key=key
        higehest_vlaues=values

print("topper:",higehest_key,"\tmarks:",higehest_vlaues)

# Sort a dictionary by its values.
sorted_students = dict(sorted(students.items()))
print("After sorting:",sorted_students)