# def abc_function(a,b,c):#variable is not declare so to know them then i take time so python is slow.
#     ...

# def abc_function(a,c,b=None):#if we dont need b then we use none and those we need then we put first and then use none variable 
#     ...

# def abc_function(a,b,c=None):
#     ...

# def abc_function(a=None,c=None,b=None):
#     print(f"{a}")
#     print(b)
#     print(c)

# def abc_function(a=None,b=None,c=None,*args,**kwargs):#it accept all the argument 
#     # breakpoint()
#     ...

# abc_function(1,2,3)#defualt argument
# abc_function(1,b=2,c=3)
# abc_function(1,2,3,4,5,6,7,i=1,j=2,k=1)
from decimal import Decimal

list_of_strings = []
list_of_ints = []
list_of_floats = []

def acceptor(*args, **kwargs):

    def seggregator(i):
        if isinstance(i, int):
            list_of_ints.append(i)
        elif isinstance(i, float):
            list_of_floats.append(i)
        elif isinstance(i, str):
            list_of_strings.append(i)
        else:
            print(f"Class object not recognized for {i} with type {type(i)}!")

    # These loops should be outside the seggregator function
    for i in args:
        seggregator(i)

    for key, value in kwargs.items():
        seggregator(value)

acceptor("Sita", 123, "Devi", 111.25, Decimal(235), aakriti="AK", sneha="Sn", poojana="badarne", math=35, science=2151.24)

# print("Integers:", list_of_ints)
# print("Floats:", list_of_floats)
# print("Strings:", list_of_strings)

print(list_of_ints,list_of_floats,list_of_strings)

    


   
