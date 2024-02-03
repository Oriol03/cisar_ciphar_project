alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ','!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']



def encrypt(msg,number):
    new_text=""
    for l in msg:
        try :
            new_position=alphabet.index(l)+number
            new_text+=alphabet[new_position]
        except IndexError:
            position=alphabet.index(l)+number
            new_position=position % 59
            new_text+=alphabet[new_position]
        
            
    print(f"The encrypted text is {new_text}")
        
def decrypt (text,number):
    new_text=""
    for l in text:
        try :
            new_position=alphabet.index(l)-(number%59)
            new_text+=alphabet[new_position]
        except IndexError:
            position=alphabet.index(l)-(number%59)
            new_position=position + 59
            new_text+=alphabet[new_position]
    print(f"The decrypted text is {new_text}")
    
game_over=False
while not game_over :       
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction=="encode":   
        encrypt(text,shift)
    else:
        decrypt(text=text,number=shift)
    
    to_continue=input("\nType 1 to continue and 0 to stop\n")            
    if to_continue=='0':
        game_over=True

