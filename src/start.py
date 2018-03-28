#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv

from src.bottle import Bottle, run, view, route, template, post, request, response
import json
app = Bottle()

@route('/')
def index(name='docs'):
    return '''
            <title>Documentations</title>
            <h1>How to use the API</h1>
        '''

@route('/lieu')
def index(name='lieu'):
    # Open the CSV
    f = open('23440003400026_J335_installations_table.csv', 'r',encoding='utf-8')
    # Change each fieldname to the appropriate field name. I know, so difficult.
    reader = csv.DictReader(f.decode('utf_8'), fieldnames=("Nom usuel de l'installation","Numéro de l'installation","Nom de la commune","Code INSEE","Code postal","Nom du lieu dit","Numero de la voie","Nom de la voie","location","Longitude","Latitude","Aucun aménagement d'accessibilité","Accessibilité handicapés à mobilité réduite","Accessibilité handicapés sensoriels","Emprise foncière en m2","Gardiennée avec ou sans logement de gardien","Multi commune","Présence d'un internet","Nombre de couvert ","Nombre de lit","Nombre total de place de parking","Nombre total de place de parking handicapés","Installation particulière","Desserte métro","Desserte bus","Desserte Tram","Desserte train","Desserte bateau","Desserte autre","Nombre total d'équipements sportifs","Nombre total de fiches équipements","Date de création de la fiche installation","Date de mise à jour de la fiche installation"))
    # Parse the CSV into JSON
    response.content_type = 'application/json;charset=UTF-8'
    print(f)
    return json.dumps([row for row in reader])
run(host='localhost', port=8080)