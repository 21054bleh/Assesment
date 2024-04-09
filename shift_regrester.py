l1 = []
l2 = []
encoded = ''
shift_encoder = []
shift_letters = []
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]
numbers = [
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
    '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
    '21', '22', '23', '24', '25', '26'
]
number = 0

l1 = numbers
loop = 0

# functions go here
def encode():
  # turn text to numbers to represent new letters
  number = 0
  encoded = text
  for i in range(26):
    encoded = encoded.replace(letters[number], shift_encoder[number+rightshift])
    number = number + 1


  print(encoded, number)
  
  # turn numbers to text
  number = 0
  for i in range(26):
    encoded = encoded.replace(numbers[number], letters[number])
    print(encoded, number)
    number = number + 1


text = input('Text to encrypt: ')  # Type your text
rightshift = int(input('How much to shift: '))  # How much you want to shift
while loop < rightshift:
     l2 = []
     l2 = l1[1:]
     l2.append(l1[0])
     l1 = []
     l1 = l2
     loop += 1

for i in range(rightshift):
    shift_encoder += "0"
    shift_letters += "0"


print(f'shift encoder = {shift_encoder}')
shift_encoder += l1
shift_letters += letters
print(f'shift encoder = {shift_letters}')
print(f'shift encoder = {shift_encoder}')
encode()
print(f"encoded/decoded = {encoded}")