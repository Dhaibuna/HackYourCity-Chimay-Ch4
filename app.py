from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    variable = request.form['variable']
    return variable


# <form method="POST">
#     <input type= "text" name="Email" placeholder="Entrer votre mail"> 
#     <input type= "text" name="Mot de passe" placeholder="Mot de passe"> 
#     <bouton>Connecter</bouton>
# </form>