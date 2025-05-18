from flask import Flask,render_template,request , redirect ,url_for,session
from resume_parser import extract_text_from_docx,extract_skills
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

        text = extract_text_from_docx(resume_path)
        skills = extract_skills(text)
        return render_template("results.html", text=text, skills=skills)
        
    return render_template('index.html')
@app.route("/home")
def home():
    return redirect(url_for('/'))
@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)

