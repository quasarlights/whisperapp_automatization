from moviepy.editor import *
from tkinter.filedialog import *
import os

        
    
def os_detect() :
    if os.name == 'nt':
        print('\nSaved Location:\n')
        os.system('cd')
    else :
        print('\nSaved Location:\n')
        os.system('pwd')

def video2audio(video_file):
    file = video_file
    video = VideoFileClip(file)
    video.audio.write_audiofile("audio.mp3")
    #return "Video converted to mp3"

"""    
def video2audio(videofile,audiofile):
    videoclip=VideoFileClip(videofile)
    audioclip=videoclip.audio
    audioclip.write_audiofile(audiofile)
    #audioclip.close()
    #videoclip.close()
    """
#mp4file = askopenfilename()
#mp3file = input('Save as (sample.mp3) : ')

    
#video = "Clase N°1.mp4"
#audioName= "ciao58.mp3"

def main(video):
    video2audio(video)

    #os_detect() 

    


#main(video, audioName)