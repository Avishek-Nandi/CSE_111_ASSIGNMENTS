# Solution to Task 1 (Function)

def bmi_calculator(height, mass):
    bmi = mass / ((height/100)**2)
    status = "Underweight" if bmi < 18.5 else "Normal" if 18.5 <= bmi <= 24.9 else "Overweight" \
        if 25 <= bmi <= 30 else "Obese"
    print(f"Score is {bmi:.1f}. You are {status}")


if __name__ == "__main__":
    height, mass = [int(i) for i in input().strip("() ").split(",")]
    bmi_calculator(height, mass)
