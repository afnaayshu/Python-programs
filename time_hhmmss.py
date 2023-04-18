# Python program to input a time in seconds and print the time in HH:MM:SS format
import math as m
timeip = int(input("Enter the time in seconds : "))
frac_min,hours = m.modf(timeip/3600)
hours=int(hours)
sec_frac, minutes = m.modf(frac_min*60)
minutes = int(minutes)
seconds = int(sec_frac*60)
time_str = str(hours)+":"+str(minutes)+":"+str(seconds)
print("Time in HH:MM:SS format is :",time_str)
