#!/usr/bin/python3
"""Calculate time since Epoch"""

import time

def timeEpoch():
    sec_since_Epoch = time.time()
    min_since_Epoch = sec_since_Epoch / 60
    hrs_since_Epoch = min_since_Epoch / 60
    days_since_Epoch = hrs_since_Epoch / 24
    mnths_since_Epoch = days_since_Epoch / 12
    years_since_Epoch = days_since_Epoch / 365

    print(f"\nThe following are calculation of time since Epoch")

    print(f"\nSeconds: {sec_since_Epoch}\nMinutes: {min_since_Epoch}\nHours: {hrs_since_Epoch}\nDays: {days_since_Epoch}\nMonths: {mnths_since_Epoch}\nYears: {years_since_Epoch}")

timeEpoch()
