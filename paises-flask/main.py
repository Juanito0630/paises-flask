# importar las dependencias de Flask
from flask import Flask, render_template

# crear el objeto Flask 
app = Flask(__name__)

# crear una primera ruta de prueba
@app.route("/hola")
def hola():
    return "<h2>No pos Dinosaurio<h2>"

# ruta paises
@app.route("/paises")
def paises():
    username = "Mafe"
    continentes = [
    {
        "nombre" : "America",
        "poblacion" : 1036900576 ,
        "densidad" : '22.8 hab/km2',
        "superficie" :42549000,
        "Nopaises" : 35,
        "paises" :
        [
           {
               "nom" : "Colombia",
               "mon" : "Peso",
               "cap" : "Bogota",
               "pob" : 51.52
           },
           {
               "nom" : "Peru",
               "mon" : "Sol",
               "cap" : "Lima",
               "pob" : 33.72
           },
           {
               "nom" : "Paraguay",
               "mon" : "Guarani",
               "cap" : "Asuncion",
               "pob" : 6.704
           }
        ]
    },
    {
        "nombre" : "Europa",
        "poblacion" : 747747395,
        "densidad" : '71 hab/km2',
        "superficie" :10530751,
        "Nopaises" : 50,
        "paises" : 
        [
            {
               "nom" : "España",
               "mon" : "Euro",
               "cap" : "Madrid" ,
               "pob" :47.42
            },
            { 
               "nom" : "Francia",
               "mon" : "Euro",
               "cap" : "Paris",
               "pob" : 67.75
            }
        ]
    },
    {
        "nombre" : "Asia",
        "poblacion" : 4598168800 , 
        "densidad" : '103.2 hab/km2',
        "superficie" : 44541138,
        "Nopaises" : 51,
        "paises" : 
        [
            {
               "nom" : "Corea Del Sur",
               "mon" : "Won Surcoreano",
               "cap" : "Seul",
               "pob" : 51.74
            }
        ]
    },
    {
        "nombre" : "Africa",
        "poblacion" : 1320000000 , 
        "densidad" : '43.7 hab/km2',
        "superficie" : 30221535 ,
        "Nopaises" :54,
        "paises" : 
        [
            {
               "nom" : "Kenia",
               "mon" : "Chelin",
               "cap" : "Nairobi",
               "pob" : 53.01
            },
            {
               "nom" : "Nigeria",
               "mon" : "Franco CFA",
               "cap" : "Abuya",
               "pob" : 213.4
            },
            {  
               "nom" : "Etiopia",
               "mon" : "Birr",
               "cap" : "Adis Abeba",
               "pob" : 120.3
            },
            {
               "nom" : "Egipto",
               "mon" : "Libra Egipcia",
               "cap" : "El Cairo",
               "pob" : 109.3
            }
        ]
    }
    ]
   
    return render_template('paises.html', 
                           username=username, 
                           continentes=continentes)