

"""
This module takes start and end time wth space separated hour, minute and seconds.
e.g. 10 20 30 i.e  10 hours, 20 minutes and 30 seconds

example:
from time_arith import time_arg, add_time
start = [10,10,10]
end = [10,10,30]
start_time = time_arg(start)  # it will add time to Time class
end_time = time_arg(end)

addition = add_time(start_time,end_time)
print (addition.hour)
print (addition.second)
print (addition.minute)

This module will not support output in form of days
"""

class Time():
     """Represents the time of day.
          attributes: hour, minute, second
     """

def time_to_int(time):
     hours = time.day*24 + time.hour
     minutes = hours*60 + time.minute
     seconds = minutes*60 + time.second
     return seconds

def int_to_time(seconds):
     time = Time()
     minutes, time.second = divmod(seconds, 60)
     time.hour, time.minute = divmod(minutes, 60)
     time.day, time.hour = divmod(time.hour,24)
     return time

def add_time(start, end):
     seconds = time_to_int(start) + time_to_int(end)
     return int_to_time(seconds)

def sub_time(start, end):
     start = time_to_int(start)
     end = time_to_int(end)
     if end > start:
          seconds = end - start
          return int_to_time(seconds)
     else:
          print ("Start time is greator than end time.")
     
def time_arg(time_string):
     """
     This function will create object of Time class

     """
     time = Time()
     time.day = int(time_string[0])
     time.hour = int(time_string[1])
     time.minute = int(time_string[2])
     time.second = int(time_string[3])
     return time

def main():
     start_time = input("Enter start time [start] :- ")
     end_time  = input("Enter end time [end] :- ")
     start_time = start_time.split()
     end_time = end_time.split()

     start = time_arg(start_time)
     end = time_arg(end_time)

def time_mod(*args):
     start_time = start_time.split()
     end_time = end_time.split()
     start = time_arg(start_time)
     end = time_arg(end_time)

if __name__ == '__main__':
     main()

