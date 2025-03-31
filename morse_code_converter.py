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
from typing import Dict

class MorseCodeConverter:
    """
    A class to convert text to Morse code and play the Morse code as sound.
    """

    # Morse code dictionary
    MORSE_CODE_DICT: Dict[str, str] = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', ' ': '/'
    }

    # Time in milliseconds, frequency in Hz
    DOT_DURATION: int = 200
    DASH_DURATION: int = 600
    FREQUENCY: int = 800

    def __init__(self, text: str) -> None:
        """
        Initialise the MorseCodeConverter class with the text parameter. Accounts for capitalisation with upper method.

        :param text: Text is to be converted to Morse code.
        """
        self.text = text.upper()

    def to_morse(self) -> str:
        """
        Convert stored text to Morse code. Will check for invalid characters.

        :return: String converted to Morse code.
        """
        morse_code = []
        for char in self.text:
            if char in self.MORSE_CODE_DICT:
                morse_code.append(self.MORSE_CODE_DICT[char])
            else:
                print(f"Warning: Character '{char}' cannot be converted to Morse code and will be ignored.")
        return ' '.join(morse_code)

    def play_morse(self) -> None:
        """
        Play Morse code as a series of beeping sounds.

        :return: Short beep per dot, longer beep on dashes and spaces are gaps.
        """
        for symbol in self.to_morse():
            if symbol == '.':
                winsound.Beep(self.FREQUENCY, self.DOT_DURATION)
            elif symbol == '-':
                winsound.Beep(self.FREQUENCY, self.DASH_DURATION)
            elif symbol == ' ':
                time.sleep(0.2)
            elif symbol == '/':
                time.sleep(0.6)
            time.sleep(0.2)

def main() -> None:
    """
    Run the program to convert user input text into Morse code and play the corresponding Morse code sounds.

    :return: None
    """
    user_input: str = input("Enter text to convert to Morse code: ")
    converter: MorseCodeConverter = MorseCodeConverter(user_input)
    print("Morse Code:", converter.to_morse())
    converter.play_morse()

#runs programme and class
if __name__ == "__main__":
   main()

