import os

base_dir = "/"
mp4_file = base_dir + "audio.mp4"
mp4_file = base_dir + "audio.mp3"

cmd  = "ffmpef -i {} -vn {}".format(mp4_file, mp4_file)
os.system(cmd)
os.