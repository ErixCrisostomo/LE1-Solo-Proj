def temperature_converter():
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        try:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print("Temperature in Fahrenheit:", fahrenheit)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    elif choice == 2:
        try:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print("Temperature in Celsius:", celsius)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    elif choice == 3:
        try:
            celsius = float(input("Enter temperature in Celsius: "))
            kelvin = celsius + 273.15
            print("Temperature in Kelvin:", kelvin)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    elif choice == 4:
        try:
            kelvin = float(input("Enter temperature in Kelvin: "))
            celsius = kelvin - 273.15
            print("Temperature in Celsius:", celsius)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    else:
        print("Invalid choice")
    temperature_converter()


def distance_converter():
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Meters to Feet")
    print("4. Feet to Meters")
    print("5. Millimeters to Inches")
    print("6. Inches to Millimeters")
    print("7. Centimeters to Inches")
    print("8. Inches to Centimeters")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        try:
            kilometers = float(input("Enter distance in Kilometers: "))
            miles = kilometers * 0.621371
            print("Distance in Miles:", miles)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    elif choice == 2:
        try:
            miles = float(input("Enter distance in Miles: "))
            kilometers = miles / 0.621371
            print("Distance in Kilometers:", kilometers)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    elif choice == 3:
        try:
            meters = float(input("Enter distance in Meters: "))
            feet = meters * 3.28084
            print("Distance in Feet:", feet)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    elif choice == 4:
        try:
            feet = float(input("Enter distance in Feet: "))
            meters = feet / 3.28084
            print("Distance in Meters:", meters)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    elif choice == 5:
        try:
            millimeters = float(input("Enter distance in Millimeters: "))
            inches = millimeters * 0.0393701
            print("Distance in Inches:", inches)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    elif choice == 6:
        try:
            inches = float(input("Enter distance in Inches: "))
            millimeters = inches / 0.0393701
            print("Distance in Millimeters:", millimeters)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    elif choice == 7:
        try:
            centimeters = float(input("Enter distance in Centimeters: "))
            inches = centimeters * 0.393701
            print("Distance in Inches:", inches)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    elif choice == 8:
        try:
            inches = float(input("Enter distance in Inches: "))
            centimeters = inches / 0.393701
            print("Distance in Centimeters:", centimeters)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    else:
        print("Invalid choice")
    distance_converter()


def weight_converter():
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    print("3. Milligrams to Grams")
    print("4. Grams to Milligrams")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        try:
            kilograms = float(input("Enter weight in Kilograms: "))
            pounds = kilograms * 2.20462
            print("Weight in Pounds:", pounds)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    elif choice == 2:
        try:
            pounds = float(input("Enter weight in Pounds: "))
            kilograms = pounds / 2.20462
            print("Weight in Kilograms:", kilograms)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    elif choice == 3:
        try:
            milligrams = float(input("Enter weight in Milligrams: "))
            grams = milligrams / 1000
            print("Weight in Grams:", grams)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    elif choice == 4:
        try:
            grams = float(input("Enter weight in Grams: "))
            milligrams = grams * 1000
            print("Weight in Milligrams:", milligrams)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    else:
        print("Invalid choice")
    weight_converter()


def volume_converter():
    print("1. Milliliters to Liters")
    print("2. Liters to Milliliters")
    print("3. Liters to Gallons")
    print("4. Gallons to Liters")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        try:
            milliliters = float(input("Enter volume in Milliliters: "))
            liters = milliliters / 1000
            print("Volume in Liters:", liters)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    elif choice == 2:
        try:
            liters = float(input("Enter volume in Liters: "))
            milliliters = liters * 1000
            print("Volume in Milliliters:", milliliters)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    elif choice == 3:
        try:
            liters = float(input("Enter volume in Liters: "))
            gallons = liters * 0.264172
            print("Volume in Gallons:", gallons)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    elif choice == 4:
        try:
            gallons = float(input("Enter volume in Gallons: "))
            liters = gallons / 0.264172
            print("Volume in Liters:", liters)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    else:
        print("Invalid choice")
    volume_converter()


def main():
    print("Welcome to the Unit Converter!")
    print("Select the type of conversion:")
    print("1. Temperature")
    print("2. Distance")
    print("3. Weight")
    print("4. Volume")
    choice = int(input("Enter your choice (1/2/3/4): "))
    if choice == 1:
        temperature_converter()
    elif choice == 2:
        distance_converter()
    elif choice == 3:
        weight_converter()
    elif choice == 4:
        volume_converter()
    else:
        print("Invalid choice")
        main()


if __name__ == "__main__":
    main()