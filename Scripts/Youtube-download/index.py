from pytube import YouTube
import os

user = os.getlogin()

check = os.path.exists(f"/home/{user}/youtube_download")


if check:
    pass
else:
    os.mkdir(f"/home/{user}/youtube_download")
    

os.system("clear")

print("-------- Youtube download --------")
print()

urls = input("Enter youtube video url to download: ")

video = YouTube(f"{urls}")

print("Title video:", video.title)
print(f"Length: {video.length /60:.2f} minutes")
print("Author:", video.author)
if video.views < 1000:
    print("View:", video.views)
elif video.views > 1000 and video.views < 1000000:
    print(f"View: {video.views}K")
elif video.views > 1000000:
    print(f"View: {video.views:.2f}M")
print("Date:",video.publish_date)


quality = input("(1)Hight quality" + " (2)Low quality" + " (3)Audio: " )

match quality:
    case "1":
        video.streams.get_highest_resolution().download(f"/home/{user}/youtube_download")
        print(f"Video in /home/{user}/youtube_download")
    case "2":
        video.streams.get_lowest_resolution().download(f"/home/{user}/youtube_download")
        print(f"Video in /home/{user}/youtube_download")
    case "3":
        video.streams.get_audio_only().download(f"/home/{user}/youtube_download")
        print(f"Audio in /home/{user}/youtube_download")