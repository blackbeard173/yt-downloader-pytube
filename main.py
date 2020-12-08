import pytube

video_list = []

print("Enter the url of video(To terminate use 'STOP'):")
while True:
    url = input("")

    if url == 'STOP':
        break

    video_list.append(url)

for number, video in enumerate(video_list, 1):

    v = pytube.YouTube(video)

    print(f'Video Title: \n'
          f'{v.title}\n')

    print(f'Video length in seconds: \n'
          f'{v.length}\n')

    print("Video streams available:")
    for stream in v.streams.filter(progressive=True):
        print(stream)

    print("\n")

    res = str(input('Enter the download resolution of video(example : "360p","720p","1080p"):\n'))

    final_video = v.streams.get_by_resolution(res)

    print(f"Downloading video {number}({v.title})...")

    final_video.download()

    print("done!")
