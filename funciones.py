import json

#Leer JSONs
with open ('jsons/usuarios.json','r',encoding="utf8") as archivoJson:
    usuarios = json.load(archivoJson)

with open ('jsons/peliculas.json','r',encoding="utf8") as archivoJson:
    peliculas = json.load(archivoJson)

with open ('jsons/directores.json','r',encoding="utf8") as archivoJson:
    directores = json.load(archivoJson)

with open ('jsons/generos.json','r',encoding="utf8") as archivoJson:
    generos = json.load(archivoJson)

with open ('jsons/comentarios.json','r',encoding="utf8") as archivoJson:
    comentarios = json.load(archivoJson)