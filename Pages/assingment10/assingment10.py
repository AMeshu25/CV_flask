from flask import Blueprint, render_template, flash
from flask import Flask, redirect, url_for, session, request
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
    return render_template('assingment10.html', allUsers=allUsers)  # includs users list


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
    if request.form['favoriteColor']:
        nickname = request.form['favoriteColor']
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