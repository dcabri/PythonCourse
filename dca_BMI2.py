#!/usr/local/bin/python3
#
# Calculate your body mass index (BMI)
# given the formula: BMI = W / (H*H)
#
#If your BMI is:
#below 18.5 - you're in the underweight range
#between 18.5 and 24.9 - you're in the healthy weight range
#between 25 and 29.9 - you're in the overweight range
#between 30 and 39.9 - you're in the obese range 
#
#
# Body weight as measured in kilograms (kg)
weight = int(input("Enter your weigth (kg): "))
# Body height as measured in meters
height = float(input("Enter your height (m): "))
bmi = round( weight / (height * height ), 2 )

if bmi < 19 :
  print("{} is in the underweight range".format(bmi))
elif bmi < 25 :
  print("{} is in the healthy weight range".format(bmi))
elif bmi < 30 :
  print("{} is in the overweight range".format(bmi))
elif bmi < 40 :
  print("{} is in the obese range".format(bmi))
elif bmi > 40 :
  print("{} is undefined (above obese)".format(bmi))
print("-" * 20)
