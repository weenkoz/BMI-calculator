#Our libraries
import sys

#Start messages
print("Welcome to the BMI calculator!\n")
print("Disclaimers:\nThe calculator does not distinguish between fat mass and muscle mass, so it may overestimate body fat in athletes.")

#declares the variable
BMI = 0

#calculations
while BMI < 1:
    print("\nChoose your unit of measurement:")
    choice = input("Metric or Imperial? ").lower()

    try:
        if choice == "metric":
            height = float(input("Height - centimeters (ex: 165): "))
            weight = float(input("Weight - kilograms (ex: 55): "))

            height_m = height / 100
            BMI = weight / (height_m ** 2)

        elif choice == "imperial":
            feet = int(input("Height - feet (ex: 5): "))
            inches = int(input("Height - inches (ex: 5): "))
            weight = float(input("Weight - pounds (ex: 121): "))

            total_inches = feet * 12 + inches
            BMI = (weight * 703) / (total_inches ** 2)

        else:
            print("Unit of measurement not supported. Please choose Metric or Imperial.")
            continue
    #if you didn't write a number
    except ValueError:
        print("Invalid input! Please enter only numbers for height and weight.")
        continue

#result
print(f"\nYour BMI is: {BMI:.2f}")

#categories
if BMI < 18.5:
    print("Result: Unfortunately, you are underweight!")
elif BMI < 25:
    print("Result: Very good! You have a normal weight!")
elif BMI < 30:
    print("Result: Unfortunately, you are overweight!")
elif BMI < 35:
    print("Result: Unfortunately, you are obese!")
else:
    print("Result: Unfortunately, you are extremely obese!")

input("\nPress Enter to exit...")
sys.exit()