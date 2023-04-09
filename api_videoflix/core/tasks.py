import subprocess
import shlex

# functionality to be executed inside django-rq workers


def convert_360p(source):
    target = source[:-4] + "_360p.mp4"
    cmd = shlex.split(
        f'sudo ffmpeg -i "{source}" -vf scale=-1:360 -c:v libx264 -crf 18 -preset veryslow -c:a copy "{target}"'
    )

    subprocess.run(cmd, capture_output=True)


def convert(source, number):
    target = source[:-4] + f"_{number}p.mp4"
    cmd = shlex.split(
        f'sudo ffmpeg -i "{source}" -s hd{number} -c:v libx264 -crf 23 -c:a aac -strict -2 "{target}"'
    )

    subprocess.run(cmd, capture_output=True)
