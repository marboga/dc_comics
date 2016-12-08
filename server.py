from flask import Flask, redirect, render_template, request, session, flash

app = Flask(__name__)
app.secret_key = "alsjglq3secretkug52klkey34gykl3ywfg"


superheroes = [
	{'name': 'bruce wayne',
	'abilities': ['money', 'cool suit', 'Alfred'],
	'hero_name': 'batman',
	'nemesis': 'the joker'
	},
	{'name': 'clark kent',
	'abilities':
	['laser vision', 'flight', 'speed', 'strength', 'invincibility'],
	'hero_name': 'superman',
	'nemesis': 7
	}
]

@app.route('/')
def index():
	print superheroes
	#cool server logic
	#retrieves all the comic characters
	session['name'] = 'Michael'
	return render_template('index.html', hero_list=superheroes)

@app.route('/new_hero_route', methods=["POST"])
def new_hero():
	#print form values
	print request.form
	temp_dict = {}
	for key, value in request.form.items():
		print key, value, "<----------whoa\n"
		temp_dict[key] = value
	errors = []
	if len(request.form['hero_name']) < 2:
		errors.append("name too short")
	if len(request.form['nemesis']) < 2:
		errors.append("nemesis too short")

	if errors:
		for error in errors:
			flash(error)

		for key, value in request.form.items():
			session[key] = value
			print session[key], session
		return redirect('/')

	else:
		print temp_dict
		session['newest_hero'] = temp_dict
		superheroes.append(temp_dict)

		return redirect('/')






app.run(debug=True)
