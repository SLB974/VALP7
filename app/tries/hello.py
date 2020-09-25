#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('try_index_form.html')

@app.route('/resultat',methods = ['POST'])
def resultat():
  result = request.form
  n = result['nom']
  p = result['prenom']
  return render_template("try_resultat.html", nom=n, prenom=p)

@app.route('/ajax', methods = ['GET','POST'])
def ajax():
  return render_template('try_button_ajax.html')

app.run(debug=True)
			