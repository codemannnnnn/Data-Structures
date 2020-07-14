# Runtime Complexity

command = input

# if command in ['n', 's', 'e', 'w']:

commands = ['n', 's', 'e', 'w', 'q', 'p' ]

commands[1] # constant time operation; doesn't depend on the size of the input

# accessing a dictionary value by key

rooms = {"outside": Room(...), ....  }
rooms["outside"] # constant time operation; doesn't depend on the number of elements in the dictionary

# depends on the number of elements in the commands list
for command in commands:
    # do something
    # adding 1 to list size increases number of loop iterations by c for some constant

for key, value in rooms.items(): # linear time operation
for key in rooms:

# print out every combination of pairs of commands from our command list
for x in commands: # 6 commands
    for y in commands: # 6 commands
        print(x, y) # 36 prints
        (n, n), (n, s), ...
        (s, n), (s, s), ...
        (e, n), (e, s), ...
