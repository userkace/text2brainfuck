# text2brainfuck

A Python script that converts any text string into Brainfuck code that outputs the original string when executed.

## Overview

This script takes a string as input and generates optimized Brainfuck code that will print the string. It uses an efficient algorithm that minimizes code length by leveraging the difference between consecutive characters.

## Features

- **Optimized Code Generation**: Uses delta encoding to minimize Brainfuck code length
- **Commented Output**: Optional character comments for better readability
- **File Output**: Save generated Brainfuck code to files
- **Command Line Interface**: Easy-to-use CLI with argparse

## Installation

No external dependencies required. Just ensure you have Python 3.6+ installed:

```bash
python --version
```

## Usage

### Basic Usage

Convert the default string "userkace":

```bash
python text2brainfuck.py
```

### Custom String

Convert your own string:

```bash
python text2brainfuck.py --input_string "Hello, World!"
```

### Save to File

Save the Brainfuck code to a file:

```bash
python text2brainfuck.py --input_string "Hello" --output_file hello.bf
```

### Commented vs Uncommented Output

The script generates commented output by default (character after each line). To get clean Brainfuck code, modify the `commented` parameter in the `string_to_brainfuck()` call.

## Command Line Arguments

- `--input_string` (optional): The string to convert to Brainfuck. Default: "userkace"
- `--output_file` (optional): Output file path. If not specified, prints to console

## How It Works

### Algorithm

1. **First Character**: Uses absolute positioning with `character_to_brainfuck()`
2. **Subsequent Characters**: Uses delta encoding with `delta_to_brainfuck()` to minimize code
3. **Optimization**: Leverages multiplication loops (`[>++++++++++<-]`) for efficient number generation

### Code Structure

- `character_to_brainfuck(char)`: Converts first character using absolute ASCII value
- `delta_to_brainfuck(delta)`: Converts character differences using optimized loops
- `string_to_brainfuck(string, commented)`: Main conversion function with optional comments

## Technical Details

- **Memory Management**: Uses two cells for efficient character generation
- **Loop Optimization**: Employs multiplication loops for numbers > 10
- **Delta Encoding**: Minimizes code by using character differences
- **ASCII Support**: Full ASCII character set support (0-127)

## Contributing

Feel free to submit issues and enhancement requests!

---

**Note**: The default input string is set to "userkace" but can be easily modified in the script or overridden via command line arguments.
