"""
What it is:
Text converter that will turn a string value into Morse Code using a dictionary.

How to use:
Run the code and input any string value into the interpreter, will print the result as Morse Code.

Made by:
Jacob Fairhurst
"""

import time
import winsound

class MorseCodeConverter:
    """
    A class to convert text to Morse code and play the Morse code as sound.
    """

    #Morse code dictionary
    MORSE_CODE_DICT = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', ' ': '/'
    }

    #time in milliseconds, frequency in Hz
    DOT_DURATION = 200
    DASH_DURATION = 600
    FREQUENCY = 800

    def __init__(self, text):
        """
        Initialises the MorseCodeConverter class with the text parameter. Accounts for capitalisation with upper method.

        :param text: Text is to be converted to Morse code.
        """
        self.text = text.upper()

    def to_morse(self):
        """
        Converts stored text to Morse code.

        :return: String converted to Morse code.
        """
        return ' '.join(self.MORSE_CODE_DICT[char] for char in self.text if char in self.MORSE_CODE_DICT)

    def play_morse(self):
        """
        Plays Morse code as a series of beeping sounds.

        :return: Short beep per dot, longer beep on dashes and spaces are gaps.
        """
        morse_code = self.to_morse()
        for symbol in morse_code:
            if symbol == '.':
                winsound.Beep(self.FREQUENCY, self.DOT_DURATION)
            elif symbol == '-':
                winsound.Beep(self.FREQUENCY, self.DASH_DURATION)
            elif symbol == ' ':
                time.sleep(0.2)
            elif symbol == '/':
                time.sleep(0.6)
            time.sleep(0.2)


#runs programme and class
if __name__ == "__main__":
    user_input = input("Enter text to convert to Morse code: ")
    converter = MorseCodeConverter(user_input)
    print("Morse Code:", converter.to_morse())
    converter.play_morse()

