from datetime import datetime
from datetime import timedelta
import math, random

def time_diff(dt1, dt2):
    time_delta = (dt2 - dt1)
    total_seconds = time_delta.total_seconds()
    minutes = int(total_seconds/60)
    return minutes

def generateOTP() : 
    digits = "0123456789"
    OTP = "" 
    for i in range(6): 
        OTP += digits[math.floor(random.random() * 10)] 
    return OTP 
