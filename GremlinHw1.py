import random


def ask_question(prompt, options):
    while True:
        print(prompt)
        for i, option in enumerate(options):
            print(f"{i + 1}. {option}")
        response = input("Enter the number of your choice: ")
        try:
            response = int(response)
            if response in range(1, len(options) + 1):
                return response
            else:
                print("Invalid choice. Please enter a number between 1 and", len(options))
        except ValueError:
            print("Invalid input. Please enter a number.")


def is_recyclable(material):
    if material in ["paper", "cardboard", "glass", "metal", "plastic"]:
        return True
    else:
        return False


options = ["Paper", "Cardboard", "Glass", "Metal", "Plastic", "Other"]


def main():
    while True:
        # Ask the user what type of material they have
        material = ask_question("What type of material do you have?", options)

        # Convert the user's response to a lowercase string
        material = options[material - 1].lower()

        # Check if the material is recyclable
        if is_recyclable(material):
            print("Yes, this material can be recycled!")
        else:
            print("Sorry, this material cannot be recycled.")

        # Ask the user if they want to continue
        response = ask_question("Do you want to continue?", ["Yes", "No"])
        if response == 2:
            break


if __name__ == "__main__":
    main()
