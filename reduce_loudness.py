from flask import Flask, request, send_file
from pydub import AudioSegment
import os

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 * 10  # 160 MB

@app.route('/loudness', methods=['POST'])
def reduce_loudness():
    print("((((((((((((((((((****************************here*******************)))))))))))))))))))))))))))")
    print(request.data)
    print(request.headers)
    print("((((((((((((((((((****************************here*******************)))))))))))))))))))))))))))")
    # Get the uploaded file from the POST request
    file = request.files['file']
    
    # Load the audio file using pydub
    audio = AudioSegment.from_file(file)
    
    # Reduce the loudness level by 6 dB
    quieter_audio = audio - 6
    
    # Save the reduced audio file to disk
    filename = 'quieter_audio.wav'
    quieter_audio.export(filename, format='wav')
    
    # Return the reduced audio file as a download
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(port=8080, debug=True)