from flask import Flask
app = Flask(__name__)



@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

# /user/john
@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)

if __name__ == '__main__':
    app.run()