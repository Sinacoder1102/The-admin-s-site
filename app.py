from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/users/<username>')
def ask(username):
    if username == "admin":
        return render_template('adminpage.html')
    else:
        return 'sorry! This site is for admins'

@app.route('/users')
def route_for_user():
    return """<h1>This isn't the main page !
    please enter your name like this:
    http://localhost:5000/users/yourname"""    


if __name__ == "__main__":
    app.run(host='localhost',debug=True)