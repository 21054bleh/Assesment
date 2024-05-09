l1 = []
l2 = []
encoded = ''
dashdecor = '-=-=-=-=-=-=-=-=-='
rightshift = 0
choseninput = ''
shift_encoder = []
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
    # loops for every letter turning to number
    for i in range(26):
        #if a letter is in the list then it changes it to the apropriate number
        if letters[i] in textlist2:
            textlist2 = [sub.replace(letters[i], shift[i + rightshift]) for sub in textlist2]
    return textlist2

def decode_num(textlist2,shift):
    #loops for every number turning to letter
    for i in range(25,-1,-1):
        #if a number is in the list then it changes it to the apropriate letter
        if numbers[i] in textlist2:
            textlist2 = [sub.replace(shift[i], letters[i]) for sub in textlist2]
    return textlist2



# input your text
while choseninput != "":
    choseninput = input('Text to encrypt: ')  # Type your text
while rightshift != 0:
    try :
        rightshift = int(input('How much to shift: '))  # How much you want to shift
    except ValueError:
        print('Sorry please enter a number')
lengthoftext = len(text)
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

for i in range(lengthoftext // 2):
    dashdecor += "-="


shift_encoder += l1
encode_numb = encode_num(textlist, shift_encoder)
encode_done = decode_num(encode_numb, numbers)
encoded = ''.join(encode_done)
print(f"\n{dashdecor}-\n\nencoded/decoded: {encoded}")