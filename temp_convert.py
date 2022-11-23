#!/usr/bin/env python3
# Created By: Minab Berhane
# Date: November 21 2022
# This program converts temperature in celsius to fahrenheit


def calculate_fahrenheit():
    # getting temp from user
    temp_celsius_string = input("enter the temperature(°C): ")
    print("")

    try:
        # convert string to float
        temp_celsius_float = float(temp_celsius_string)
        # convert from celsius to fahrenheit
        temp_fahrenheit = 9 / 5 * temp_celsius_float + 32
        print("{:,.2f}°C is equal to {:,.2f}°F".format(temp_celsius_float, temp_fahrenheit))

    # checking if input is invalid
    except Exception:
        print("{} is not a number".format(temp_celsius_string))


def main():
    calculate_fahrenheit()


if __name__ == "__main__":
    main()
