title: --- La cave ---

Ça sent la poussière par ici ...

P'têt que tu trouveras des trucs _tout au fond_ .

<br /><br /><br />
<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />
<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />


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
        s = s.upper() * 3
        return 'Mais pour le moment, je fais : {}!'.format(s)


    txt1 = to_morse('Salut Elliot')
    txt2 = from_morse('- ..-  ...- .- ...  -... .. . -.  ..--..')
    txt3 = to_bipbop("C'est cool !")
    txt4 = "J'aurais bientôt un Samsung tout neuf !"

    print(txt1)
    print(txt2)
    print(txt3)
    print(txt4.replace('Samsung', 'Iphone SE'))

    # Essaye de changer la fonction from_bipbop() pour traduire ce qui dit le robot.
    # Tu as ici tout ce qu'il faut pour y parvenir. 

    print( from_bipbop('prout ') ) # <- Je suis sûr que c'est encore un coup des loupiaux ça !
