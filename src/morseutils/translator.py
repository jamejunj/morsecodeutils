import time

class MorseCodeTranslator:
    MORSE_CODE_DICT = { 
        'A':'.-', 
        'B':'-...',
        'C':'-.-.', 
        'D':'-..', 
        'E':'.',
        'F':'..-.', 
        'G':'--.', 
        'H':'....',
        'I':'..', 
        'J':'.---', 
        'K':'-.-',
        'L':'.-..', 
        'M':'--', 
        'N':'-.',
        'O':'---', 
        'P':'.--.', 
        'Q':'--.-',
        'R':'.-.', 
        'S':'...', 
        'T':'-',
        'U':'..-', 
        'V':'...-', 
        'W':'.--',
        'X':'-..-', 
        'Y':'-.--', 
        'Z':'--..',
        '1':'.----', 
        '2':'..---', 
        '3':'...--',
        '4':'....-', 
        '5':'.....', 
        '6':'-....',
        '7':'--...', 
        '8':'---..', 
        '9':'----.',
        '0':'-----', 
        ',':'--..--', 
        '.':'.-.-.-',
        '?':'..--..', 
        '/':'-..-.', 
        '-':'-....-',
        '(':'-.--.', 
        ')':'-.--.-',
        ' ':' '
    }

    REV_MORSE_DICT = {}

    @staticmethod
    def encode(message:str, * , 
        mapping=MORSE_CODE_DICT,
        short_char:str='.',
        long_char:str='-',
        seperator:str=' '
    ):
        morse_str = ""
        for char in message.upper():
            if char in mapping:
                morse_str += mapping[char] + seperator
                continue
            raise ValueError(f"The character '{char}' is not supported")
        if short_char != '.': 
            morse_str = morse_str.replace(".", short_char)
        if long_char != '-':
            morse_str = morse_str.replace("-", long_char)
        return morse_str.strip()
    
    @staticmethod
    def decode(morse_str:str, * , 
        mapping:dict=REV_MORSE_DICT,
        short_char:str='.',
        long_char:str='-',
        seperator:str=' ',
        output_seperator:str='',
    ): 
        msg_str = ""
        morse_list = morse_str.split(seperator)
        if short_char != '.' or long_char != '-': 
            morse_list = [code.replace(short_char, ".").replace(long_char, "-") for code in morse_list]

        if len(MorseCodeTranslator.REV_MORSE_DICT) != len(MorseCodeTranslator.MORSE_CODE_DICT):
            MorseCodeTranslator.REV_MORSE_DICT.update({value:key for key, value in MorseCodeTranslator.MORSE_CODE_DICT.items()})

        for code in morse_list:
            if code in mapping:
                msg_str += mapping[code] + output_seperator
                continue
            raise ValueError(f"The code '{code}' is unknown")
        return msg_str.strip()

if __name__ == '__main__':
    pass