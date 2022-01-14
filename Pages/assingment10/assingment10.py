from flask import Blueprint, render_template, flash, jsonify
from flask import Flask, redirect, url_for, session, request
import requests
from interactDB import interact_db

# assignment10
global updateUser
updateUser = ''
# blueprint definition
assignment10 = Blueprint('assingment10', __name__,
                         static_folder='static',
                         static_url_path='/assingment10',
                         template_folder='templates')

# Routes
@assignment10.route('/assignment10')
def assignment10func():
    query = 'select * from users;'

    allUsers = interact_db(query=query, query_type='fetch')  # users list
    return render_template('assingment10.html', allUsers=allUsers, updateUser=updateUser)  # includs users list



@assignment10.route('/insertUser', methods=['post'])
def insertUserFunc():
    # get the data
    name = request.form['name']
    if request.form['email']:
        email = request.form['email']
    else:
        email = ''
    if request.form['b_day']:
        b_day = request.form['b_day']
    else:
        b_day = '1990-02-05'
    if request.form['nickname']:
        nickname = request.form['nickname']
    else:
        nickname = ''
    # insert to DB
    query = "insert into users (name, email, b_day, nickname) values ('%s','%s','%s','%s')" % (
        name, email, b_day, nickname)
    interact_db(query=query, query_type='commit')
    flash("%s's user created successfully!" % name)
    # return to assignment10
    return redirect('/assignment10')


@assignment10.route('/deleteUser', methods=['post'])
def deleteUserFunc():
    user = request.form['id']
    username = interact_db("select * from users where id = '%s'" % user, 'fetch')[0].name
    query = "delete from users where id = '%s';" % user
    interact_db(query, 'commit')
    flash("%s's user deleted successfully" % username)
    return redirect('/assignment10')


@assignment10.route('/updateUser', methods=['get', 'post'])
def updateUserFunc():
    user = request.form['id']
    query = "select * from users where id = '%s';" % user
    global updateUser
    updateUser = interact_db(query, 'fetch')[0]
    return redirect('/assignment10')


@assignment10.route('/doneUpdate', methods=['post'])
def doneUpdateFunc():
    global updateUser
    updateUser = ''
    id = request.form['id']
    name = request.form['name']
    email = request.form['email']
    b_day = request.form['b_day']
    nickname = request.form['nickname']
    query = "update users set name = '%s', email = '%s', b_day = '%s', nickname = '%s' where id = '%s';" % (
        name, email, b_day, nickname, id)
    interact_db(query, 'commit')
    flash("%s's user updated successfully" % name)
    return redirect('/assignment10')


@assignment10.route('/assignment11/users')
def Assignment11():  # put application's code here
    query = ' select * from users;'
    users = interact_db(query=query, query_type='fetch')
    response = jsonify(users)
    return response
    # return render_template('assignment11.html',allUser_dict = allUser_json)

def get_user(num):
    res = requests.get(f'https://reqres.in/api/users/{num}')
    res = res.json()
    return res

@assignment10.route('/assignment11/outer_source')
def assignment11_outer_source_func():
    num = 1
    if "number_backend" in request.args:
        num = int(request.args['number_backend'])
        user = get_user(num)
        return render_template('assignment11.html', User=user)
    return render_template('assignment11.html')


@assignment10.route('/assignment12/restapi_users', defaults={'user_id': 1})
@assignment10.route('/assignment12/restapi_users/<int:user_id>')
def get_users_func(user_id):
    query = 'select * from users where id=%s;' % user_id
    users = interact_db(query=query, query_type='fetch')
    if len(users) == 0:
        return_dict = {
            'status': 'Error!!!!!!',
            'message': 'user was not found try different id'
        }
    else:
        return_dict = {
            'status': 'Found the guy',
            'id': users[0].id,
            'name': users[0].name,
            'email': users[0].email,
            'b_day': users[0].b_day,
            'nickname': users[0].nickname,
        }
    return jsonify(return_dict)
