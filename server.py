from flask import Flask,render_template

app = Flask(__name__)

app.secret_key='pray cuz.'


@app.route('/')
def index():
    if 'count' not in session:
        session['counter']= 0
    
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)