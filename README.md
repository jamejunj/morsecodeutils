# Python Morse Code Utils

A python morse code encoder / decoder with window morsecode player

This package contains:
1. translator
2. player

## Translator
```python
from morseutils.translator import MorseCodeTranslator as mct

mct.encode('hello') # return '.... . .-.. .-.. ---'
mct.decode('.- .-.') # return 'AR'
```
## Player

```python
from morseutils.player import MorseCodePlayer

mcp = MorseCodePlayer() 

mcp.play('hello') # play hello morse code
mcp.play_morse('.- .-.') # play .- .-.
```

### Customization
```python
from morseutils.player import MorseCodePlayer

mcp = MorseCodePlayer() 

mcp.BEEP_FREQ = 600
mcp.BEEP_DURATION_MS = 100
mcp.BEEP_LONG_DURATION_MS = 300
mcp.CHARACTER_BREAK_MS =  50
mcp.SPACE_BREAK_MS = 200
```