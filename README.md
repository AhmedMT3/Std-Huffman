
# Huffman Compression and Decompression Program

This Python program implements the Standard Huffman Encoding algorithm for compressing and decompressing text files. It allows you to reduce file sizes while maintaining the integrity of the original content.

## Features
- **Compression**: Compress text files into a `.huff` binary file format.
- **Decompression**: Restore the original file content and its extension from a `.huff` file.
- Displays the Huffman Tree and codes for debugging or educational purposes.

## How It Works
1. **Compression**:
   - The program calculates the frequency of characters in the input file.
   - It builds a Huffman Tree and generates binary codes for each character.
   - The file is compressed into a `.huff` file, which includes:
     - The Huffman codes (header).
     - The binary data (body).
     - The original file extension.

2. **Decompression**:
   - Reads the Huffman codes and original file extension from the `.huff` file.
   - Decodes the binary data back to the original text.
   - Restores the file with its original extension.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/AhmedMT3/Std-Huffman.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Std-Huffman
   ```

## Usage
Run the program from the command line:

```bash
python main.py
```

### Menu Options
1.  **Compress a File**: Provide the name of the text file (located in the `Playground` folder) to compress.
2.  **Decompress a File**: Provide the name of the `.huff` file (located in the `Playground` folder) to decompress.

### Example
#### Compress
- Input file: `example.txt`
- Output file: `example.huff`

#### Decompress
- Input file: `example.huff`
- Output file: `example.txt` (restored with the original content and extension).

## Dependencies
- Python 3.x
- No external libraries are required.

## Limitations
- Only processes text files.
- Requires the compressed file to contain the Huffman codes header for decompression.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Feel free to fork this repository, open issues, and submit pull requests to improve the project.

---

**Author**: [Ahmed M-T]

