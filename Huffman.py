import os
from collections import OrderedDict


class Node:
    def __init__(self, char, prob) -> None:
        self.char = char
        self.prob = round(prob, 2)
        self.code = None
        self.left = None
        self.right = None


def calcProb(input_text):
    probs = {}
    for char in set(input_text):
        count = input_text.count(char)
        probs[char] = count / len(input_text)
    return probs


def buildHuffmanTree(nodes: list) -> Node:
    while len(nodes) > 1:
    
        left = nodes.pop()
        right = nodes.pop()

        left.code = 1
        right.code = 0

        combined_char = left.char + right.char
        combined_prob = left.prob + right.prob

        combined_node = Node(combined_char, combined_prob)
        combined_node.left = left
        combined_node.right = right

        nodes.append(combined_node)
        nodes.sort(key=lambda node: node.prob, reverse=True)

    return nodes[0]


def generateCodes(node, code='', huffman_codes={}):
    if node is not None:
        if len(node.char) == 1:
            huffman_codes[node.char] = code
        generateCodes(node.left, code + '1', huffman_codes)
        generateCodes(node.right, code + '0', huffman_codes)
    return huffman_codes


def compressToFile(input_file_path):
    
    with open('Playground/' + input_file_path, 'r') as file:
        input_text = file.read().strip()

    data = calcProb(input_text)
    nodes = sorted([Node(char, prob) for char, prob in OrderedDict(sorted(data.items())).items()],
                   key=lambda node: node.prob, reverse=True)
    root = buildHuffmanTree(nodes)
    huffman_codes = generateCodes(root)

    compressed_binary = ''.join(huffman_codes[char] for char in input_text)

    output_file_path = os.path.splitext('Playground/' + input_file_path)[0] + '.huff'
    with open(output_file_path, 'wb') as file:
        padded_binary = compressed_binary + '0' * ((8 - len(compressed_binary) % 8) % 8)
        byte_array = bytearray(int(padded_binary[i:i+8], 2) for i in range(0, len(padded_binary), 8))
        file.write(byte_array)

    print(f"Compressed data has been written to {output_file_path}.")


def decompressFromFile(huff_file_path):
   
    huffman_codes = {
        'A': '11', 
        'B': '10', 
        'C': '001',
        'D' : '0000',
        'E' : '01',
        'F' : '0001'
    }
    reverse_huffman_codes = {v: k for k, v in huffman_codes.items()}

    with open('Playground/' + huff_file_path, 'rb') as file:
        byte_array = file.read()

    binary_string = ''.join(format(byte, '08b') for byte in byte_array)
    decoded_text = ''
    current_code = ''

    for bit in binary_string:
        current_code += bit
        if current_code in reverse_huffman_codes:
            decoded_text += reverse_huffman_codes[current_code]
            current_code = ''

    return decoded_text
