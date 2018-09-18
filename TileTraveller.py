#Player starts at 1,1 and can only go north
#We tell the player what direction he can go in
#If he enters a direction which is not available we print not a valid direction and let him try again
#Players wins if he gets to the tile 3,1, and we print out Victory!
#Valid moves for each tile:
    #1,1 -> N
    #1,2 -> N, E, S
    #1,3 -> E, S
    #2,1 -> N
    #2,2 -> S, W
    #2,3 -> W, E
    #3,1 -> Victory!
    #3,2 -> S, N
    #3,3 -> S, W

#1,1 = 11 
#3,1 = 31 og victory!
   
n = "(N)orth"
s = "(S)outh"
w = "(W)est"
e = "(E)ast"


position = 11
while position != 31:
    if position == 11 or position == 21:
        print("You can travel: ", n)
        direction = input("Direction: ")
        if direction == "n" or direction == "N":
            position += 1
        else:
            print("Not a valid direction!")
    elif position == 12:
        print("You can travel: " + n + " or " + e + " or " + s + ".")
        direction = input("Direction: ")
        if direction == "n" or direction == "N":
            position += 1
        elif direction == "e" or direction == "S":
            position += 10
        elif direction == "s" or direction == "S":
            position -= 1
    elif position == 13:
        print("You can travel: " + e + " or " + s + ".")
        direction = input("Direction: ")
        if direction == "e" or direction == "E":
            position += 10
        elif direction == "s" or direction == "S":
            position -= 1
    