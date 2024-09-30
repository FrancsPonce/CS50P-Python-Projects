####
import emoji

def main():
    input_user= input("Input: ")
    print(emoji.emojize(f"Output: {input_user}", language='alias'))

main()
