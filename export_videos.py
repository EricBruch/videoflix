from core.admin import VideoResource

dataset = VideoResource().export()
f = open("exported_videos.json", "w")
f.write(dataset.json)
f.close()

exit()
