def prettier(func):

    

    def print_well(value):
        print("*"*5,value,"*"*5)

    def print_ugly(value):
        print(">"*5,value,"<"*5)

    

    def wrapper(*args,**kwargs):
        if kwargs.get("address")=="Lalitpur":
            print_well("I am being prettified")
            splitted=args[0].split(" ")

            for index, i in enumerate(splitted):
                print(f"Name {index}:{i}")

            func(*args,**kwargs)
            print("I am prettified well!")

        else:
            print_ugly(f"Address not Acceptable!.You are a foreigner,{kwargs}")
            return None        
        
    return wrapper
@prettier
def print_name(name,**kwargs):
    print(name)

print_name("Mohanmand Sekh Altaf Raze" ,address="Lalitpur")