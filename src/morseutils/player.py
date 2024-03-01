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
        verbose=False,
    ):
        CHAR_BREAK_S = self.CHARACTER_BREAK_MS / 1000
        SPACE_BREAK_S = self.SPACE_BREAK_MS / 1000
        if verbose:
            morse_str = morse_str + ' '
            print(f"start playing : {morse_str}")
        for i, char_code in enumerate(morse_str):
            if verbose:
                print(self.__highlight_at(i, morse_str), end='\r', flush=True)
            if char_code == short_char:
                winsound.Beep(self.BEEP_FREQ, self.BEEP_DURATION_MS)
                time.sleep( CHAR_BREAK_S )
            if char_code == long_char:
                winsound.Beep(self.BEEP_FREQ, self.BEEP_LONG_DURATION_MS)
                time.sleep( CHAR_BREAK_S )
            if char_code == seperator:
                time.sleep( SPACE_BREAK_S )
        if verbose:
            print(f"\ncompleted : {morse_str}")
        return morse_str

    def __highlight_at(self, index, morse_str, color='91'):
        if morse_str[index] == ' ':
            return  morse_str[:index] + f"■" + morse_str[index+1:]
        return morse_str[:index] + f"\033[{color}m" + morse_str[index] + "\033[0m" + morse_str[index+1:]
    
if __name__ == '__main__':
    pass