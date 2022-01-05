from flask import Flask, render_template, url_for, request,session,redirect
import mysql.connector
app = Flask(__name__)
# app.config.from_pyfile('settings.py')
app.secret_key='123456'
users = {'user1': {'name': 'Amir', 'email': 'AM@gmail.com', 'nickname': 'Miri', 'b-day': '25/05/1995 '},
         'user2': {'name': 'Or', 'email': 'Orda@gmail.com', 'nickname': 'Orcha', 'b-day': '20/08/1995'},
         'user3': {'name': 'Ron', 'email': 'sad@gmail.com', 'nickname': 'Ponia ', 'b-day': '14/04/1995'},
         'user4': {'name': 'Ofek', 'email': 'Ope@gmail.com','nickname': 'Puki' ,'b-day': '20/10/1996' },
         'user5': {'name': 'Shir', 'email': 'shir@gmail.com', 'nickname': 'Chir', 'b-day': '13/8/1993'} }


@app.route('/')
def Main_page():  # put application's code here
    return render_template('CV1.html')


@app.route('/Second_page')
def Second_page():  # put application's code here

    return render_template('CV2.html')

@app.route('/forms')
def forms_page():  # put application's code here
    return render_template('forms.html')

@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    if request.method == 'GET':
        # someone made a search
        if 'searchName' in request.args:
            # request.args for GET method
            search = request.args['searchName']
            # empty search - section 4
            if search == '':  # need to return all the users
                return render_template('assignment9.html', allUsers=users)
            # not empty search - section 3
            else:
                user = ' '
                for userID, userInfo in users.items():
                    if search == userInfo['name']:
                        user = userInfo
                        break
                return render_template('assignment9.html', foundUser=user)
        # no one made a search
        return render_template('assignment9.html')
    elif request.method == 'POST':
        # request.form for POST method
        if 'username' in request.form:  # at least username was enterd
            username = request.form['username']
            password = request.form['password']
            session['username'] = username
            return render_template('assignment9.html')
        return render_template('assignment9.html')

@app.route('/logout')
def logout_func():
    session['username'] = ''
    return redirect(url_for('assignment9'))

@app.route('/assignment8')
def something_page():  # put application's code here
    return render_template('assignment8.html', user = {'firstname': 'Amir', 'lastname':'Meshurer'},
                           hobbies = ['Not that intrensting man', 'beer'], movies =('EuroTrip','American Pie'))


#assignment10 blueprint
from Pages.assingment10.assingment10 import assignment10
app.register_blueprint(assignment10)


if __name__ == '__main__':
    app.run(debug=True)
