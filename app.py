from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def main():
    return "This is the Home Page"


@app.route('/admin/<name>')
def admin(name):
    if name == "Godwin":
        return "Welcome %s, Please Log In to the Admin Page" % name
    elif name == "Jeandre":
        return redirect(url_for('user', name=name))
    else:
        return redirect(url_for('guest', name=name))


@app.route('/guest/<name>')
def guest(name):
    return "Welcome %s, this is the guest page" % name


@app.route('/user/<name>')
def user(name):
    return "Welcome %s, this is the user login" % name


if __name__ == '__main__':
    app.debug = True
    app.run()
