n=int(input("Enter the number: "))
for s in range (n):
    for m in range (s, n-1):
        print(" ",end=" ")
    for m in range (s):
        print("*",end=" ")
    for m in range (s+1):
        print("*",end=" ")
    print()
              
          