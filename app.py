from flask import Flask, render_template, request, redirect
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        file.save('input.csv')
        
        # Duygu analizi betiğini çalıştırın
        subprocess.call(['python', 'duyguanalizi.py'])
        return redirect('/results')

@app.route('/results')
def show_results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True)