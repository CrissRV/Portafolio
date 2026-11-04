# Import
from flask import Flask, render_template,request, redirect, url_for
from pathlib import Path


app = Flask(__name__)
FEEDBACK_FILE = Path(__file__).resolve().parent / 'feedback.txt'

# Página de contenidos en ejecución
@app.route('/')
def index():
    return render_template('index.html')



# Habilidades dinámicas
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    return render_template('index.html', button_python=button_python, button_discord=button_discord, button_html=button_html, button_db=button_db)
@app.route('/feedback', methods=['POST'])
def feedback():
    feedback_text = request.form.get('text')
    email = request.form.get('email')
    # Aquí puedes procesar el feedback, guardarlo en una base de datos, enviarlo por correo, etc.
    if email and feedback_text:
        with FEEDBACK_FILE.open('a', encoding='utf-8') as f:
            f.write(f"Email: {email}\nFeedback: {feedback_text}\n\n")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
