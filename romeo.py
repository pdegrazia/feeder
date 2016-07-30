from flask import Flask, render_template
from flask import request, redirect, url_for

app = Flask(__name__)

fed= False
is_first_visit = True


def is_post_value_yes(request):
	return 'Yes' in request.form.to_dict().values()


@app.route('/', methods=['GET','POST'])
def index():
	if request.method == 'GET':
		return render_template('login.html')

	if request.method == 'POST':
		if request.form['submit'] == '1111':
			return redirect(url_for('romeo'))
		else:
			return render_template('login.html',error_message=True)


@app.route('/registration',methods=['POST'])
def registration():
	global is_first_visit
	if request.method == 'POST' and is_first_visit:
		print 'first visit'
		is_first_visit = False
		return render_template('registration.html')
	else:
		print 'not first visit'
		name = request.form['pet_name']
		return render_template('registration.html')


@app.route('/completed', methods=['GET'])
def completed():
	if request.method == 'GET':
		print 'COMPLETED'
		document = "<h1>Registration completed!</h1>"
		document = document + "<a href='./'>Home</a>"
		return document


@app.route('/romeo', methods=['GET','POST'])
def romeo():
	global fed
	if request.method == 'GET':
		if fed:
			return '<h1>Romeo has already been fed!</h1>'
		else:
			return render_template('template1.html')

	if request.method == 'POST':
		print 'im here'
		fed = is_post_value_yes(request)
		if fed:
			return render_template('fedromeo.html')
		else:
			return '<h1>Romeo has not been fed yet...</h1><h2>Hopefully someone will do it...</h2>'


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
