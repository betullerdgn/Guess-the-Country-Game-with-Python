from random import choice

while True:
    print("/*/" * 40)
    print("/*/" * 15 + "GUESS THE COUTRY" + "/*/" * 15)
    print("/*/" * 40)

    countries = choice(
        ["France", "America", "China", "Spain", "Italy", "Turkey", "Germany", "Mexico", "Ukraine", "Canada", "Korea", "Japan", "Australia", "Brazil", "Sweden", "Norway", "India", "Germany", "Spain", "Russia", "UK", "Ireland"])

    countries = countries.upper()
    number_of_letters = len(countries)

    print("\nKelimemiz {} harflidir.".format(number_of_letters))
    guesses = []
    error = []

    guess_count = 7




    while guess_count > 0:
        chart = ""
        for letter in countries:
            if letter in guesses:
                chart = chart + letter
            else:
                chart = chart + "_"
        if chart == countries:
            print(" You guessed the country correctly")
            break



        print("Guessed the Country", chart)
        print( "You have",guess_count, "guesses left!")

        guess_input = input("Enter a letter\n>>>>")
        guess_input = guess_input.upper()

        if guess_input == countries:
            print("You guessed it correctly")
            break

        if guess_input in guesses or guess_input in error:
            print("{} has been said before. Please enter another letter".format(guess_input))

        elif guess_input in countries:
            rpt = countries.count(guess_input)
            print("Correct!, letter {0} occurs {1} time in your word ".format(guess_input, rpt))
            guesses.append(guess_input)
        else:
            print("Wrong!, This letter does not exist in the word!")
            error.append(guess_input)
            guess_count -=1

    if guess_count == 0:
        print("No more guesses left")
        print("Your Country {} ".format(countries))

    print("If you want to exit the game \n  Press the ',' key .\Press any other key to continue")
    continue_to_play = input(">>>>")
    continue_to_play = continue_to_play.upper()
    if continue_to_play == ",":
        break
    else:
        continue


