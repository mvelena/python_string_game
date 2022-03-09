import time
import random


def select_scene(scenes):
    scene = random.choice(scenes)
    return scene


def select_place(places):
    place = random.choice(places)
    return place


def select_villain(villains):
    villain = random.choice(villains)
    return villain


def select_weapon(villain):
    if villain == "The Dark Knight":
        add_weapon = random.choice(["garlic", "juggling balls"])
    elif villain == "The Crazy Clown":
        add_weapon = random.choice(["sword", "garlic"])
    else:
        add_weapon = random.choice(["sword", "juggling balls"])
    return add_weapon


def villain_weapon(villain):
    if villain == "The Dark Knight":
        main_weapon = "sword"
    elif villain == "The Crazy Clown":
        main_weapon = "juggling balls"
    else:
        main_weapon = "garlic"
    return main_weapon


def print_pause(message):
    print(message)
    time.sleep(2)


def intro(scene, villain, place):
    print_pause(f"You found yourself laying in a {scene} filled "
                "with bones of different animals. ")
    print_pause(f"You are not sure how you got there but you do"
                f" know that there is {villain} close by.")
    print_pause("After examining the area, you notice a house on the right.")
    print_pause(f"On the left, there is a {place}.")


def knight_stay(current_weapon, main_weapon, emoji_won, emoji_lost):
    if "sword" in current_weapon:
        stay(main_weapon)
        print_pause("With a single strike, you knocked this villain out.")
        print_pause("You won!!!")
        print_pause(emoji_won)
    else:
        print_pause(
            "You decided to stay and fight but you do not have a sword.")
        print_pause("With one strike, The Dark Knight knocked you out.")
        print_pause("You lost.")
        print_pause(emoji_lost)
    repeat_game()


def clown_stay(current_weapon, main_weapon, emoji_won, emoji_lost):
    if "juggling balls" in current_weapon:
        stay(main_weapon)
        print_pause("You started to juggle and hypnotize the villain.")
        print_pause("In a minute, The Clown fell down.")
        print_pause("You won!!!")
        print_pause(emoji_won)
    else:
        print_pause("You decided to stay. The Crazy Clown attacked you.")
        print_pause(
            "Oh no! Without juggling balls all your efforts are useless.")
        print_pause("The Clown killed you.")
        print_pause("You lost. ")
        print_pause(emoji_lost)
    repeat_game()


def vampire_stay(current_weapon, main_weapon, emoji_won, emoji_lost):
    if "garlic" in current_weapon:
        stay(main_weapon)
        print_pause("Without any hesitation, you threw garlic at the Vampire.")
        print_pause("It got into the Vampire’s mouth.")
        print_pause("The villain started to suffocate and die.")
        print_pause("You won!!!")
        print_pause(emoji_won)
    else:
        print_pause("You decided to stay and fight.")
        print_pause("But nothing is working against the Vampire.")
        print_pause("After several minutes of fighting, the Vampire "
                    "finally got you and put his teeth into your flesh.")
        print_pause("You lost.")
        print_pause(emoji_lost)
    repeat_game()


def stay(main_weapon):
    print_pause("You decided to stay and fight. ")
    print_pause(
        f"Good for you that you collected the {main_weapon} earlier.")


def run(villain):
    print_pause(f"You ran so fast that {villain} could not get you.")
    print_pause("You are back to the place where you woke up.")


def option_valid():
    print_pause("Are you going to stay or will you run away?")
    option = input("Choose 1 to stay, choose 2 to run away.\n")
    if option == "1":
        return option
    elif option == "2":
        return option
    else:
        return option_valid()


def direction_valid(place):
    print_pause("Where would you like to go?")
    direction = input(f"Enter 1 - for the house. Enter 2 - for the {place}\n")
    if direction == "1":
        return direction
    elif direction == "2":
        return direction
    else:
        return direction_valid(place)


def item_valid(main_weapon, add_weapon):
    print_pause("What will you take with you?")
    item = input(f"Choose 1 for the {main_weapon}, 2 for {add_weapon}.\n")
    if item == "1":
        return item
    elif item == "2":
        return item
    else:
        return item_valid(main_weapon, add_weapon)


def repeat_game():
    print_pause("Would you like to play again?")
    repeat = input("Type 'y' for yes, type 'n' for no:\n")
    if repeat == "y":
        play_game()
    elif repeat == "n":
        print_pause("Thank you.")
    else:
        repeat_game()


def place_weapon(place, main_weapon, add_weapon, current_weapon):
    print_pause(f"You decided to explore the {place}.")
    print_pause("It is very dark inside but you decided to keep moving.")
    print_pause(f"Suddenly, on one side, you saw {main_weapon}. On the "
                f"other side, you saw {add_weapon}.")
    item = item_valid(main_weapon, add_weapon)
    if item == "1":
        current_weapon.append(main_weapon)
        print_pause(f"You took the {main_weapon} and left the {place}.")
    else:
        current_weapon.append(add_weapon)
        print_pause(f"You took the {add_weapon} and left the {place}.")
    print_pause("You are back to the place where you woke up. ")
    return current_weapon


def main(place, villain, current_weapon, main_weapon,
         add_weapon, emoji_won, emoji_lost):
    direction = direction_valid(place)
    if direction == "1":
        print_pause("You chose to go to the house.")
        print_pause(f"You opened the door and found {villain}.")
        option = option_valid()
        if villain == "The Dark Knight" and option == "1":
            knight_stay(current_weapon, main_weapon, emoji_won, emoji_lost)
        elif villain == "The Crazy Clown" and option == "1":
            clown_stay(current_weapon, main_weapon, emoji_won, emoji_lost)
        elif villain == "The Vampire" and option == "1":
            vampire_stay(current_weapon, main_weapon, emoji_won, emoji_lost)
        else:
            run(villain)
            main(place, villain, current_weapon, main_weapon,
                 add_weapon, emoji_won,  emoji_lost)
    elif direction == "2":
        current_weapon = place_weapon(
            place, main_weapon, add_weapon, current_weapon)
        main(place, villain, current_weapon, main_weapon,
             add_weapon, emoji_won, emoji_lost)


def play_game():
    villains = ["The Dark Knight", "The Crazy Clown", "The Vampire"]
    scenes = ["desert", "forest"]
    places = ["dark cave", "deep hole in the ground"]
    current_weapon = []
    scene = select_scene(scenes)
    place = select_place(places)
    villain = select_villain(villains)
    main_weapon = villain_weapon(villain)
    add_weapon = select_weapon(villain)
    emoji_won = "\U0001F600"
    emoji_lost = "\U0001F480"

    intro(scene, villain, place)
    main(place, villain, current_weapon, main_weapon,
         add_weapon, emoji_won, emoji_lost)


play_game()
