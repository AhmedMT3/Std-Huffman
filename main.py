from Huffman import *

# ==========[ Main ]===========
def main():
    
    print("Huffman Compression Program")
    print("1. Compress a file")
    print("2. Decompress a file")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == '1':
        input_file = input("Enter the name of the file (located in 'Playground'): ").strip()
        try:
            compressToFile(input_file)
        except FileNotFoundError:
            print(f"Error: File '{input_file}' not found.")
        except Exception as e:
            print(f"Error occurred during compression: {e}")

    elif choice == '2':
        huff_file = input("Enter the name of the .huff file (located in 'Playground'): ").strip()
        try:
            decompressed_text = decompressFromFile(huff_file)
            print("\nDecompressed Text:")
            print(decompressed_text)
        except FileNotFoundError:
            print(f"Error: File '{huff_file}' not found.")
        except Exception as e:
            print(f"Error occurred during decompression: {e}")

    else:
        print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()

# AAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBCCCCCCCCCCCCCCCDDDDDDDDDDDDDDEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEFF
