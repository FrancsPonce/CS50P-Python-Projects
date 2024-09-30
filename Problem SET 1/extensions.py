def convert():
    file_name= input("Write a file: " ).lower()
    if ".gif" in file_name:
        print("image/gif")
    elif ".jpg" in file_name or ".jpeg" in file_name:
        print("image/jpeg")
    elif ".png" in file_name:
        print("image/png")
    elif ".pdf" in file_name:
        print("application/pdf")
    elif ".txt" in file_name:
        print("text/plain")
    elif ".zip" in file_name:
        print("application/zip")
    else:
        print("application/octet-stream")
convert()
