#!/usr/bin/env python3

# Created by : Mariam Hemdan
# Created on : October 2019
# This program uses while loop


def main():
    # this program uses While loop
    sum = 0
    loop_counter = 0

    # input
    positive_integer = int(input("Enter an integer: "))
    print("")

    # process & output
    while loop_counter <= positive_integer:
        sum = sum + loop_counter
        print(sum)
        loop_counter = loop_counter + 1


if __name__ == "__main__":
    main()
