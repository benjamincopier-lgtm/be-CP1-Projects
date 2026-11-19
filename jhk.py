def hello(name, *args):
    print(args)
    for first in args:
        print(f"hello {first} {name}")
hello("g","j","k","l","o","i",)
hello("kreg","o")


def clean(**kwargs):
    if kwargs["type"] =="str":
        return kwargs["data"].strip().lower()
    elif kwargs["type"]=="int":
        return int(kwargs["data"])
    elif kwargs["type"] == "float":
        return round(float(kwargs["data"]),2)
    elif kwargs["type"] == "list":
        return str(f"{x}, " for x in kwargs["data"])
    elif type=="bool":
        return f"{kwargs["data"]}"
    

print(clean( type="float", data ="3.141596214"))
print(clean( data="utah", type="str"))