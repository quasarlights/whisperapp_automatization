from flask import Flask, render_template, request 
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
from VideoToAudio import main
from pathlib import Path
from Transcript import Transcript

app = Flask(__name__)


@app.route('/transcript', methods =['POST'])
def transcript():
    video_file = request.files['video']
    video_file.save(video_file.filename)
    main(video_file)
    os.remove(video_file)
    return "ok"
"""
    text = Transcript.get_transcript(file_name)
    os.remove(audio_file)

    return text
"""
    

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True, port=5000)