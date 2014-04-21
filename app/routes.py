from flask import Flask, render_template, flash, redirect
from flask import request, make_response
from flask import url_for
#from app import app
from forms import SpecConfigForm
import time
 
app = Flask(__name__)     
app.secret_key = 'ZkLhVTTj'
 
@app.route('/')
def home():
    return "Hi"

@app.route('/about')
def about():
    return "about"

@app.route('/hello')
def hello():
    hellos = [1, 2, 3, 4]
    return render_template("hello.html", hellos=hellos)

@app.route('/config', methods=['GET', 'POST'])
def config():
    print request
    form = SpecConfigForm(request.form)
    print(request.method)
    if request.method == 'POST':
        if form.validate():
            response= make_response(render_template("spec-config-parsed.txt", form=form))
            response.headers['Content-Type'] = 'text/plain'
            return response 
        else:
            print "Hi"
            print(form.errors) 
    return render_template("spec-config.html", form = form)

 
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
