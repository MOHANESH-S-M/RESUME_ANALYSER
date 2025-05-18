from flask import Flask,render_template,request

import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'
UPLOAD_FOLDER = 'uploads'


@app.route('/',methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        resume = request.files['resume']
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        resume_path = os.path.join(app.config['UPLOAD_FOLDER'],resume.filename)
        

        resume.save(resume_path)

        return "Resume Uploaded Successfully"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

