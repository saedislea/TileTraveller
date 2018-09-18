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

n = "(N)orth"
s = "(S)outh"
w = "(W)est"
e = "(E)ast"


print("You can travel: ",n)
direction = input("Direction: ")
if direction == "n" or direction == "N":
    #position = 1,2
    print("You can travel :" + n + " or " + e + " or " + s + ".")
    direction = input("Direction: ")
    if direction == "n" or direction == "N":
        #1,3
        print("You can travel: " + e + " or " + s + ".")
        direction = input("Direction: ")
        if direction == "e" or direction == "E":
            #2,3
            print("You can travel :" + w + " or " + e + ".")
            direction = input("Direction: ")
            if direction == "e" or direction == "E":
            #3,3
                print("You can travel :" + s + " or " + "w" + ".")
            direction = input("Direction: ")
            if direction == "s" or direction == "S":
            #3,2
                print("You can travel: " + s + " or " + n + ".")
            direction = input("Direction: ")
            if direction == "s" or direction == "S":
            #3,1
                print("Victory!")
    elif direction == "E" or direction == "e":
        print("You can travel: " + s + " or " + w + ".")
    elif direction == "s" or direction == "S":
        print("You can travel :" + n + ".")
    else:
        print("Not a valid direction")
else:
    print("Not a valid direction")