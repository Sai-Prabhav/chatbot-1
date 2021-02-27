from flask import Flask, request, render_template
import random
import threading
from lib import *
from time import sleep
from chat import chatbot
def fla():
	app = Flask(  # Create a flask app
		__name__,
		template_folder='templates',  # Name of html file folder
		
	)

    print("hi")
    @app.route('/')
    def my_form():
        path = find_database_path()
        with open(path, "r") as jsonFile:
			data1 = json.load(jsonFile)
		
		return render_template('my-form.html',texss=data1["text"])
	@app.route('/', methods=['POST'])
	def my_form_post():
		text = request.form['text']
		path = find_database_path()
		with open(path, "r") as jsonFile:
			data1 = json.load(jsonFile)
		
		data=data1
		data["input"]=text
		with open(path, "w") as jsonFile:
				json.dump(data, jsonFile, indent=4)
		sleep(0.5)
		with open(path, "r") as jsonFile:
			data1 = json.load(jsonFile)
		
		return render_template('my-form.html',texss=data1["text"])

	if __name__ == "__main__":  # Makes sure this is the main process
		app.run( # Starts the site
			host='0.0.0.0',  # Establishes the host, required for repl to detect the site
			port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
		)



threading. Thread(target=fla). start()
threading. Thread(target=chatbot). start()
