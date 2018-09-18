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
