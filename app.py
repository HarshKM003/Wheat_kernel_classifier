from flask import Flask,render_template,request
import pickle
import numpy as np

model = pickle.load(open('C:/Users/HP/Desktop/wheat_3/Saved_model/model.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def wheatkernel_predictor():
    print('hello user')
    Area = float(request.form.get('Area'))
    Perimeter = float(request.form.get('Perimeter'))
    Compactness = float(request.form.get('Compactness'))
    Length = float(request.form.get('Length'))
    Width = float(request.form.get('Width'))
    Asymmetry_Coefficient= float(request.form.get('Asymmetry Coefficient'))
    Length_of_kernel_groove = float(request.form.get('Length of kernel Groove'))

    result = model.predict(np.array([Area,Perimeter,Compactness,Length,Width,Asymmetry_Coefficient,Length_of_kernel_groove]).reshape(1,7))


    if result[0] == 1:
        result = 'This is Kama'
    if result[0] == 2:
        result = 'This is Rosa'
    if result[0] == 3:
        result = 'This is Cananda '


    return render_template('index.html',result=result)


if __name__ == '__main__':
   app.run(debug=True)