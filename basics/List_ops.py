#filter,map,sort

#sort:which name have to sort give all list
list_of_dicts = [
    {"name":"Ram Hari Kafle", "address":"kavre","age":35},
    {"name":"preja Budhathoki", "address":"Lalitpur","age":21},
    {"name":"Garima Koirala", "address":"kathmandu","age":21},
    {"name":"Sita Tamang", "address":"Baglung","age":25},
]
# list_of_dicts.sort(key=lambda x : x["address"],reverse=False)

sorted_list = sorted(list_of_dicts,key=lambda x : x["address"],reverse=False)
print(list_of_dicts)

#filter:use to compare 

# def func(x,y):
#     print(x,y)
# func=lambda x: print(x)# annomous function
# func("My name is preja.I am from Nepal")

filtered_item=filter(lambda x:x["age"]>30,list_of_dicts)
print(list(filtered_item))

# map: print only specified only name,address ,age
mapped_item=map(lambda x : dict(age=x["age"]),list_of_dicts)
mapped_items=map(lambda x : dict(address=x["address"]),list_of_dicts)

print(list(mapped_item))
print(list(mapped_items))