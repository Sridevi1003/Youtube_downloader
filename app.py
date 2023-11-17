from flask import Flask, url_for, render_template, redirect, send_file, request, session
from pytube import YouTube

app = Flask(__name__)
app.config['SECRET_KEY'] = "!2367@abc"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['link'] = request.form.get('url')
        url = YouTube(session['link'])
        return render_template('video.html', url=url)
    return render_template('index.html')


@app.route('/see-video', methods=['POST'])
def see_video():
    url = YouTube(session['link'])
    itag = request.form.get('itag')
    video = url.streams.get_by_itag(itag)
    filename = video.download()
    return send_file(filename, as_attachment=True)


@app.route('/see-audio', methods=['POST'])
def see_audio():
    url = YouTube(session['link'])
    audio = url.streams.filter(only_audio=True).first()
    filename = audio.download()
    return send_file(filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
