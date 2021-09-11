
import ffmpeg
import os

dir_name = "./Test/"
name = "test.mp4"
start = 0
end = 10

stream = ffmpeg.input(dir_name+name)
audio = stream.audio
audio.filter('atrim', start=start, end=end).output(filename="audiofile.wav", format="wav").run()

