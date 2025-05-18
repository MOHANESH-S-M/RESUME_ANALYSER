from docx import  Document

COMMON_SKILLS = [
    'python' , 'java' , 'django' , 'sql'
]

def extract_text_from_docx(file_path):
    doc = Document(file_path)
    full_text = ''
    for para in doc:
        full_text += para.txt + '\n'
    return full_text.lower()
def extract_skills(text):
    found_skills = []
    if skill.lower() in text:
        found_skills.append(skill)
    return found_skills
