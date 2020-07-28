"""
name=[]
i=0
j = int(input(" enter the size of list"))
while i<j :
    k = input("enter the name")

    name.append(k)
    i+=1

print(name)
"""
name= ["aman","preet","aman","deep","aman","deep","deep","deep","aman","preet","sai", "krishna", "rahul","sai", "rahul", "sai","sri"]

#name = ["sai", "krishna", "rahul", "sai", "rahul", "sai","sri"]
z = len(name)
print(z)

a=0
b=0
c=0
check=[]

while a < z:
    count = 0
    b=0
    if name[a] not in check:
        while b < z:
            if name[a] == name[b] :
                count = count +1
                b=b+1
            else:
                b =b+1
    else:
        pass

    if name[a] not in check:
        check.append(name[a])
        #print("the count is ",count)
        print(f"{name[a]} is {count} times")
    a = a+1


print("task is done")