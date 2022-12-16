from flask import Flask, render_template 

app = Flask(__name__, template_folder='template', static_folder='static')

@app.route('/remove', methods=["GET", "POST"])
def removeowner():

    return render_template("removeowner.html")

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=8086, ssl_context='adhoc')
