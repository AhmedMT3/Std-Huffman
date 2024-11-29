import os
from Huffman import *

def compressToFile(input_file_path):
    # Read the input file
    with open(input_file_path, 'r') as file:
        input_text = file.read().strip()

    # Calculate character frequencies and build Huffman Tree
    data = calcProb(input_text)
    nodes = sorted([Node(char, prob) for char, prob in OrderedDict(sorted(data.items())).items()],
                   key=lambda node: node.prob, reverse=True)
    root = buildHuffmanTree(nodes)
    huffman_codes = generateCodes(root)

    # Create the compressed binary string
    compressed_binary = ''.join(huffman_codes[char] for char in input_text)

    # Define the output file name with .huff extension
    output_file_path = os.path.splitext(input_file_path)[0] + '.huff'

    # Write the binary string to the output file
    with open(output_file_path, 'wb') as file:
        # Convert the binary string to bytes and write it
        # Ensure that the length of the binary string is a multiple of 8
        padded_binary = compressed_binary + '0' * ((8 - len(compressed_binary) % 8) % 8)
        byte_array = bytearray(int(padded_binary[i:i+8], 2) for i in range(0, len(padded_binary), 8))
        file.write(byte_array)

    print(f"Compressed data has been written to {output_file_path}.")


def decompressFromFile(huff_file_path):
    # Read the binary data from the .huff file
    with open(huff_file_path, 'rb') as file:
        byte_array = file.read()

    # Convert the byte data back into a binary string
    binary_string = ''.join(format(byte, '08b') for byte in byte_array)

    # Rebuild the Huffman tree from the original data or from a predefined table
    # This assumes you have a way to rebuild the tree (e.g., from a file or saved structure)
    # Here, we assume you have the huffman_codes (predefined or saved from compression)
    huffman_codes = {
        'a': '110', 
        'b': '10', 
        'c': '0'
    }

    # Reverse the Huffman codes for decoding
    reverse_huffman_codes = {v: k for k, v in huffman_codes.items()}

    # Decode the binary string into the original text using the Huffman tree
    decoded_text = ''
    current_code = ''
    
    for bit in binary_string:
        current_code += bit
        if current_code in reverse_huffman_codes:
            decoded_text += reverse_huffman_codes[current_code]
            current_code = ''
    
    return decoded_text

# ==========[ Main ]===========
# file_name = input("Enter a file path: ")

# compressToFile(file_name)

decompressed_text = decompressFromFile('file1.huff')
print("Decompressed Text:", decompressed_text)


# data = calcProb(input_text)

# nodes = sorted([Node(char, prob) for char, prob in OrderedDict(sorted(data.items())).items()],
#                key=lambda node: node.prob, reverse=True)


# root = buildHuffmanTree(nodes)

# huffman_codes = generateCodes(root)

# # Display the results
# print("\nHuffman Codes:")
# for char, code in huffman_codes.items():
#     print(f"'{char}': {code}")

# print("\nTree structure:")

# printTree(root)

# AAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBCCCCCCCCCCCCCCCDDDDDDDDDDDDDDEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEFF
