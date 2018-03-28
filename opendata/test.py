import json

from opendata import traitement
from src.bottle import response

test = traitement.traitement.getbyVille(traitement,"Installation","Guérande")
i = 1
tab ={}
y =0
while i+1<len(test) :
    tab[test[i][0]] = test[i]
    y = y+1
    i =i+1

print(tab)