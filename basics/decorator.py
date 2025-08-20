#decorators

def prettier(func):

    def wrapper(*args,**kwargs):
        if kwargs.get("address")=="Lalitpur":
            func(*args,**kwargs)
            print("I am prettified well!")

           
        else:
            print("Address not Acceptable!.You are a foreigner",kwargs)
            return None
    return wrapper
@prettier
def print_name(name,**kwargs):
    print(name)

print_name("Preja Budhathoki." ,address="Lalitpur")
print_name("Garima koirala." ,address="Kathmandu")
