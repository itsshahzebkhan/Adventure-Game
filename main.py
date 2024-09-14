# step 1 - install PyCharm community edition or VS Code to start this project
# step 2 - start coding


name = input("Type your name: ")
print("Welcome", name, "to this adventure game!")

answer = input("You are on a dirt road and it has come to an end, you can either go left or right from here. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can either walk around it or swim across. Type walk to walk around the river or swim to swim across the river: ")

    if answer == "swim":
        print("You swam across the river and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for a couple of miles, collapsed due to no water and lost the game.")
    else:
        print('Not a valid option. You lose.')


elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

    if answer == "cross":
        answer = input("You decide to cross the bridge and see a stranger standing at a distance. do you wish to talk to him (yes/no)? ")

        if answer == "yes":
            print("You have decided to talk to that stranger and he told you the way out of this place. You won!")
        elif answer == "no":
            print("You have decided not to talk to that stranger and now you are stuck here for eternity. You lose. ")
        else:
            print('Not a valid option. You lose.')


    elif answer == "back":
        print("You chose to go back so now you lose.")
    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option. you lose. ')

print("Thank you for trying", name)

# note - this was just a demo game with very few options, but you can add more "if, elif and else" statements and add your own interesting scenarios in this game