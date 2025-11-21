from flask import Flask, render_template, request
from src.preprocessing import preprocess_data, detect_ponzi

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    initial_investment = float(request.form['initial_investment'])
    monthly_return = float(request.form['monthly_return'])
    duration_months = int(request.form['duration_months'])
    
    data = preprocess_data(initial_investment, monthly_return, duration_months)
    result = detect_ponzi(data)
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
