# list comprehension
xyz = [i for i in range(5)]

print(xyz)

xyz = []
for i in range(5):
    xyz.append(i)

print(xyz)


# generator object
xyz = (i for i in range(5)) # parentheses make all difference 
# not gonna store this in memory 


