#aparna
import pytube
from pytube import YouTube
video_url = input("Enter URL of video to be Downloaded: ")
try:
	youtube = pytube.YouTube(video_url)
except:
	print("Connection Error")
video = youtube.streams.first()
try:
	video.download('./')
except:
	print("Some Error occured!!")
print("Video downloaded sucessfully")
