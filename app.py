from flask import Flask, jsonify, Response, request
import funciones as fc
from http import HTTPStatus
import json
from random import choice

app = Flask(__name__)

#Rutas API
@app.route("/usuario/<usuarioUI>/contrasena/<contrasenaUI>")
def getLogin(usuarioUI,contrasenaUI):
    #Obteneniendo JSONs
    usuarios = fc.obtenerUsuarios()

    for usuario in usuarios:
        if usuario['usuario'] == usuarioUI and usuario['contrasena'] == contrasenaUI and usuarioUI != '' and contrasenaUI != '':
            return str(usuario['id'])
            
    return 'Error'

@app.route("/directores")
def getDirectores():
    #Obteneniendo JSONs
    directores = fc.obtenerDirectores()
    return jsonify(directores)

@app.route("/directores/<id>")
def getDirectoresByCodigo(id):
    #Obteneniendo JSONs
    directores = fc.obtenerDirectores()
    for director in directores:
        if director['id'] == id:
            return director
    return Response("{}", status=HTTPStatus.NOT_FOUND)

@app.route("/generos")
def getGeneros():
    #Obteneniendo JSONs
    generos = fc.obtenerGeneros()
    return jsonify(generos)
    
@app.route("/generos/<id>")
def getGenerosByCodigo(id):
    #Obteneniendo JSONs
    generos = fc.obtenerGeneros()
    for genero in generos:
        if genero['id'] == id:
            return genero
    return Response("{}", status=HTTPStatus.NOT_FOUND)

@app.route("/peliculas/director/<id>")
def getPeliculasByDirector(id):
    #Obteneniendo JSONs
    peliculas = fc.obtenerPeliculas()

    peliculasByDirector = []

    for pelicula in peliculas:
        if pelicula["idDirector"] == id:
            peliculasByDirector.append(pelicula)
    if len(peliculasByDirector)==0:
        return jsonify('Director no encontrado')
    else:
        return jsonify(peliculasByDirector)

@app.route("/peliculas/imagen")
def getPeliculasByPortada():
    #Obteneniendo JSONs
    peliculas = fc.obtenerPeliculas()

    peliculasByPortada = []
    for pelicula in peliculas:
        if pelicula["imagen"] != '':
            peliculasByPortada.append(pelicula)
    if len(peliculasByPortada)==0:
        return jsonify("Peliculas con portada no encontradas")
    else:
        return jsonify(peliculasByPortada)