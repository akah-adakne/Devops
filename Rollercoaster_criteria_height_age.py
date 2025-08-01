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

# output 1 : height > 120 and age is >= 25
# what is your height in cm? 130
# you are eligible for a rollercoaster ride
# my age is 25
#  you should pay 100 rupees

# Process finished with exit code 0


# output 2 : height<120 
# "C:\Users\AKASH ADAKNE\PyCharmMiscProject\.venv\Scripts\python.exe" "C:\Users\AKASH ADAKNE\PyCharmMiscProject\rollercoaster_height_age.py" 
# welcome to rollercoaster ride!
# what is your height in cm? 118
# sorry! you are not eligible for rollercoaster ride 

# Process finished with exit code 0


