file = input("File name: ").strip().lower()

if file[-5:] == ".jpeg":
    print("image/jpeg")
else:
    match file[-4:]:
        case ".gif":
            print("image/gif")
        case ".jpg":
            print("image/jpeg")
        case ".png":
            print("image/png")
        case ".pdf":
            print("application/pdf")
        case ".txt":
            print("text/plain")
        case ".zip":
            print("application/zip")
        case _:
            print("application/octet-stream")

