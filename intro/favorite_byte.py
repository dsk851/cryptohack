from pwn import xor
from os import * 

puzzle = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')
  
for cle in range(0,256):
    test = xor(puzzle,cle)
    print(test)