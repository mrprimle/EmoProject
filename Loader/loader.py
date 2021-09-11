import ffmpeg
import os

class Loader():
    """
    Custom loader for the video stream
    """
    def __init__(self, dir, name):
        """
        The loader for stream handling
        Input: 
            dir: str directory name
            name: str file name
        """
        
        self.dir = dir
        self.name = name

        if os.path.exists(dir+name):
            self.stream = ffmpeg.input(dir+name)
        else: 
            return Exception
    
    
    def get_video(self, start, end):
        """
        Get the raw video
        Input:
            start: float
            end: float 
        """
        self.video = self.stream.video
        return self.video
    
    def get_audio(self, start, end):
        """
        Get audio from video
        Input:
            start: float
            end: float 
        """
        self.audio = self.stream.audio
        audio =  self.filter('atrim', start=start, end=end)
        return ffmpeg.output(audio, "mp3").run()



