alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caeser(start_text, shipft_amount, cipher_direction):
    end_text = ""
    for letter in start_text:
        position = alphabet.index(position)
        if cipher_direction == "decode":
         shift_amount *= -1
        new_position = position + shift_amount    
        end_text += alphabet[ne]
        
        
def encrypt (plane_text, shift_amount):
    cipher_text = ""
    for letter in plane_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"the encoded text is {cipher_text}")    
        
encrypt(plane_text=text, shift_amount=shift)        


def decrypt(cipher_text, shift_amount):
    plane_text = ""
    for letter in cipher_text:
       position = alphabet.index(letter)
       new_position = position - shift_amount
       plane_text += alphabet[new_position]
    print(f"the encoded text is {plane_text}")    
       
       
       
    
if  direction == "encode":
    encrypt(plane_text=text, shift_amount=shift)       
elif direction == "decode":
    encrypt(cipher_text=text, shift_amount=shift)        
