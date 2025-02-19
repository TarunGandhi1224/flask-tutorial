from flask import Flask,request,render_template,request
from datetime import datetime
import requests
BACKEND_URL='http://127.0.0.1:9000/'
app= Flask(__name__)
@app.route('/')
def home():
    day_of_week=datetime.today().strftime('%A')
    current_time=datetime.now().strftime('%H:%M:%S')
    return render_template('index.html',day_of_week=day_of_week,current_time=current_time)
@app.route('/submit',methods=['POST']) #1234_temp
def submit():
    form_data=dict(request.form)
    requests.post(BACKEND_URL +'/submit',json=form_data)
    return 'Data Subitted Successfully'
@app.route('/view_data')
def view_data():
    response=requests.get(BACKEND_URL +'/admin')
    return response.json()
if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)