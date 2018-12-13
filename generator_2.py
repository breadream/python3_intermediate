input_list =[5,6,2,10,15,7,8,9]

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False


xyz = (i for i in input_list if div_by_five(i))
    

for i in xyz:
    print(i)

    
[print(i) for i in xyz] # list comprehension; one liner, building a list  
(print(i) for i in xyz) # generator object, nothing's gonna happen 


[[print(i,ii) for ii in range(5)] for i in range(5)]

for i in range(5):
    for ii in range(5):
        print(i, ii) 


xyz = (((i, ii) for ii in range(9999999999)) for i in range(9999999999))

# this will run because xyz is a generator object
for i in xyz:
    for ii in i:
        print(ii)


xyz = (print(i) for i in range(5))

for i in xyz:
    i
# instead of print(i) 
