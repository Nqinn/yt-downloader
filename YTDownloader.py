from pytube import YouTube

# Asking user to insert the link
link = input("Enter the youtube url: ")
yt = YouTube(link)

#Show the video details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length,"seconds")
print("Ratings: ",yt.rating)
#Showing MP4 options only
videos = yt.streams.filter(progressive=True)
video  =list(enumerate(videos))

for i in video:
    print(i)

print("Enter the desired options to download the format!")
dn_option = int(input("Enter the option: "))
dn_video = videos[dn_option]
dn_video.download()

#Starting Download
print ("Downloading...")
print("Your video has been downloaded :D")
