from flask import Flask,render_template,redirect,request
import pickle as pkl
import pandas as pd



app = Flask(__name__)
model = pkl.load(open('model.pkl','rb'))

@app.errorhandler(404)
def error(e):
    return redirect('/')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/submit', methods=['GET', 'POST'])
def form_handler():
    if request.method == 'POST':
        # Collect form data and make a dictionary
        data = {
        'Prop': request.form.get('prop'),
        'inPlans': request.form.get('inPlans'),
        'JobType': request.form.get('jobType'),
        'foreign': request.form.get('foreign'),
        'telephone': request.form.get('telephone'),
        'Cbal': request.form.get('cbal'),
        'Chist': request.form.get('chist'),
        'Edur': request.form.get('edur'),
        'MSG': request.form.get('msg'),
        'Rdur': request.form.get('rdur'),
        'Htype': request.form.get('htype'),
        'Camt': request.form.get('camt'),
        'Cdur': request.form.get('cdur'),
        'InRate': request.form.get('inRate'),
        'age': request.form.get('age'),
        'NumCred': request.form.get('numCred'),
        'Ndepend': request.form.get('ndepend')
        }
        df = pd.DataFrame([data])
        val = model.predict(df)
        if val[0]=='good':
            return render_template('output.html',credit_granted=f"Congratulation you can get the credit")
        else:
            return render_template('output.html',credit_granted=f"Sorry Better Luck Next Time")
        

    

if __name__=="__main__":
    app.run(debug=True,port=5000)