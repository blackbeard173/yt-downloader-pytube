# Documentation: https://python-pytube.readthedocs.io/en/latest/index.html

import pytube

url = "https://youtu.be/qbW6FRbaSl0"

video = pytube.YouTube(url)

# print(video.title)
print(f'''Video Title: 
{video.title}
''')

# print(video.thumbnail_url)
print(f'''Video Thumbnail: 
{video.thumbnail_url}
''')

print("Video streams available:")
for stream in video.streams.filter(progressive=True):
    print(stream)

# video.streams.get_by_itag('22')

# The legacy streams that contain the audio and video in a single file (referred to as “progressive download”)
# are still available, but only for resolutions 720p and below.
# video.streams.filter(progressive=True).all()

# Conversely, if you only want to see the DASH streams (also referred to as “adaptive”) you can do:
# video.streams.filter(adaptive=True).all()

# Get Streams by itag
# To get a stream by a specific itag:
# video.streams.get_by_itag('22')

# Query MPEG-4 Streams
# To query only streams in the MPEG-4 format:
# video.streams.filter(file_extension='mp4').all()


final_video = video.streams.get_by_itag(18)

print("Downloading video..")

final_video.download()

print("done!")
