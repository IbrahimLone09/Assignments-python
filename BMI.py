weight = float(input("Enter your weight in kgs: "))
prefunit = input(
    "What is your preffered unit of height (type (F) feet and (M) for meters): ").upper()

if prefunit == "F":
    print("You will enter your height given as feet and inches ")
    feet = float(input("Enter you height in feet: "))
    inches = float(input("Enter your height in inches: "))

elif prefunit == "M":
    height = float(input("what is your height in meters: "))

if prefunit == "F":
    height = ((feet * 12 + inches) * 2.54) / 100


BMI = weight / (height * height)

if BMI < 18.5:
    print("underweight")

elif 18.5 <= BMI < 25:
    print("normal")

elif 25 <= BMI < 30:
    print("overweight")

elif BMI >= 30:
    print("very overweight")

print(BMI) 
