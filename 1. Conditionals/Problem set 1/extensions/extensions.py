e = input("File name: ").casefold().strip()
if e.endswith(".gif"):
    print("image/gif")
elif e.endswith(".jpg"):
    print("image/jpeg")
elif e.endswith(".jpeg"):
    print("image/jpeg")
elif e.endswith(".png"):
    print("image/png")
elif e.endswith(".pdf"):
    print("application/pdf")
elif e.endswith(".txt"):
    print("text/plain")
elif e.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")