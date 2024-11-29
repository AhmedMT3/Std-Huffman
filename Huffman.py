from collections import OrderedDict

def calcProb(input):
    probs = {}
    for char in set(input):
        count = input.count(char)
        probs[char] = count / len(input)
    return probs


class Node:
    def __init__(self, char, prob) -> None:
        self.char = char
        self.prob = round(prob, 2)
        self.code = None
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f"Node(Char='{self.char}', Prob={self.prob}, Code={self.code})"


def buildHuffmanTree(nodes: list) ->Node:
    while len(nodes) > 1:
        # Take the last two nodes with the smallest probabilities
        left = nodes.pop()
        right = nodes.pop()
        
        # Assign binary codes to the branches
        left.code = 1
        right.code = 0

        # Combine the characters and sum their probabilities
        combined_char = left.char + right.char
        combined_prob = left.prob + right.prob

        # Create a new node for the combined data
        combined_node = Node(combined_char, combined_prob)
        combined_node.left = left
        combined_node.right = right

        # Insert the new node into the list while maintaining descending order by probability
        nodes.append(combined_node)
        nodes.sort(key=lambda node: node.prob, reverse=True)  # Sort descending again

    return nodes[0]  # The final node is the root of the tree


def generateCodes(node, code='', huffman_codes={}):
    if node is not None:
        # If the node is a leaf (character node), store its code
        if len(node.char) == 1:
            huffman_codes[node.char] = code
        generateCodes(node.left, code + '1', huffman_codes)
        generateCodes(node.right, code + '0', huffman_codes)
    return huffman_codes


def printTree(node, prefix="", is_left=True):
    if node is not None:
        connector = "└── " if is_left else "├── "
        print(prefix + connector + f"({node.char}, {node.prob})")
        # Adjust prefix for the left and right branches
        new_prefix = prefix + ("    " if is_left else "│   ")
        printTree(node.left, new_prefix, True)
        printTree(node.right, new_prefix, False)


