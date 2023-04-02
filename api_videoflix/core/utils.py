from django.conf import settings
from pathlib import Path

MEDIA_ROOT = settings.MEDIA_ROOT


def getPathsToEncodedFiles(file_url):
    encodingList = [
        "_360p.mp4",
        "_480p.mp4",
        "_720p.mp4",
        "_1080p.mp4",
    ]

    # inner mapFn
    def mapToEncoding(ending):
        return file_url[:-4] + ending

    myMapped = list(map(mapToEncoding, encodingList))
    return myMapped


def combineToAbsolutePath(relativePath):
    return MEDIA_ROOT + "/" + relativePath


def deleteVideoFiles(video_file):
    relativePaths = getPathsToEncodedFiles(video_file.name)

    absolutePaths = list(map(combineToAbsolutePath, relativePaths))

    for path in absolutePaths:
        p = Path(path)
        try:
            p.unlink()
        except:
            print(
                f"Error on delete encoded file, probably no file exists, Path: {path}"
            )

    # delete original file
    try:
        video_file.delete(save=False)
    except:
        print(
            f"Error on delete original file, probably no file exists, Path: {video_file.name}"
        )
