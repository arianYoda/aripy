from datetime import date, timedelta
import random
from persiantools.jdatetime import JalaliDate


# =========================================================
# Calculator
# =========================================================

def calculator():
    print("Opening Calculator...")

    while True:
        print("""
=========================================
              Calculator
=========================================

Choose an option:

1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulo
6. Floor Division
7. Power
8. Back
""")

        operation = input("Choose an option: ")

        if operation == "8":
            return

        if operation not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("Invalid Choice!")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        if operation == "1":
            result = num1 + num2
        elif operation == "2":
            result = num1 - num2
        elif operation == "3":
            result = num1 * num2
        elif operation == "4":
            if num2 == 0:
                print("Cannot divide by zero.")
                continue
            result = num1 / num2
        elif operation == "5":
            if num2 == 0:
                print("Cannot use modulo with zero.")
                continue
            result = num1 % num2
        elif operation == "6":
            if num2 == 0:
                print("Cannot use floor division with zero.")
                continue
            result = num1 // num2
        else:
            result = num1 ** num2

        print(f"Result: {result}")


# =========================================================
# BMI Calculator
# =========================================================

def BMI_Calculator():
    print("Opening BMI Calculator...")

    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if weight <= 0 or height <= 0:
        print("Weight and height must be greater than zero.")
        return

    bmi = weight / (height ** 2)

    print(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25:
        print("Normal weight")
    elif bmi < 30:
        print("Overweight")
    else:
        print("Obesity")


# =========================================================
# Unit Converter
# =========================================================

def Unit_Converter():
    print("Opening Unit Converter...")

    while True:
        print("""
=========================================
             Unit Converter
=========================================

1. Length
2. Weight
3. Area
4. Back
""")

        choice = input("Choose an option: ")

        if choice == "1":
            print("""
Length Converter:
1. Meters to Kilometers
2. Kilometers to Meters
3. Meters to Centimeters
4. Centimeters to Meters
5. Back
""")

            option = input("Choose an option: ")

            if option == "5":
                continue

            try:
                value = float(input("Enter value: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if option == "1":
                print(f"{value} m = {value / 1000} km")
            elif option == "2":
                print(f"{value} km = {value * 1000} m")
            elif option == "3":
                print(f"{value} m = {value * 100} cm")
            elif option == "4":
                print(f"{value} cm = {value / 100} m")
            else:
                print("Invalid Choice!")

        elif choice == "2":
            print("""
Weight Converter:
1. Kilograms to Grams
2. Grams to Kilograms
3. Kilograms to Pounds
4. Pounds to Kilograms
5. Back
""")

            option = input("Choose an option: ")

            if option == "5":
                continue

            try:
                value = float(input("Enter value: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if option == "1":
                print(f"{value} kg = {value * 1000} g")
            elif option == "2":
                print(f"{value} g = {value / 1000} kg")
            elif option == "3":
                print(f"{value} kg = {value * 2.20462} lb")
            elif option == "4":
                print(f"{value} lb = {value / 2.20462} kg")
            else:
                print("Invalid Choice!")

        elif choice == "3":
            print("""
Area Converter:
1. Square meters to Square kilometers
2. Square kilometers to Square meters
3. Square meters to Square centimeters
4. Square centimeters to Square meters
5. Back
""")

            option = input("Choose an option: ")

            if option == "5":
                continue

            try:
                value = float(input("Enter value: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if option == "1":
                print(f"{value} m² = {value / 1_000_000} km²")
            elif option == "2":
                print(f"{value} km² = {value * 1_000_000} m²")
            elif option == "3":
                print(f"{value} m² = {value * 10_000} cm²")
            elif option == "4":
                print(f"{value} cm² = {value / 10_000} m²")
            else:
                print("Invalid Choice!")

        elif choice == "4":
            return

        else:
            print("Invalid Choice!")


# =========================================================
# Temperature Converter
# =========================================================

def Temperature_Converter():
    print("Opening Temperature Converter...")

    while True:
        print("""
=========================================
         Temperature Converter
=========================================

1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Celsius to Kelvin
4. Kelvin to Celsius
5. Back
""")

        choice = input("Choose an option: ")

        if choice == "5":
            return

        try:
            temperature = float(input("Enter temperature: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == "1":
            result = (temperature * 9 / 5) + 32
            print(f"{temperature} °C = {result:.2f} °F")

        elif choice == "2":
            result = (temperature - 32) * 5 / 9
            print(f"{temperature} °F = {result:.2f} °C")

        elif choice == "3":
            result = temperature + 273.15
            print(f"{temperature} °C = {result:.2f} K")

        elif choice == "4":
            result = temperature - 273.15
            print(f"{temperature} K = {result:.2f} °C")

        else:
            print("Invalid Choice!")


# =========================================================
# Age Calculator
# =========================================================

def Age_Calculator():
    print("Opening Age Calculator...")

    print("""
=========================================
           Age Calculator
=========================================

1. Gregorian Birthday
2. Persian Birthday
3. Back
""")

    age_choice = input("Choose an option: ")

    if age_choice == "3":
        return

    # -----------------------------------------------------
    # Gregorian Birthday
    # -----------------------------------------------------

    if age_choice == "1":

        try:
            year = int(input("Enter your birth year: "))
            month = int(input("Enter your birth month: "))
            day = int(input("Enter your birth day: "))

            birth_date = date(year, month, day)
        except ValueError:
            print("Invalid Gregorian date.")
            return

        today = date.today()

        if birth_date > today:
            print("Birthday cannot be in the future.")
            return

        years = today.year - birth_date.year
        months = today.month - birth_date.month
        days = today.day - birth_date.day

        if days < 0:
            months -= 1
            first_day_of_current_month = date(today.year, today.month, 1)
            last_day_previous_month = first_day_of_current_month - timedelta(days=1)
            days += last_day_previous_month.day

        if months < 0:
            years -= 1
            months += 12

        persian_birth_date = JalaliDate(birth_date)
        persian_today = JalaliDate.today()

        print()
        print(f"Gregorian Birthday: {birth_date}")
        print(f"Persian Birthday:   {persian_birth_date}")
        print(f"Today (Gregorian):  {today}")
        print(f"Today (Persian):    {persian_today}")
        print(f"You are {years} years, {months} months, and {days} days old.")

        # Next Gregorian birthday
        try:
            next_birthday = date(today.year, birth_date.month, birth_date.day)
        except ValueError:
            # February 29 birthdays
            next_birthday = date(today.year, 2, 28)

        if next_birthday < today:
            try:
                next_birthday = date(
                    today.year + 1,
                    birth_date.month,
                    birth_date.day
                )
            except ValueError:
                next_birthday = date(today.year + 1, 2, 28)

        difference = next_birthday - today
        next_months = difference.days // 30
        next_days = difference.days % 30

        print(
            f"Your next birthday is in approximately "
            f"{next_months} months and {next_days} days. 🎂"
        )

    # -----------------------------------------------------
    # Persian Birthday
    # -----------------------------------------------------

    elif age_choice == "2":

        try:
            year = int(input("Enter your Persian birth year: "))
            month = int(input("Enter your Persian birth month: "))
            day = int(input("Enter your Persian birth day: "))

            birth_date = JalaliDate(year, month, day)
            today = JalaliDate.today()
        except ValueError:
            print("Invalid Persian date.")
            return

        if birth_date > today:
            print("Birthday cannot be in the future.")
            return

        years = today.year - birth_date.year
        months = today.month - birth_date.month
        days = today.day - birth_date.day

        if days < 0:
            months -= 1

            previous_month = today.month - 1
            previous_year = today.year

            if previous_month == 0:
                previous_month = 12
                previous_year -= 1

            if previous_month <= 6:
                days_in_previous_month = 31
            elif previous_month <= 11:
                days_in_previous_month = 30
            else:
                days_in_previous_month = (
                    30 if JalaliDate.is_leap(previous_year) else 29
                )

            days += days_in_previous_month

        if months < 0:
            years -= 1
            months += 12

        gregorian_birth_date = birth_date.to_gregorian()
        gregorian_today = today.to_gregorian()

        print()
        print(f"Persian Birthday:   {birth_date}")
        print(f"Gregorian Birthday: {gregorian_birth_date}")
        print(f"Today (Persian):    {today}")
        print(f"Today (Gregorian):  {gregorian_today}")
        print(f"You are {years} years, {months} months, and {days} days old.")

        # Next Persian birthday
        next_year = today.year

        if (today.month, today.day) >= (birth_date.month, birth_date.day):
            next_year += 1

        next_persian_birthday = JalaliDate(
            next_year,
            birth_date.month,
            birth_date.day
        )

        next_birthday_gregorian = next_persian_birthday.to_gregorian()
        gregorian_today = today.to_gregorian()

        difference = next_birthday_gregorian - gregorian_today

        next_months = difference.days // 30
        next_days = difference.days % 30

        print(
            f"Your next Persian birthday is in approximately "
            f"{next_months} months and {next_days} days. 🎂"
        )

    else:
        print("Invalid Choice!")


# =========================================================
# Password Generator
# =========================================================

def Password_Generator():
    print("Opening Password Generator...")

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "{}[]().-_=+!@#$%^&*~`"

    print("""
=========================================
          Password Generator
=========================================

1. Letters only
2. Letters + numbers
3. Symbols only
4. Numbers + symbols
5. Numbers only
6. All characters
7. Back
""")

    pass_choice = input("Choose an option: ")

    if pass_choice == "7":
        return

    if pass_choice == "1":
        characters = lower + upper
    elif pass_choice == "2":
        characters = lower + upper + numbers
    elif pass_choice == "3":
        characters = symbols
    elif pass_choice == "4":
        characters = numbers + symbols
    elif pass_choice == "5":
        characters = numbers
    elif pass_choice == "6":
        characters = lower + upper + numbers + symbols
    else:
        print("Invalid Choice!")
        return

    try:
        length = int(input("Enter password length: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if length <= 0:
        print("Password length must be greater than zero.")
        return

    # random.sample prevents repeated characters.
    if length > len(characters):
        print(
            f"Maximum length for this option is "
            f"{len(characters)} because characters cannot repeat."
        )
        return

    password = "".join(random.sample(characters, length))

    print(f"Your password: {password}")


# =========================================================
# Rock Paper Scissors
# =========================================================

def Rock_Paper_Scissors():
    print("Opening Rock Paper Scissors...")

    print("""
=========================================
        Rock Paper Scissors
=========================================

1. Play with Computer
2. Play Two Players
3. Back
""")

    play_choice = input("Choose an option: ")

    moves = ["Rock", "Paper", "Scissors"]

    # -----------------------------------------------------
    # Computer Mode
    # -----------------------------------------------------

    if play_choice == "1":

        print("\nStarting game with Computer...")

        computer_score = 0
        human_score = 0

        while computer_score < 3 and human_score < 3:

            human = input(
                "Human, make your move: "
            ).capitalize()

            if human not in moves:
                print("Invalid move!")
                continue

            computer = random.choice(moves)

            print(f"Computer chose: {computer}")

            if computer == human:
                print("Tie")

            elif (
                (computer == "Rock" and human == "Scissors")
                or (computer == "Paper" and human == "Rock")
                or (computer == "Scissors" and human == "Paper")
            ):
                print("Computer scores!")
                computer_score += 1

            else:
                print("Human scores!")
                human_score += 1

            print(
                f"Score: Computer = {computer_score} | "
                f"Human = {human_score}"
            )

        print("\nFinished")

        if computer_score == 3:
            print("Computer is the winner!")
        else:
            print("Human is the winner!")

    # -----------------------------------------------------
    # Two Player Mode
    # -----------------------------------------------------

    elif play_choice == "2":

        print("\nStarting Two Player game...")

        player1_score = 0
        player2_score = 0

        while player1_score < 3 and player2_score < 3:

            player1 = input(
                "Player 1, please make your move: "
            ).capitalize()

            if player1 not in moves:
                print("Invalid move for Player 1!")
                continue

            player2 = input(
                "Player 2, please make your move: "
            ).capitalize()

            if player2 not in moves:
                print("Invalid move for Player 2!")
                continue

            print(f"\nPlayer 1 chose: {player1}")
            print(f"Player 2 chose: {player2}")

            if player1 == player2:
                print("Tie")

            elif (
                (player1 == "Rock" and player2 == "Scissors")
                or (player1 == "Paper" and player2 == "Rock")
                or (player1 == "Scissors" and player2 == "Paper")
            ):
                print("Player 1 scores!")
                player1_score += 1

            else:
                print("Player 2 scores!")
                player2_score += 1

            print(
                f"Score: Player 1 = {player1_score} | "
                f"Player 2 = {player2_score}"
            )

        print("\nFinished")

        if player1_score == 3:
            print("Player 1 is the winner!")
        else:
            print("Player 2 is the winner!")

    elif play_choice == "3":
        return

    else:
        print("Invalid Choice!")


# =========================================================
# Main Menu
# =========================================================

def main():
    while True:

        print("""
=========================================
             PYTHON MULTI-TOOL
=========================================

1. Calculator
2. BMI Calculator
3. Unit Converter
4. Temperature Converter
5. Age Calculator
6. Password Generator
7. Rock Paper Scissors
8. Exit

=========================================
""")

        choice = input("Please Input Your Option: ")

        if choice == "1":
            calculator()

        elif choice == "2":
            BMI_Calculator()

        elif choice == "3":
            Unit_Converter()

        elif choice == "4":
            Temperature_Converter()

        elif choice == "5":
            Age_Calculator()

        elif choice == "6":
            Password_Generator()

        elif choice == "7":
            Rock_Paper_Scissors()

        elif choice == "8":
            Exit()

        else:
            print("Invalid Choice!")


def Exit():
    print("Exit...")
    raise SystemExit


if __name__ == "__main__":
    main()
