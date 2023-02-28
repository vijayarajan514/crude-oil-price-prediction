import numpy as np
from flask import Flask,render_template,request
from tensorflow.keras.models import load_model

app=Flask(__name__)
model = load_model('E:\Final Deliverables\Crude Oil Price Prediction\Flask\crude_oil.hs')
@app.route('/index.html')
def home():
    return render_template("index.html")
@app.route('/web.html')
def home1():
    return render_template("web.html")
@app.route('/',methods = ["POST"])
def login():
    x_input=str(request.form['year'])
    x_input=x_input.split(',')
    print(x_input)
    for i in range (0, len(x_input)):
        x_input[i]=float(x_input[i])
    print(x_input)
    x_input=np.array(x_input).reshape(1,-1)
    temp_input=list(x_input)
    temp_input=temp_input[0].tolist()
    lst_output=[]
    n_steps=10
    i=0
    while(i<1):
        if (len(temp_input)>10):
            x_input=np.array(temp_input[1:])
            print("{}day input {}".format(i,x_input))
            x_input=x_input.reshape(1,-1)
            x_input=x_input.reshape((1,n_steps,1))
            yhat=model.predict(x_input,verbose=0)
            print("{}day output {}".format(i,yhat))
            temp_input.extend(yhat[0].tolist())
            temp_input=temp_input[1:]
            lst_output.extend(yhat.tolist())
            i=i+1
        else:
            x_input=x_input.reshape((1,n_steps,1))
            yhat=model.predict(x_input,verbose=0)
            print(yhat[0])
            temp_input.extend(yhat[0].tolist())
            print(len(temp_input))
            lst_output.extend(yhat.tolist())
            i=i+1
    
    print(lst_output)

    
    return render_template("web.html",showcase = 'The new day predicted value is :'+str(lst_output))

if __name__ == '__main__':
    app.run(debug = True,port = 5000)