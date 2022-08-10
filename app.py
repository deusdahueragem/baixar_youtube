from nturl2path import url2pathname
from flask import Flask, render_template, redirect, request
from pytube import YouTube, streams

app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def page_home():
    if request.method =="POST":

        first_name = request.form.get("fname")
        last_name = request.form.get("lname")

        video = YouTube(first_name)
        stream = video.streams.get_highest_resolution()
        stream.download(output_path='../static')
        print ("Waiting Download")
        return "Seu nome é "+first_name + last_name
    return render_template("index.html")

if __name__ == '__main__':
    app.run()

