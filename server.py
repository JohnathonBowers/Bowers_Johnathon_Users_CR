from flask import Flask, render_template, request, redirect

from user import User

app = Flask(__name__)
@app.route('/users')
def users():
    print("Showing New User Form")
    return render_template("users_new.html")

@app.route('/users/input', methods=['POST'])
def input():
    print("Got Post Info")
    User.save(request.form)
    print(request.form)
    return redirect('/users/new')

@app.route('/users/new')
def new():
    users = User.get_all()
    print(users)
    return render_template("users.html", users=users)

if __name__ == "__main__":
    app.run(debug=True, port=5001)