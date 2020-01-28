import os


downloads = "/Users/logan/Downloads"
filedest = "/Users/logan/Desktop/docs"
for file in os.listdir(downloads):
    if file.endswith(".pdf") or file.endswith(".doc") or file.endswith("docx"):
        tobemoved = downloads + "/" + file
        tobeplaced = filedest +"/"+ file
        os.rename(tobemoved,tobeplaced)


for file in os.listdr(filedest):
    if file.
print("done")

