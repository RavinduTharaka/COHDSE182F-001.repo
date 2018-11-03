def encrypt(string, shift):
 
  a = ''
  for char in string:
    if char.isalpha(): 
     if char == ' ':
       a = a + char
     elif  char.isupper():
       a = a + chr((ord(char) + shift - 65) % 26 + 65)
     else:
       a = a + chr((ord(char) + shift - 97) % 26 + 97)
    else:
     print("Please enter characters")
  
  return a

def decrypt(string, shift):
 
  a = ''
  for char in string:
    if char.isalpha(): 
     if char == ' ':
       a = a + char
     elif  char.isupper():
       a = a + chr((ord(char) - shift - 65) % 26 + 65)
     else:
       a = a + chr((ord(char) - shift - 97) % 26 + 97)
    else:
     print("Please enter characters")
  
  return a
 
print("Select your choice")
c=input("e - Encript \nd - Decript\t")

if c=='e':
 text = input("enter string: ")
 print("after encryption: ",encrypt(text, 3))
elif c=='d':
 text = input("enter string: ")
 print("after decryption: ",decrypt(text, 3))
else:
 print("Invalid Choice")
