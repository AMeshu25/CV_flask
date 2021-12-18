from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def Main_page():  # put application's code here
    return render_template('CV1.html')


@app.route('/Second_page')
def Second_page():  # put application's code here

    return render_template('CV2.html')

@app.route('/forms')
def forms_page():  # put application's code here
    return render_template('forms.html')



@app.route('/assignment8')
def something_page():  # put application's code here
    return render_template('assignment8.html', user = {'firstname': 'Amir', 'lastname':'Meshurer'},
                           hobbies = ['Not that intrensting man', 'beer'], movies =('EuroTrip','American Pie'))

if __name__ == '__main__':
    app.run()
