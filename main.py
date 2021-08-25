from flask import Flask, redirect, url_for, request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def render_static():
    return render_template('/index.html')

@app.route('/index.html')
def render_static2():
    return render_template('/index.html')

@app.route('/achat.html')
def render_static3():
    return render_template('/achat.html')

@app.route('/liste-produits.html')
def render_static4():
    return render_template('/liste-produits.html')

@app.route('/liste-magasins.html')
def render_static5():
    return render_template('/liste-magasins.html')


@app.route('/profil.html')
def render_static6():
    return render_template('/profil.html')

@app.route('/nouvel-achat.html', methods = ['POST'])
def render_static7():
    return render_template('/nouvel-achat.html')

@app.route('/ajouter-produit.html', methods = ['POST'])
def render_static8():
    return render_template('/ajouter-produit.html')

@app.route('/ajouter-produit-done.html', methods = ['POST'])
def render_static9():
    return render_template('/ajouter-produit-done.html')

@app.route('/ajouter-magasin.html', methods = ['POST'])
def render_static13():
    return render_template('/ajouter-magasin.html')


@app.route('/ajouter-magasin-done.html', methods = ['POST'])
def render_static10():
    return render_template('/ajouter-magasin-done.html')

@app.route('/nouveau-profil-done.html', methods = ['POST'])
def render_static11():
    return render_template('/nouveau-profil-done.html')

@app.route('/nouvel-achat-done.html', methods = ['POST'])
def render_static12():
    return render_template('/nouvel-achat-done.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
   app.run(debug = True)