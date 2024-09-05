from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Home route to render the form
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle the prediction request
@app.route('/predict', methods=['POST'])
def predict():
    # Get input from form
    years_of_experience = float(request.form['YearsOfExperience'])
    
    # Predict using the loaded model
    prediction = model.predict(np.array([[years_of_experience]]))
    
    # Return the result as JSON or rendered page
    return render_template('index.html', prediction_text=f'Estimated Salary: ${prediction[0]:.2f}')

if __name__ == "__main__":
    app.run(debug=True)
