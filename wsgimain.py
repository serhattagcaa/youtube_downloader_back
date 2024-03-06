# # wsgi.py

# from flask import Flask, request, send_file, jsonify
# from flask_cors import CORS
# from pytube import YouTube
# import traceback

# app = Flask(__name__)
# CORS(app)

# def download_audio(url):
#     yt = YouTube(url)
#     audio = yt.streams.filter(only_audio=True).first()
    
#     audio_path = audio.download()
#     return audio_path

# @app.route('/download-audio', methods=['POST'])
# def download_audio_handler():
#     try:
#         data = request.get_json()
#         audio_url = data.get('url')
        
#         audio_path = download_audio(audio_url)
        
#         return send_file(audio_path, as_attachment=True)
#     except Exception as e:
#         # Log the exception traceback
#         traceback.print_exc()
#         app.logger.error(f"Error downloading audio: {str(e)}")
#         return jsonify(error=str(e)), 500  # Internal Server Error

from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from pytube import YouTube
import traceback
import logging

app = Flask(__name__)
CORS(app)

def download_audio(url):
    yt = YouTube(url)
    audio = yt.streams.filter(only_audio=True).first()
    
    audio_path = audio.download()
    return audio_path

def download_video(url, high_resolution=True):
    yt = YouTube(url)
    
    if high_resolution:
        video = yt.streams.get_highest_resolution()
    else:
        video = yt.streams.filter(file_extension='mp4').first()
        if not video:
            video = yt.streams.first()
    
    video_path = video.download()
    return video_path

@app.route('/download-audio', methods=['POST'])
def download_audio_handler():
    try:
        data = request.get_json()
        audio_url = data.get('url')
        
        audio_path = download_audio(audio_url)
        
        return send_file(audio_path, as_attachment=True)
    except Exception as e:
        traceback.print_exc()
        app.logger.error(f"Error downloading audio: {str(e)}")
        return jsonify(error=str(e)), 500

@app.route('/download', methods=['POST'])
def download_handler():
    try:
        data = request.get_json()
        video_url = data.get('url')
        high_resolution = data.get('high_resolution', True)
        
        video_path = download_video(video_url, high_resolution)
        
        return send_file(video_path, as_attachment=True)
    except Exception as e:
        traceback.print_exc()
        app.logger.error(f"Error downloading video: {str(e)}")
        return jsonify(error=str(e)), 500

@app.route('/get_youtube_title', methods=['POST'])
def get_youtube_title():
    try:
        data = request.get_json()
        video_url = data['video_url']
        yt = YouTube(video_url)
        video_title = yt.title
        return jsonify({'title': video_title}), 200
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
# from flask import Flask, request, send_file, jsonify
# from flask_cors import CORS
# from pytube import YouTube
# import os
# import traceback
# import logging
# from io import BytesIO

# app = Flask(__name__)
# CORS(app)

# def download_audio(url):
#     yt = YouTube(url)
#     audio = yt.streams.filter(only_audio=True).first()

#     audio_content = audio.stream_to_buffer()
#     return BytesIO(audio_content)

# def download_video(url, high_resolution=True):
#     yt = YouTube(url)
    
#     if high_resolution:
#         video = yt.streams.get_highest_resolution()
#     else:
#         video = yt.streams.filter(file_extension='mp4').first()
#         if not video:
#             video = yt.streams.first()

#     video_content = video.stream_to_buffer()
#     return BytesIO(video_content)

# @app.route('/download-audio', methods=['POST'])
# def download_audio_handler():
#     try:
#         data = request.get_json()
#         audio_url = data.get('url')
        
#         audio_buffer = download_audio(audio_url)
        
#         return send_file(audio_buffer, as_attachment=True, download_name="audio.mp3")
#     except Exception as e:
#         traceback.print_exc()
#         app.logger.error(f"Error downloading audio: {str(e)}")
#         return jsonify(error=str(e)), 500

# @app.route('/download', methods=['POST'])
# def download_handler():
#     try:
#         data = request.get_json()
#         video_url = data.get('url')
#         high_resolution = data.get('high_resolution', True)
        
#         video_buffer = download_video(video_url, high_resolution)
        
#         return send_file(video_buffer, as_attachment=True, download_name="video.mp4")
#     except Exception as e:
#         traceback.print_exc()
#         app.logger.error(f"Error downloading video: {str(e)}")
#         return jsonify(error=str(e)), 500

# if __name__ == "__main__":
#     app.run(debug=True)

