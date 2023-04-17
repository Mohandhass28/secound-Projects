from flask import Flask,request,render_template
from Path_Search_Algo import path
import maze


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
    # ma = maze.maz
    # p = path(ma).find_path()

