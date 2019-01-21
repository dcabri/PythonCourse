#!/usr/local/bin/python3
#
# Calculate your body mass index (BMI)
# given the formula: BMI = W / (H*H)
#
#
# Body weight as measured in kilograms (kg)
weight=64
# Body height as measured in meters
height=1.74
bmi = round( weight / (height * height ), 2 )

print( bmi )

