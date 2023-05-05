from flask import Flask, render_template

app = Flask(__name__)

# Note that for Flask, html pages must be in folder templates, and static files are under static
@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
