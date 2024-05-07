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
#number = 0

textlist2 = []
l1 = numbers
loop = 0
numbercount = 0

# functions go here
def encode_num(textlist2,shift):
    print(rightshift)
    print(shift)
    for i in range(26):
        if letters[i] in textlist2:
            textlist2 = [sub.replace(letters[i], shift[i + rightshift]) for sub in textlist2]
    return textlist2

def encode_lett(textlist2,shift):
    for i in range(25,-1,-1):
        if numbers[i] in textlist2:
            textlist2 = [sub.replace(shift[i], letters[i]) for sub in textlist2]
    print(textlist2)
    return textlist2




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


shift_encoder += l1
shift_letters += letters
encode_numb = encode_num(textlist, shift_encoder)
print(f"\nencode_numb = {encode_numb}\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n\n")
encode_done = encode_lett(encode_numb, numbers)
print(f"encoded/decoded = {encoded}")