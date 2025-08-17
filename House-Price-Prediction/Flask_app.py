from flask import Flask,request,render_template

from Model import regressor_model

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def House():
    if request.method == 'GET':
        return render_template('House.html')
    elif request.method == 'POST':
        s = float(request.form['Size_sqft'])
        b = int(request.form['Bedrooms'])
        a = int(request.form['Age_years'])
        op= regressor_model.predict([[s, b, a]])
        Y_pred = round(op[0],2)
        return render_template('Output.html', Predicted_sales =Y_pred)

if __name__ == '__main__':
    app.run(debug=True)