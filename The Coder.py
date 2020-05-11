alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = int(input('Input Key:'))



newmessage = ''

message = input('Please Input Message:')

for character in message:
  if character in alphabet:
     position = alphabet.find(character)
     newposition = (position + key) %26
     newcharacter = alphabet[newposition]
     newmessage += newcharacter
  else:
    newmessage += character 

print'The Coded Message is:', newmessage

