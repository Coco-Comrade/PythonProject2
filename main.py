import sys
import logging
#Logging config
logging.basicConfig(filename="Encryption.log", level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
FILE = "output.txt"

encoding_map = {
        "A": 56, "B": 57, "C": 58, "D": 59, "E": 40, "F": 41, "G": 42, "H": 43, "I": 44,
        "J": 45, "K": 46, "L": 47, "M": 48, "N": 49, "O": 60, "P": 61, "Q": 62,
        "R": 63, "S": 64, "T": 65, "U": 66, "V": 67, "W": 68, "X": 69, "Y": 10,
        "Z": 11, "a": 12, "b": 13, "c": 14, "d": 15, "e": 16, "f": 17, "g": 18,
        "h": 19, "i": 30, "j": 31, "k": 32, "l": 33, "m": 34, "n": 35, "o": 36,
        "p": 37, "q": 38, "r": 39, "s": 90, "t": 91, "u": 92, "v": 93, "w": 94,
        "x": 95, "y": 96, "z": 97, " ": 98, ",": 99, ".": 100, "’": 101, "!": 102,
        "-": 103
}


# Reverses the dictionary we used to encode stuff
decode_map = {v: k for k, v in encoding_map.items()}
def decoding():
    with open(FILE, "r", encoding="utf-8") as f:
        file_input = f.read()
    nums = file_input.split(",")
    output = ""
    for num in nums:
        num_str = num.strip()
        if not num_str:
            continue
        try:
            num_int = int(num_str)
            if num_int in decode_map:
                output += decode_map[num_int]
            else:
                output += "?"
        except ValueError:
            output += num_str

    with open('output.txt', "w", encoding="utf-8") as f:
        f.write(output)
        logging.info("Decryption text written in output.txt")





def encoding(user_input):
    output = []
    if user_input == "":
        with open(FILE, "w", encoding="utf-8") as f:
            f.write("")
            logging.warn("Empty text written in output.txt")
            return
    for char in user_input:
        if char in encoding_map:
            output.append(str(encoding_map[char]))
        else:
            output.append(char)
    encrypted_text = ','.join(output)

    with open(FILE, "w", encoding="utf-8") as f:
        f.write(encrypted_text)
        logging.info("Encrypted text written to output.txt")


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <Decrypt/Encrypt>")
        sys.exit()
    
    #sets the file
    dec = sys.argv[1] # sets the mode
    assert dec in ("Encrypt","Decrypt"), "Invalid input (must be Encrypt or Decrypt)"
    logging.error("Invalid input")
    if dec == "Decrypt":
        try:
            decoding()
            logging.info("decoding successful")
            print("Decoded text written to output.txt")
        except FileNotFoundError:
            logging.error("File not made yet")
            print("File not made yet please encode first")
        except:
            logging.error("Unexpected error:", sys.exc_info()[0])
            print("An error has occurred.")

    if dec == "Encrypt":

        print("What would you like to encrypt?")
        user_input = input()
        encoding(user_input)
        logging.info("encoding successful")
if __name__ == "__main__":
    main()

