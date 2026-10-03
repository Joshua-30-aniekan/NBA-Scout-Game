print('''
-|
               -' |
             -'   | __().
        ==wkm=====|'\\/   `.O__
                            \\ `,
                           _-^.
                           `.  `---,
                             :



       ____________________________________
       ///\\\\///\\\\////\\\\///\\\\///\\\\///\\\

''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("You're at a cross road.Whhere do you want to go ?\n Type 'left' or 'right' ").lower()
if direction == "right":
    print("Bad Luck!! Game Over")
elif direction == "left" or direction ==  "left " or direction == " left ":
    decision = input("You're Stephen curry at the game 7 of the 2028 NBA Finals\n You're being  double teamed by two 7 footers.What do you do ,'shoot' or 'pass' or 'time out' ?").lower()
    if decision == "pass":
        print("Stephen Curry does'nt need to pass, Game Over")
    elif decision == "time out":
        print("Zero Ball Knowledge!!Game Over")
    elif decision == "shoot":
        best_ballplayer =input("Who is the best basketball player in the ball family?").lower()
        if best_ballplayer == "lamelo":
            print("You have found the treasure,Here is the ring")
        else:
            print("You can't be serious!!! Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")
