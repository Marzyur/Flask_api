from flask import Flask, request, render_template, send_file
from gtts import gTTS

app = Flask(__name__,template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Get text from HTML form
    text = request.form['text']

    # Set language and voice options
    lang = request.form.get('language', 'en')
    voice = request.form.get('voice', 'com')

    # Generate speech using gTTS library
    tts = gTTS(text=text, lang=lang, tld=voice)
    tts.save('output.mp3')

    # Return audio file to user
    return send_file('output.mp3', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
