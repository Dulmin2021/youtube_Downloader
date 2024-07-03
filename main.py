from pytube import Playlist,YouTube

playlist_url = input("Playlist URL: ")

pl = Playlist(playlist_url)
# pl.playlist_url()

i=0
for video_url in pl.video_urls:
    i= i+1
    yt = YouTube(video_url)
    video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc() .first()
    print("Starting...")
    video.download(f"Videos/ {yt.author}")
    print(f"Done !! {i}  / {len(pl.video_urls)} ",  )

print('ALL DONE')

