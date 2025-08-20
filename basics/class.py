# class Utility:
#     def __init__(self):
#         self.sneha()
#         self.junU()

#     def sneha(self):
#         print("Hi baderne")
    
#     def junU(self):
#         print("Hi junuwa")

# # static method class method abstract method
# isinstance=Utility()

# class Utility:

#     def add_ab(self,a,b):
#         return a+b
    
#     @staticmethod
#     def add_sab(a,b):
#         return a+b
    
#     @staticmethod
#     def sub_sab(a,b):
#         return a-b
    
# num1=Utility.add_sab(1,2)
# num2=Utility.sub_sab(6,2)#direct only for static method

# print(num1)
# print(num2)

# instance=Utility()#instantiation
# num=instance.add_ab(1,2)
# print(num)

#generator read only once 
def generate_uoton(n):
    count=0

    while count<n:
        yield count #yield return generator value
        count+=1

g5=generate_uoton(5)

g5s=[i for i in g5]

print(g5s)
print([i for i in g5])

    