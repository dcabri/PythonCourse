#!/usr/local/bin/python3
#
# Given that:
# - An astronomical hour consists of 60 minutes
# - An academical hour consists of 40 minutes
# - For each 4 academical hours there are 20 minutes brake
#
# Print out how many astronomical hours a python course should take, 
# if it consists of 64 academical hours, including the respective brakes
#
#
course_duration = 64
#
# Total course duration would be the number of academical hours, 
# plus 1/4 of brake time (or "for each 4 there is 1) 
# Expressed in real hours, we need then to devide the total by 60 minutes
py_course_academic=course_duration * ( 40 + ( 20 / 4 ) )
py_course_astro=py_course_academic / 60

print( py_course_astro )

