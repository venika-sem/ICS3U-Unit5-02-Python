# Copyright (c) 2022 Venika Sem All rights reserved.
#
# Created by: Venika Sem
# Created on: Nov 2022
# This program finds area of triangle


def calculate_area(base: int, height: int) -> None:
    # calculate area

    # process
    area = (base * height) / 2

    # output
    print("The area is {0} cm²".format(area))


def main():
    # this function gets base and height

    # input
    base_from_user = int(input("Enter the base of a triangle (cm): "))
    height_from_user = int(input("Enter the height of a triangle (cm): "))
    print("")

    try:
        base = float(base_from_user)
        height = float(height_from_user)
        calculate_area(base_from_user, height_from_user)
    except ValueError:
        print("Invalid input, please try again.")

    print("\n\nDone.")


if __name__ == "__main__":
    main()
