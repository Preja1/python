# Reverse a string
s = "hello"
reversed_s = s[-1::-1]
print("Reversed String:", reversed_s)

# Count vowels in a string
name="Preja Budhathoki"
vowels="aeiouAEIOU"
vowel_count = 0
for char in name:
    if char in vowels:
        vowel_count +=1   

print("Vowel Count:", vowel_count)

# Check if a string is a palindrome
t = "madam"
palindrome = t == t[::-1]
print("Palindrome:", palindrome)

# Convert string to uppercase
print("String to uppercase:",name.upper())

# Replace spaces with hyphens in a string
string="Replace spaces with hyphens"
string_replace=string.replace(" ","-")
print(string_replace)

# Extract digits from a string
text_with_digits = "abc123xyz9"
digits = "".join(filter(str.isdigit, text_with_digits))
print("Extracted Digits:",digits)

# Remove vowels from a string
remove_vowels="".join(char for char in name
    if char not in vowels)
print("Remove vowels from a string",remove_vowels)

# Sum of all integers in a list
num=[1,2,3,4,5]
sum_num=0
for i in num:
    sum_num+=i
print("Sum of list:",sum_num)

# Find the maximum value in a list
print("Maximum value in a list:",max(num))

# Find the minimum value in a list
print("Minimum value in a list:",min(num))

# Multiply all numbers in a list
multi_num=1
for i in num:
    multi_num *=i
print("Multiply all number ina a list:",multi_num)

# Remove duplicates from a list
num_1=[1,2,2,3,3,3,3,4,4,4,5,5,5,]
no_duplicates=list(set(num_1))
print("Remove duplicates:",no_duplicates)

# Sort a list of integers
num_2=[4,3,5,7,8,6,2,1]
num_sort=sorted(num_2)
print("Sort a list of integers:",num_sort)

# Find even numbers in a list
even_num=[]
for i in num_2:
    if i%2==0 :
        even_num.append(i)
print("Even number:",even_num)

# Find odd numbers in a list
old_num=[]
for i in num_2:
    if i%2!=0 :
        old_num.append(i)
print("Odd number:",old_num)

# Convert list of strings to integers
num_3=["1","2","3","4","5"]
int_list=list(map(int,num_3))
print("Convert string list into integers:",int_list)

# Count how many times each element appears in a list
fruit=["apple","banana","mango","apple","graph","mango"]
count_num={}
for i in fruit:
    if i in count_num:
        count_num[i]+=1
    else:
        count_num[i]=1
print("Count element appers in a list:",count_num)


# Merge two lists into one
merge_list=num_3+fruit
print("Merge two list:",merge_list)

# Find the common elements between two lists
common=list(set(num)&set(num_2))
print("Common elements between two lists:",common)



# Flatten a list of lists
nested_list = [[1, 2], [3, 4], [5, 6]]
flattened = []

for sublist in nested_list:
    for i in sublist:
        flattened.append(i)

print("Flattened List:", flattened)

# Check if an element exists in a list
exists = 3 in num
print("3 exists in list:", exists)


# Remove all negative numbers from a list
list_with_negatives = [0 ,1, -2, 3, -4, 5]
list_with_positives=[]
for i in list_with_negatives:
    if i>=0:
        list_with_positives.append(i)

print("Remove all negative numbers:",list_with_positives)

# Find the longest word in a list of strings
longest=""
for word in fruit:
    if len(word)>len(longest):
        longest=word
print("Longest word in the list:",longest)


# Join a list of strings into one string
joined = ' '.join(fruit)
print("Joined String:", joined)


# Split a sentence into a list of words
sentence="I am learning python language"
split_sentence = sentence.split()
print("Split Sentence:", split_sentence)

# Ask for 5 student names, append to list and display
nums = []
students=[]
for i in range(5):
    name = input("Enter the name of student: ")
    students.append(name)
    # students.extend(name)
print("List of 5 students:",students)

    



