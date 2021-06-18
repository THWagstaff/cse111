import math

desiredvolume = float(input("What is your desired volume: "))
width = float(input("Enter the width of the tire in mm (ex 205): "))
aspectRatio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = (math.pi * width * width * aspectRatio * (width * aspectRatio + 2540 * diameter)) / 10000000

from datetime import datetime
Current_Day_Time = datetime.now()

if desiredvolume < volume:
    print(f"The approximate volume is {volume:.1f} milliliters, you are over your desired volume of {desiredvolume:.1f}")
else:
        print(f"The approximate volume is {volume:.1f} milliliters, you are under your desired volume of {desiredvolume:.1f}")

with open("volumes.txt", "at") as volumes_file:
    print(Current_Day_Time, file=volumes_file)
    print(f"{width}, {aspectRatio}, {diameter}, {volume}", file=volumes_file)