import sys
from PIL import Image, ImageOps
from os.path import splitext

def main():
    check_sys()

    try:
        image_open= Image.open(sys.argv[1])

    except FileNotFoundError:
        sys.exit("Input does not exist")

    file_polera= Image.open("shirt.png")
    tamano= file_polera.size
    tamano_convert= ImageOps.fit(image_open, tamano)
    tamano_convert.paste(file_polera, file_polera)
    tamano_convert.save(sys.argv[2])

def check_sys():

    if len(sys.argv) <3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) >3:
        sys.exit("Too many command-line arguments")

    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])

    if file1 in [".jpg", ".jpeg", ".png"] == False:
        sys.exit("Invalid input")

    if file2 in [".jpg", ".jpeg", ".png"] == False:
        sys.exit("Invalid output")

    if file1[1].lower() != file2[1].lower():
        sys.exit("Input and output have different extensions")



if __name__ == "__main__":
    main()
