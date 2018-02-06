x = int(input("Enter a number to find divisors:\n"))
divisorlist = [1]
for a in range(2,((x//2)+1)):
    if int(x/a)==x/a:
        divisorlist.append(a)

divisorlist.append(x)
print("The list of divisors are:\n")
print(divisorlist)
