from flask import Flask, request, redirect, url_for, render_template
import config
from Users import User
from ShoppingList import ShoppingList
app = Flask(__name__)

app.config.from_object(config)

new_user = User()
new_list = ShoppingList()


@app.route('/')
def index():
    return 'hello'


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        content = new_user.add_user(username, password)

        print(content)

    return render_template('adduser.html', data=None)


@app.route('/deleteuser/<id>', methods=['GET'])
def deleteuser(id):
    content = new_user.deleteuser(id)
    return redirect(url_for('index'))


@app.route('/users', methods=['GET'])
def all_users():
    content = new_user.get_all_users() if new_user.get_all_users() else None

    return render_template('users.html', data=content)


@app.route('/changepass/<id>', methods=['GET', 'POST'])
def change_password(id):
    if request.method == 'POST':
        username = id
        current_pass = request.form['current_password']
        new_pass = request.form['new_password']

        content = new_user.change_password(username, current_pass, new_pass)

        print(content)
        return redirect(url_for('all_users'))

    return render_template('change_pass.html')


@app.route('/slist', methods=['GET', 'POST'])
def create_list():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']

        content = new_list.create_list(name, description)

        print(content)

    return render_template('create_list.html', data=None)


@app.route('/delete_list/<id>', methods=['GET'])
def delete_list(id):
    content = new_list.delete_list(id)
    return redirect(url_for('index'))


@app.route('/update_list/<id>', methods=['POST', 'GET'])
def update_list(id):
    if request.method == 'POST':
        name = request.form['name']
        curr_desc = request.form['curr_desc']
        new_desc = request.form['new_desc']

        content = new_list.update_list(name, curr_desc, new_desc)

        print(content)

    return render_template('update_list.html', data=None)


@app.route('/view_list', methods=['GET'])
def view_list():
    content = new_list.view_list()

    print(content)

    return render_template('lists.html', data=content)


if __name__ == "__main__":
    app.run()
