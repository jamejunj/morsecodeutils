import winsound
import time
from morseutils.translator import MorseCodeTranslator as MCT

class MorseCodePlayer(MCT):
    def __init__(self):
        self.BEEP_FREQ = 600
        self.BEEP_DURATION_MS = 100
        self.BEEP_LONG_DURATION_MS = self.BEEP_DURATION_MS * 3
        self.CHARACTER_BREAK_MS =  50
        self.SPACE_BREAK_MS = 200

    def play(self, 
        message_str, *, 
        verbose=False
    ):
        return self.play_morse(self.encode(message_str), verbose=verbose)
    
    def play_morse(self, morse_str, *,
        short_char:str='.',
        long_char:str='-',
        seperator:str=' ',
        verbose=False
    ):
        if verbose:
            print(f"start message: {morse_str}")
        for char_code in morse_str:
            if char_code == short_char:
                winsound.Beep(self.BEEP_FREQ, self.BEEP_DURATION_MS)
                time.sleep( self.CHARACTER_BREAK_MS / 1000)
            if char_code == long_char:
                winsound.Beep(self.BEEP_FREQ, self.BEEP_LONG_DURATION_MS)
                time.sleep( self.CHARACTER_BREAK_MS / 1000)
            if char_code == seperator:
                time.sleep( self.SPACE_BREAK_MS / 1000)
        if verbose:
            print(f"end message: {morse_str}")
        return morse_str

    
if __name__ == '__main__':
    pass