import os

os.chdir('bin')

url = input("YouTube URL: ")
file = input("Download Options: A = Audio Only, B = Video & Audio: ")

while file == "A" or "B":
    if file == "A":
        os.system('cmd /k "yt-dlp --downloader aria2c -f 139 -P "..\Downloaded" "'+url)
    if file == "a":
        os.system('cmd /k "yt-dlp --downloader aria2c -f 139 -P "..\Downloaded" "'+url)
    if file == "B":
        os.system('cmd /k "yt-dlp --downloader aria2c -f bv+ba/b -P "..\Downloaded" "'+url)
    if file == "b":
        os.system('cmd /k "yt-dlp --downloader aria2c -f bv+ba/b -P "..\Downloaded" "'+url)
    else:
        print("Please enter either A or B")
        file = input("Download Options: A = Audio Only, B = Video & Audio: ")
