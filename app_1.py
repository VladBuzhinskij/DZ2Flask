from flask import Flask, render_template,make_response,request

app=Flask(__name__)

@app.route('/')
def index():
    context={
        'registration':"0"
    }
    return render_template('index.html',**context)

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.get('/registration')
def registartion():
    
    return render_template('registration.html')

@app.post('/submit')
def registration_post():
    context={
        'registration': 1
    }
    name=request.form.get('name')
    email=request.form.get('email')
    response=make_response(render_template('index.html',**context))
    response.set_cookie('username',name)
    response.set_cookie('email',email)
    return response

@app.route('/exit')
def exit():
    context={
        'registration': 0
    }
    response=make_response(render_template('index.html',**context))
    response.set_cookie('username', '', expires=0)
    response.set_cookie('email', '', expires=0)
    return response

if __name__ == '__main__':
    app.run