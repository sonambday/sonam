from flask import Flask, render_template

app = Flask(__name__)

# Route for the landing page
@app.route('/')
def home():
    return render_template('index.html')  # Renders templates/index.html

if __name__ == '__main__':
    app.run(debug=True)
