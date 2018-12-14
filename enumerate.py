example = ['left', 'right', 'up', 'down']

for i in range(len(example)):
    print(i, example[i])

# the above is not the right way to do it
# use enumerator! 
for i, j in enumerate(example):
    print(i, j)


# key = index value of enumerate, value : value in the list
new_dict = dict(enumerate(example))

print(new_dict)
