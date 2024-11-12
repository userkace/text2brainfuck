"""
Text to Brainfuck generator.

This script takes a string as input and generates Brainfuck code
which will print the string.
"""

import argparse


def main():
    """
    Main entry point of the script.
    """
    parser = argparse.ArgumentParser(description='Text to Brainfuck generator.')
    parser.add_argument('--input_string', metavar='S', default="userkace", help='Input string to be converted to Brainfuck code.')
    parser.add_argument('--output_file', metavar='O', help='Output file. If not specified, the output will be sent to the console.')

    args = parser.parse_args()
    """
    True for character after each output line
    False for straight brainfuck code
    """
    brainfuck_code = string_to_brainfuck(args.input_string, True)

    if args.output_file is None:
        print(brainfuck_code)
    else:
        with open(args.output_file, 'w') as file:
            file.write(brainfuck_code)


def character_to_brainfuck(char):
    """
    Convert a single character to Brainfuck code.
    """
    buffer = "[-]>[-]<"
    buffer += "+" * (ord(char) // 10)
    buffer += "[>++++++++++<-]>"
    buffer += "+" * (ord(char) % 10)
    buffer += ".<"
    return buffer


def delta_to_brainfuck(delta):
    """
    Convert a delta (difference between two ASCII values) to Brainfuck code.
    """
    buffer = ""
    buffer += "+" * (abs(delta) // 10)
    buffer += "[>++++++++++<-]>" if delta > 0 else "[>----------<-]>"
    buffer += "+" * (abs(delta) % 10) if delta > 0 else "-" * (abs(delta) % 10)
    buffer += ".<"
    return buffer


def string_to_brainfuck(string, commented):
    """
    Convert a string to Brainfuck code.
    """
    buffer = ""
    if string is None:
        return buffer
    for i, char in enumerate(string):
        if i == 0:
            buffer += character_to_brainfuck(char)
        else:
            delta = ord(string[i]) - ord(string[i - 1])
            buffer += delta_to_brainfuck(delta)
        if commented:
            buffer += ' ' + string[i].strip('+-<>[],.') + '\n'
    return buffer


if __name__ == '__main__':
    main()

