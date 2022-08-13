from nturl2path import url2pathname
from flask import Flask, render_template, redirect, request
from pytube import YouTube, streams

app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])

def page_home():
    if request.method =="POST":
        link_video = request.form.get("l_video")
        video = YouTube(link_video)
        stream = video.streams.get_highest_resolution()
        stream.download(output_path='./video')
        print ("Waiting Download")
        return render_template("video_download.html")
    return render_template("index.html")

if __name__ == '__main__':
    app.run()