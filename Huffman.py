import os
import pickle

class Node:
    def __init__(self, char, prob) -> None:
        self.char = char
        self.prob = round(prob, 2)
        self.code = None
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f"Node(Char='{self.char}', Prob={self.prob}, Code={self.code})"


class Huffman:
    def __init__(self):
        self.huffman_codes = {}

    def calcProb(self, input_text):
        """Calculate the probability of each character in the input text."""
        probs = {}
        for char in set(input_text):
            count = input_text.count(char)
            probs[char] = count / len(input_text)
        return probs

    def buildHuffmanTree(self, nodes: list) -> Node:
        """Build the Huffman tree and return its root."""
        while len(nodes) > 1:
            left = nodes.pop()
            right = nodes.pop()

            # Assign binary codes to the branches
            left.code = 1
            right.code = 0

            # Combine the characters and probabilities
            combined_char = left.char + right.char
            combined_prob = left.prob + right.prob

            # Create a new node for the combined data
            combined_node = Node(combined_char, combined_prob)
            combined_node.left = left
            combined_node.right = right

            # Insert the new node into the list and sort
            nodes.append(combined_node)
            nodes.sort(key=lambda node: node.prob, reverse=True)

        return nodes[0]

    def generateCodes(self, node, code=''):
        """Generate the Huffman codes for each character."""
        if node is not None:
            if len(node.char) == 1:
                self.huffman_codes[node.char] = code
            self.generateCodes(node.left, code + '1')
            self.generateCodes(node.right, code + '0')
            
#=============================[ Compress ]===========================

    def compressToFile(self, input_file_path):
        with open('Playground/' + input_file_path, 'r') as file:
            input_text = file.read().strip()

        # Calculate character frequencies and build Huffman Tree
        data = self.calcProb(input_text)
        nodes = sorted([Node(char, prob) for char, prob in sorted(data.items())], key=lambda node: node.prob, reverse=True)
        root = self.buildHuffmanTree(nodes)
        self.generateCodes(root)

        # Create the compressed binary string
        compressed_binary = ''.join(self.huffman_codes[char] for char in input_text)

        # Define the output file name with .huff extension
        output_file_path = os.path.splitext('Playground/' + input_file_path)[0] + '.huff'
        original_extension = os.path.splitext(input_file_path)[1]  # Get the original file extension

        with open(output_file_path, 'wb') as file:
            # Save Huffman codes and original extension (header)
            pickle.dump((self.huffman_codes, original_extension), file)

            # Save the binary data (body)
            padded_binary = compressed_binary + '0' * ((8 - len(compressed_binary) % 8) % 8)
            byte_array = bytearray(int(padded_binary[i:i+8], 2) for i in range(0, len(padded_binary), 8))
            file.write(byte_array)

        print("\nHuffman Tree:")
        self.printTree(root)
        print("\nHuffman code:")
        self.printCodesTable(self.huffman_codes)

        print(f">>>>> Compressed data has been written to '{output_file_path}' <<<<<<<<<\n")

#=============================[ DeCompress ]============================

    def decompressFromFile(self, huff_file_path):
        full_path = os.path.join('Playground', huff_file_path)
        if not os.path.exists(full_path):
            print(f"Error: File '{full_path}' not found.")
            return

        with open(full_path, 'rb') as file:
            # Load Huffman codes and original extension (header)
            self.huffman_codes, original_extension = pickle.load(file)

            # Load the binary data (body)
            byte_array = file.read()

        # Convert the byte data back into a binary string
        binary_string = ''.join(format(byte, '08b') for byte in byte_array)

        # Reverse the Huffman codes for decoding
        reverse_huffman_codes = {v: k for k, v in self.huffman_codes.items()}

        # Decode the binary string into the original text
        decoded_text = ''
        current_code = ''

        for bit in binary_string:
            current_code += bit
            if current_code in reverse_huffman_codes:
                decoded_text += reverse_huffman_codes[current_code]
                current_code = ''

        # Restore the original file extension
        output_file_path = os.path.splitext(full_path)[0] + original_extension

        with open(output_file_path, 'w') as output_file:
            output_file.write(decoded_text)

        print(f">>>>> DeCompressed content has been written to '{output_file_path}' <<<<<<<<<\n")


    def printTree(self, node, prefix="", is_left=True, output_file=None):
        if node is not None:
            connector = "└── " if is_left else "├── "
            line = prefix + connector + f"({node.char}, {node.prob})\n"
            if output_file:
                output_file.write(line)
            else:
                print(line, end="")
            
            # Adjust prefix for the left and right branches
            new_prefix = prefix + ("    " if is_left else "│   ")
            self.printTree(node.left, new_prefix, True, output_file)
            self.printTree(node.right, new_prefix, False, output_file)
    
    def printCodesTable(self, huff_codes: dict):
        print("---------------------")
        for char, prob in huff_codes.items():
            print(f"{char} | {prob}")
        print("---------------------")
        