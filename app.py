from flask import Flask, request, render_template, send_file
import subprocess, os, uuid

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['video']
        if file:
            input_path = os.path.join(UPLOAD_FOLDER, f'{uuid.uuid4()}.mp4')
            output_path = os.path.join(UPLOAD_FOLDER, f'{uuid.uuid4()}_4x.mp4')
            file.save(input_path)
            subprocess.run([
                'ffmpeg', '-i', input_path,
                '-filter_complex', '[0:v]setpts=0.25*PTS[v];[0:a]atempo=2.0,atempo=2.0[a]',
                '-map', '[v]', '-map', '[a]', '-y', output_path
            ], check=True)
            return send_file(output_path, as_attachment=True)
    return render_template('index.html')
