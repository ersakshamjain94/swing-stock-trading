from flask import Flask , render_template, request ,send_file
from werkzeug.utils import secure_filename
from filter_csv import *
app = Flask(__name__) 
  
@app.route("/") 
def home_view(): 
        return render_template('upload.html')
@app.route('/uploader', methods = ['GET', 'POST'])
def process_csv():
    if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename('master.csv'))
      output = filter_bymarket()
      return send_file(output, attachment_filename='consolidated.xlsx', as_attachment=True)