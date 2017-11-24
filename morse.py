CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',

        "." : ".-.-.-",
        "," : "--..--",
        "?" : "..--..",
        "'" : ".----.",
        "!" : "-.-.-----.",
        "/" : "-..-.",
        ":" : "---...",
        "-" : "-....-",
        "@" : ".--.-.",
        "=" : "-...-"
        }

CODE_REVERSED = {value:key for key,value in CODE.items()}

BIP_CODE = {'.': 'Bip', '-': 'Bop', ' ': ' '}

def to_morse(s):
    mots = s.split()
    for i, mot in enumerate(mots):
        mots[i] = ' '.join(CODE.get(j.upper()) for j in mot)
    return '  '.join(mots)

def from_morse(s):
    s = s.replace('  ', 'w')
    mots = s.split('w')
    for i, mot in enumerate(mots):
        mots[i] = ''.join(CODE_REVERSED.get(i) for i in mot.split())
    return ' '.join(mots)

def to_bipbop(s):
    s = to_morse(s)
    return ''.join(BIP_CODE.get(i) for i in s)

def from_bipbop(s):
    s = s.replace('Bip', '.').replace('Bop', '-')
    return from_morse(s)
