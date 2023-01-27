from flask import Flask, render_template, request 
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
from VideoToAudio import main, deleteAudio
from pathlib import Path
from Transcript import Transcript

app = Flask(__name__)


@app.route('/transcript', methods =['POST'])
def transcript():
    video_file = request.files['video']
    video_file.save(video_file.filename)
    file_name = secure_filename(video_file.filename)
        
    if file_name:
        main(file_name)
        os.remove(file_name)
        audio_name = "audio.mp3"
        text = Transcript.get_transcript(audio_name)
        return text, deleteAudio(audio= audio_name)
    else:
        return "ko"
    
    

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True, port=5000)