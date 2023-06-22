from pytube import YouTube

link = input("Enter the link of the video : ")
yt = YouTube(link)

print("Title: ", yt.title)
print("Views: ", yt.views)
video = yt.streams.get_highest_resolution()
if video is not None:
    video.download()
print(f"{yt.title} downloaded successfully.")
