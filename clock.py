#!/usr/bin/python3
HOURS = 24
MINUTES = 60

n = int(input('n: '))

hours = n // MINUTES % HOURS
minutes = n % MINUTES

print(hours, minutes)
