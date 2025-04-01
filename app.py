from flask import Flask, render_template, request
import pickle
from datetime import datetime

app = Flask(__name__)

# Load the trained model (replace 'Goldmodel.pkl' with your actual model path)
with open('Goldmodel.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        date = request.form['date']
        currency = request.form['currency']
        
        # Simulate prediction (replace with actual model logic)
        # In a real app, preprocess the date/currency and call model.predict()
        prediction = {
            'date': date,
            'currency': currency,
            'price': "123396.11"  # Example value (replace with model output)
        }
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)