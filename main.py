"""
What it is:
Text converter that will turn a string value into Morse Code using a dictionary.

How to use:
Run the code and input any string value into the interpreter, will print the result as Morse Code.

Made by:
Jacob Fairhurst
"""

#Morse Code Dictionary as constant
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'
}


def text_to_morse(text):
    """Converts a string to morse code. Takes a text parameter. Converts input to uppercase
    Appends input string values from main() to an empty string, then joins together as a
    translation from the MORSE_CODE_DICT dictionary. Will only take letters or numbers."""
    text = text.upper()
    for char in text:
        if char not in MORSE_CODE_DICT:
            print("Please enter a valid letter or number.")
            return main()
        else:
            morse_code = ' '.join(MORSE_CODE_DICT[char] for char in text if char in MORSE_CODE_DICT)
            return morse_code

def main():
    """Function to call main script. Takes the input string value to convert to morse code."""
    user_input = input("Write a message to convert to Morse Code: ")
    print(f"Morse code reads: {text_to_morse(user_input)}")


main()

