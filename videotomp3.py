# Video to mp3 converter with moviepy package

from moviepy.editor import *

video_path = input('Enter path to video file: ')
videoclip = VideoFileClip(video_path)
audioclip = videoclip.audio
audioclip.write_audiofile('output.mp3')