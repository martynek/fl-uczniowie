# -*- coding: utf-8 -*-
# quiz-orm/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, HiddenField, FieldList
from wtforms import SelectField, FormField, BooleanField
from wtforms.validators import Required

blad1 = 'To pole jest wymagane'

class KlasaForm():
    id = HiddenField()
    klasa = StringField('Klasa:')
    rok_naboru = StringField('Rok naboru:')
    rok_matury = StringField('Rok matury:')
    
class DodajForm(FlaskForm):
    id = HiddenField('Pytanie id')
    imie = StringField('Imie:',
                          validators=[Required(message=blad1)])
    nazwisko = StringField('Nazwisko',
                          validators=[Required(message=blad1)])
    klasa= SelectField('Kategoria', coerce=int)


    
