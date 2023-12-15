alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(shift , text):

  text1 = list(text)
  text2 = ""

  for letter in text1:
    if letter in alphabet:

      index = alphabet.index(letter)
      if(direction == "encode"):
        index += shift
      elif(direction == "decode"):
        index -= shift
      else:
        print("\n\n\t\t\t ERROR \n\t\t WRONG INPUT\n\t WRITE ENCODE OR DECODE")
        break
      index %= 26
      text2 += alphabet[index]
    elif(letter == " "):
      text2 += " "

  print(text2)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(shift , text)