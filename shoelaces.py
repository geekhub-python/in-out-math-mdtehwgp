#!/usr/bin/python3

aa = int(input('aa = ')) # 2
bb = int(input('bb = ')) # 1
ll = int(input('ll = ')) # 3
NN = int(input('NN = ')) # 4

large = (ll * 2) + (((NN*2)-1) * aa) + (bb * (NN - 1) * 2) # some magic math
print(large)
