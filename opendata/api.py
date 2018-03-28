#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv

import itertools

from opendata import traitement
from src.bottle import Bottle, run, view, route, template, post, request, response
import json
app = Bottle()

@route('/')
def index(name='docs'):
    return '''
            <title>Documentations</title>
            <h1>How to use the API</h1>
        '''

@route('/<db>/<city>')
def search(db ,city):
    test = traitement.traitement.getbyVille(traitement,db,city)
    response.content_type = 'application/json;charset=UTF-8'
    tab={}
    i =0
    while i + 1 < len(test):
        tab[test[i][0]] = test[i]
        i = i + 1
    return json.dumps(tab)
run(host='localhost', port=8080)