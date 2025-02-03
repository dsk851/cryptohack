from pwn import * 

if __name__ == '__main__' :
    message = bytes('label', 'utf-8')
    
    resulat = xor(message, 13)
    print(resulat)
    

    
