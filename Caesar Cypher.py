uppercase = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
    "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]
lowercase = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]
error=""
choice=""
text_to_cipher=""
key_to_cipher=""

def check_choice_is_valid(choice):
  while True:
    if choice == "e":
      print(
          f"\nThe encrypted text is:\n{encrypt(text_to_cipher, key_to_cipher)}")
      break
    elif choice == "d":
      print(
          f"\nThe decrypted text is:\n{decrypt(text_to_cipher, key_to_cipher)}")
      break
    else:
      choice=input("\nPlease enter either 'e' or 'd'\n")


def encrypt(text, shift):
  i = len(text)
  encrypted_text = ""
  letter = 1
  for letter in range(i):
    if text[letter] in uppercase:
      index = uppercase.index(text[letter])
      encrypted_text += uppercase[(int(index) + int(shift)) % 26]
      letter += 1
    elif text[letter] in lowercase:
      index = lowercase.index(text[letter])
      encrypted_text += lowercase[(int(index) + int(shift)) % 26]
      letter += 1
    else:
      encrypted_text += text[letter]
      letter += 1
  return encrypted_text


def decrypt(text, shift):
  i = len(text)
  decrypted_text = ""
  letter = 1
  for letter in range(i):
    if text[letter] in uppercase:
      index = uppercase.index(text[letter])
      decrypted_text += uppercase[(int(index) - int(shift)) % 26]
      letter += 1
    elif text[letter] in lowercase:
      index = lowercase.index(text[letter])
      decrypted_text += lowercase[(int(index) - int(shift)) % 26]
      letter += 1
    else:
      decrypted_text += text[letter]
      letter += 1
  return decrypted_text


print("Welcome to the Caesar Cipher!")
while True:
  text_to_cipher = input("\nEnter your text:\n")
  while len(text_to_cipher) <1:
    for i in range(1):
     print("\033[F\033[K", end='')
    text_to_cipher = input("\nPlease enter some text:\n")

  key_to_cipher = input("\nEnter the key (it should be  a number (between 1 and 26)):\n")
  while not key_to_cipher.isnumeric() or not (1 <= int(key_to_cipher) <= 26):
    for i in range(2):
      print("\033[F\033[K", end='')
    key_to_cipher=input("Please enter a number (which is in between 1 and 26): \n")


  print("\nWould you like to encrypt or decrypt?")
  choice = input("Enter 'e' to encrypt or 'd' to   decrypt:\n")

  check_choice_is_valid(choice)
  
  continue_action=input("\nWould you like to continue? Enter 'y' to continue or any other key to exit this program:\n")
  if continue_action == "y":
    print("\n")
    continue
  else:
    print("\nThank you for using the Caesar Cipher!")
    break