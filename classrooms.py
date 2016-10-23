#!/usr/bin/python3
SEATS = 2

scholars = [int(input('scholars in first classroom: ')),
            int(input('scholars in first classroom: ')),
            int(input('scholars in third classroom: ')),
            ]
desks = 0
for scholar in scholars:
    desk = (scholar // SEATS) + (scholar % SEATS)
    desks += desk

print(desks)
