import subprocess
import shlex


def convert_480p(source):
    target = source[:-4] + "_480p.mp4"
    cmd = shlex.split(
        'ffmpeg -i "{}" -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(
            source, target
        )
    )

    subprocess.run(cmd, capture_output=True)
