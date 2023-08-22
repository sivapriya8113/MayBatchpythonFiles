row=int(input("enter the limit"))

for i in range(row):
    for s in range(row-i):
        print("  ",end="  ")
    for j in range(0,1):
        print("* ",end="  ")
    print()

for i in range(row-1):
    for s in range(i+2):
        print("  ",end="  ")
    for j in range(0,1):
        print("* ", end=" ")
    print()

for i in range(row):
    for s in range(2*(row-i)):
        print("  ",end="  ")
    for j in range(0,1):
        print("* ",end="  ")
    print()

# for i in range(row):
#      for s in range(row + i):
#         print("  ", end="  ")
#      for j in range(0, 1):
#         print("* ", end="  ")
#         print()

