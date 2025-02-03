from pwn import xor
from Crypto.Util.number import * 

# KEY1 =  bytes('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
# KEY21 = KEY2 ^ KEY1 = bytes('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e')
# KEY23 = KEY2 ^ KEY3 = bytes('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
# KEY123 = FLAG ^ KEY1 ^ KEY3 ^ KEY2 = bytes('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')

# Commutative: A ⊕ B = B ⊕ A
# Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
# Identity: A ⊕ 0 = A
# Self-Inverse: A ⊕ A = 0

KEY1 =  bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
KEY21 = bytes.fromhex('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e')
KEY23 = bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
KEY123 = bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')

KEY2 = xor(xor(KEY21, KEY1))
KEY3 = xor(KEY2,KEY23)

FLAG = xor(xor(xor(KEY123,KEY2),KEY3),KEY1)
resutat = bytes_to_long(FLAG)

resultatfinal = FLAG.decode('utf-8')
print(resultatfinal)