#!/usr/bin/env python3

# Created by: Joseph Palermo
# Created on: September 2019
# This program calculates the circumference of a circle using tau and radius


import constants


def main():
    # this function calculates the circumference of a circle using tau and
    #   radius

    # input & variables
    radius = int(input("Enter radius of circle (mm): "))

    # process
    circumference = constants.TAU*radius

    # output
    print("")
    print("Circumference is {}mm"
          .format(circumference))


if __name__ == "__main__":
    main()
