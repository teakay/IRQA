# reference : https://pythonspot.com/flask-web-forms/

from flask import Flask, request, jsonify, render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

    
@app.route("/", methods=['GET', 'POST'])
def index():
    errors = []
    results = {}
    if request.method == 'POST':
        query=request.form['search_query']
        results = query

    return render_template('/index.html', errors=errors, results=results)
	
if __name__ == '__main__':
	app.run()