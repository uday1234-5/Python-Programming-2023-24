def display(x):
    x='''
            
    {0} | {1} | {2}
    -----------
    {3} | {4} | {5}
    ___________
    {6} | {7} | {8}

    '''.format(*move)
    print(x)

move = [' ',' ',' ',' ',' ',' ',' ',' ',' ']*9

for i in range(5):
    turn = "X"
    input1 = int(input(f"To display {turn} , Enter the position :"))
    move[input1] = turn
    display(move)
    if move[input1] != " ":
        print("USED LOCATION")
    
    turn = "O"
    input2 = int(input(f"To display {turn} , Enter the position :"))
    move[input2] = turn
    display(move)
    if move[input1] != " ":
        print("USED LOCATION")