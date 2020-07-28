name = []
"""
x = int(input("enter the number of names to be added "))
for i in range(x):
    y = input(f"enter{i} name ")
    if y not in name:
        name.append(y)
    else:
        print("please enter a different name")

print(name)
"""
x = int(input("enter the number of names to be added "))
for i in range(x):
    y = input(f"enter{i} name ")
    if  y != name:
        name.append(y)
    elif y==name:
        print("please enter difernt name")

print(name)