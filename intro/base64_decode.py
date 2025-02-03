import base64

message = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
result = bytes.fromhex(message)


result1 = base64.b64encode(result)

result1_str = result1.decode('utf-8')

#print(result)        
print(result1_str)   
