# filename: app.py
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def api():
    # Process data from frontend and send to AutoGen agent
    data = request.json

    # Send data to AutoGen agent and get the response
    # You'll need to complete this part based on your AutoGen agent

    # Return response to frontend as JSON
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)