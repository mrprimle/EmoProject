import ffmpeg
import os

class Loader():
    """
    Custom loader for the video stream
    """
    
    def __init__(self, dir, name):
        """
        """
        self.dir = dir
        self.name = name
        self.stream = ffmpeg.input(dir+name)

        
    def get_video(self):
        """
        Get the raw video
        Input:
            start: float
            end: float 
        """
        start=0
        for x in iter(int, 1):
            video =  self.stream.video.filter('atrim', start=start, end=start+10)
            start+=10
            yield audio.output(filename="videofile_{0}.mp4".format(start/10), format="wav").run()
    
    
    def get_audio(self):
        """
        Get audio from video
        Input:
            start: float
            end: float 
        """
        start=0
        for x in iter(int, 1):
            audio =  self.stream.audio.filter('atrim', start=start, end=start+10)                                 
            start+10
            yield audio.output(filename="audiofile_{0}.wav".format(start/10), format="wav").run()

    


