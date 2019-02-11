# -*- coding: utf-8 -*-
# quiz-orm/views.py

from flask import Flask
from flask import render_template, request, redirect, url_for, abort, flash
from modele import *
from forms import *

app = Flask(__name__)

@app.route('/')
def index():
    """Strona główna"""
    return render_template('index.html')
    
@app.route('/klasy')
def klasy():
    pytania = Pytanie.select()
    return render_template('klasy.html', query = pytania)

@app.route('/uczniowie')
def uczniowie():
    pytania = Pytanie.select()
    return render_template('uczniowie.html', query = pytania)
    
@app.route('/dodaj_u')
def dodaj_u():
    pytania = Pytanie.select()
    return render_template('dodaj_u.html', query = pytania)
    
@app.route('/dodaj_k', methods=['GET', 'POST'])
def dodaj_k():
    form = DodajForm()
    
    return render_template('dodaj_k.html', form=form)
