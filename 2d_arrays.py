#!/usr/bin/env python3

# Created by: Seti Ngabo
# Created on: Oct 2021
# This program print random numbers between 1 and 50 with the average


import random


def random_average(passed_in_2D_list):
    # this function accepts 2d arrays

    row = len(passed_in_2D_list)
    column = len(passed_in_2D_list[0])
    sub_total = row * column
    total = 0
    for row_value in passed_in_2D_list:
        for number in row_value:
            total = total + number

    final_sum = total / sub_total

    return final_sum


def main():
    # this function uses a 2D array

    a_2d_list = []

    # input
    first_input = input("How many rows would you like: ")
    second_input = input("How many columns would you like: ")
    print("")

    try:
        rows = int(first_input)
        columns = int(second_input)
        for counter_rows in range(0, rows):
            temp_column = []
            for counter_columns in range(0, columns):
                a_random_number = random.randint(1, 50)
                temp_column.append(a_random_number)
                print("{0} ".format(a_random_number), end="")
            a_2d_list.append(temp_column)
            print("")

    except Exception:
        print("Invalid input, try again.")
        print("\nDone.")
        exit()

    final_answer = random_average(a_2d_list)
    print("")
    print("The average of all the numbers is: {0} ".format(final_answer))

    print("\nDone.")


if __name__ == "__main__":
    main()
