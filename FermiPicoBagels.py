"""
    Create a program asking user to guess three digits location. Giving three number chooses randomly stored in a list.
    Output of 'Fermi' for correct position and number, 'Pico' for correct number exist in both list and 'Bagels' for no correct guess. 
    Filename: FermiPicoBagels.py
    Author: Anh Tran
    Date: Jan 13, 2024
    Collaborators: None
"""
import random


def answer_repeat(user_int: str, user_input_list: list) -> bool:
    """
    Checking if user input pre-exist or repeat digit.
    parameters: (user_input: str, user_input_list: list) #user_input_list is empty list
    return: True or False
    """
    # user_input not in existing list, then append to list.
    if user_int not in user_input_list:
        user_input_list.append(user_int)
        # checking for repeat digits using index
        for i in range(len(user_int) - 1):
            if user_int[i] in user_int[i + 1]:
                return False
        # keep the loop in main function going
        return True
    else:
        return False


def check_answer(user_input: str, li: list) -> bool:
    """
    Function take in two diameters, one is user_input
    and second one is changeless 3 digits random_list.
    parameters: (<str>, <list>)
    return: True or False
    """
    # converting string straight to str in list individually.
    user_list = [str(digit) for digit in user_input]
    x = False
    bagels = False
    fermi_found = False
    non_matching_found = False
    out_come = ""

    for j in range(len(user_list)):
        # comparing each digits to find same position + same value
        if user_list[j] == li[j]:
            out_come += "Fermi! "
            # only print once no repeat following loop
            fermi_found = True
        elif user_list[j] in li:
            out_come += "Pico! "
            non_matching_found = True
    # exist the loop print final answer
    print(out_come)

    if user_list == li:
        x = True
        return x  # x is True passed back to main and stop the program

    if fermi_found:
        return False

    # nothing similar after enter the loop return bagels one time.
    if not (non_matching_found or bagels):
        print("Bagels! ")
        bagels = True
    # There is matching found exit the loop and check position and value.
    return False


def main():
    """
    Main function design to take in user_input
    and passed it to the 'called' function.
    parameters: None
    return: None
    """
    list_num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    # random.sample() function allow random pick, no repeat choice
    three_digit_list = random.sample(list_num, 3)  # (list to pick from, how many)
    user_input_list = []
    guesses = 0
    while True:
        user_input = input("Guess the three digits in its location: ")
        if user_input.isdigit() and len(user_input) == 3:
            # function answer_repeat == True
            if answer_repeat(user_input, user_input_list):
                guesses += 1
                # check_answer == True
                if check_answer(user_input, three_digit_list):
                    guesses += 1
                    print(f"You got the correct answer in {guesses-1} guesses.")
                    break
            else:
                print("Invalid guess. Guesses must be all digits with no repeats.")
        else:
            print("Invalid guess. Guesses must be all digits with no repeats.")


if __name__ == "__main__":
    main()
