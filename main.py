__author__ = "Basel Akasha"


def main():

    # Get user's input
    user_input = str(input("Number: "))

    # Reverse the string
    user_input = user_input[::-1]

    # Divide userInput into two arrays
    group1 = []
    group2 = []
    counter = len(user_input) - 1
    while counter >= 0:
        if counter == 0:
            group2.append(int(user_input[counter]))
        elif (counter % 2) == 0:
            group2.append(int(user_input[counter]))
        else:
            group1.append(int(user_input[counter]))
        counter -= 1

    # Multiply each digit of the first array by 2 and append the sum as a string to group1_sum_digits
    group1_sum_digits = ""
    for digit in group1:
        group1_sum_digits += str(digit * 2)

    # Add up each digit group1_sum_digits variable
    group1_sum = 0
    for i in group1_sum_digits:
        group1_sum += int(i)

    # Add up each digit from group2 (the digits that were not multiplied at the beginning).
    group2_sum = 0
    for i in group2:
        group2_sum += int(i)

    # Add up both sums together.
    total_sum = group1_sum + group2_sum

    # Check total
    if total_sum % 10 == 0:
        print("Valid")
    else:
        print("Invalid")




if __name__ == '__main__' : main()
