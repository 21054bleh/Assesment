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

textlist2 = []
l1 = numbers
loop = 0

# functions go here
def encode():
    number = 0
    textlist2 = []
    print(textlist2)
    for i in range(26):
        print(f"number = {number}")
        if letters[number] in textlist:
            print(f"letter = {shift_letters[number + rightshift]}, number = {numbers[number]} + {rightshift} = {numbers[number + rightshift]}")
            textlist2 = [sub.replace(letters[number], numbers[number + rightshift]) for sub in textlist]
        else:
            # Handle the case when the index is out of range
            print(f"letter = {letters[number]} not in list, number {numbers[number]}")
        print(textlist2)
        number += 1



text = input('Text to encrypt: ')  # Type your text
rightshift = int(input('How much to shift: '))  # How much you want to shift
len_oftext = len(text)  # grabs the lengh of text
print(f"Len = {len_oftext}")  # remove when done -----
textlist = list(text)   # turns text into list

# shifts letters over
while loop < rightshift:
     l2 = []
     l2 = l1[1:]
     l2.append(l1[0])
     l1 = []
     l1 = l2
     loop += 1


# adds place holder numbers for shift
for i in range(rightshift):
    shift_encoder += "0"
    shift_letters += "0"


print(f'shift encoder = {shift_encoder}')  # remove when done -----
shift_encoder += l1
shift_letters += letters
print(f'shift letters = {shift_letters}')  # remove when done -----
print(f'shift encoder = {shift_encoder}')  # remove when done -----
print(text)
encode()
print(f"encoded/decoded = {encoded}")
print(textlist2)