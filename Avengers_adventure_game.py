import time
import random


def print_pause(message):
    print(message)
    time.sleep(2.4)


def intro(thing, villain):
    print_pause("You find yourself inside a game and\n"
                "you're standing in Amazon rainforest, surrounded "
                "by Giant Water Lily and Monkey Brush Vines.\n")
    print_pause("According to our source " + villain + " is somewhere around "
                "here, in search of infinty stones.\n")
    print_pause("In front of you is a spaceship.\n")
    print_pause("To your left is a magical portal.\n")
    print_pause("In your hand you hold your Mjolnir (but not very "
                "effective).\n")


def portal(thing, villain):
    if "Stormbreaker" in thing:
        print_pause("\nYou peer cautiously into the magical portal.")
        print_pause("\nYou've been here before, and gotten all"
                    " the good stuff. It's just an empty cave"
                    " now.")
        print_pause("\nYou walk back to the Amazon rainforest.\n")
    else:
        print_pause("\nYou peer cautiously into the magical portal.")
        print_pause("\nIt turns out to be only a very small cave.")
        print_pause("\nYour eye catches a glint of metal behind a "
                    "rock.")
        print_pause("\nYou have found the Stormbreaker")
        print_pause("\nNow you are carrying both weapons.")
        print_pause("\nYou walk back out to the Amazon rainforest.\n")
        thing.append("Stormbreaker")
    forest(thing, villain)


def spaceship(thing, villain):
    print_pause("\nYou approach the door of the spaceship.")
    print_pause("\nYou are about to enter when the door "
                "opens and out steps " + villain + ".")
    print_pause("\nOMG! This is " + villain + "'s spaceship!")
    print_pause("\nEvil " + villain + " attacks you!\n")
    if "Stormbreaker" not in thing:
        print_pause("You feel a bit scared, "
                    "what with only having a Mjolnir.\n")
    while True:
        choice2 = input("Would you like to (1) fight or (2) "
                        "run away?")
        if choice2 == "1":
            if "Stormbreaker" in thing:
                print_pause("\nAs the " + villain + " moves to attack, "
                            "you started thundering with Stormbreaker.")
                print_pause("\nThe Stormbreaker shines brightly in "
                            "your hand as you brace yourself for the "
                            "attack.")
                print_pause("\nBut " + villain + " takes one look at "
                            "your shiny new weapon and runs away!")
                print_pause("\nYou have rid the Earth from " + villain +
                            ". You are victorious!\n")
            else:
                print_pause("\nYou did your best...")
                print_pause("but your Mjolnir is no match for the "
                            + villain + ".")
                print_pause("\nYou have been defeated!\n")
            play_again()
            break
        if choice2 == "2":
            print_pause("\nYou run back into the Amazon rainforest. "
                        "\nFortunately, you don't seem to have been "
                        "followed.\n")
            forest(thing, villain)
            break


def forest(thing, villain):
    print_pause("Enter 1 to enter through the door of the spaceship.")
    print_pause("Enter 2 to go through the magical portal .")
    print_pause("What would you like to do?")
    while True:
        choice1 = input("(Please enter 1 or 2.)\n")
        if choice1 == "1":
            spaceship(thing, villain)
            break
        elif choice1 == "2":
            portal(thing, villain)
            break


def play_again():
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y":
        print_pause("\n\n\nWait! Restarting the game ...\n\n\n")
        play_game()
    elif again == "n":
        print_pause("\n\n\nThanks for playing! See you next time.\n\n\n")
    else:
        play_again()


def play_game():
    thing = []
    villain = random.choice(["Thanos", "EGO", "Hela", "Loki"])
    intro(thing, villain)
    forest(thing, villain)


play_game()
