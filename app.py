import os
from flask import Flask, render_template ,request,redirect
from SudokuMain import main

UPLOAD_FOLDER  = os.path.dirname(__file__) + '\input'

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)

 
def allowed_file(filename): 
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS 

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/var',methods=['POST'])
def var():
    # data = request.form.get('imp')
    print(request.files)
    file = request.files['mainImage'] 
    # if user does not select file, browser also 
    # submit an empty part without filename 
    if file.filename == '': 
        return redirect('/home') 
    if file and allowed_file(file.filename): 
        filename = 'Input.png'
        file.save(os.path.join(UPLOAD_FOLDER, filename)) 
    url=main()

    return render_template('var.html', a=url)



if __name__ == '__main__':
    app.run(debug = True)
