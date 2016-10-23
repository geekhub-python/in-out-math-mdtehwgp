#!/usr/bin/env python3

schoolboys = int(input('schoolboys count: '))
apples_count = int(input('how many apples: '))

div = apples_count//schoolboys
apples_in_box = apples_count % schoolboys
print('apples per schoolboy: ', div)
print('apples left:', apples_in_box)
