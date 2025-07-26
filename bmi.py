def calculate_bmi(weight, height):
    """
    Calculate BMI using weight (in kg) and height (in meters)
    Formula: BMI = weight / (height^2)
    """
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    """
    Interpret the BMI value according to WHO standards
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("BMI Calculator")
    print("--------------")
    
    try:
        # Get user input
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        
        # Interpret BMI
        category = interpret_bmi(bmi)
        
        # Display results
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}")
        
    except ValueError:
        print("Please enter valid numerical values for weight and height.")

if __name__ == "__main__":
    main()