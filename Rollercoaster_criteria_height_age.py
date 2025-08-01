print("welcome to rollercoaster ride!")
height= int(input("what is your height in cm? "))
if height >= 120:
    print("you are eligible for a rollercoaster ride")
    age = int(input("my age is "))
    if age <=18:
        print("you should pay 50 rupees")
    elif age >= 25:
            print(" you should pay 100 rupees")
    else:
        print("you should pay 20 rupess ")
else:
    print("sorry! you are not eligible for rollercoaster ride ")
