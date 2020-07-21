x = int(input("enter the no of candies"))
i=1
st = 10
if x <= st :
  while i <= x:
    if i > st:
         break

    print('candy')
    i = i+1
elif x> st:
    print(f"stock {st} available")
    ans= input("do you want to proceed further(yes/no)")
    if ans == 'yes':
        while i<=st:
            if i>st:
                break
            print("candy")
            i= i+1
    else:
        print("thankyou visit again")

print("bye")


