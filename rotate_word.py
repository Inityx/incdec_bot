#!/usr/bin/python3

import sys

def rotate_word(word):
    ret_str = ""
    for _char in word:
        ret_str += " ".join(word) + "\n"
        word = word[1:] + word[:1]
    return ret_str

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Usage: rotate str [str, ...]")

    for arg in sys.argv[1:]:
        print(rotate_word(arg))
