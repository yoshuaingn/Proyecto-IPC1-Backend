#Importaciones de Flask

from flask import Flask,request,jsonify
from flask_cors import CORS, cross_origin
from Gestor import Gestor
import re
#Crear la app

gestor = Gestor()
posicicion= gestor.PosDeUserEnMiVector

app = Flask(__name__)
app.config["DEBUG"] = True

CORS(app)

# EndPoints

@app.route('/',methods=['GET'])
def home():
    return 'SERVER IS WORKING!!!!'

#CrearUsario
@app.route('/registrar',methods=['POST']) 
#mandar un mensaje que diga exito al crear un usuario
def insertar():
    data= request.json
    contraseña=data['contra']
    if len(contraseña)>8:
          if re.search('[°!"#$%&]', contraseña):
                if any(chr.isdigit() for chr in contraseña):
                      if gestor.CrearUsuario(data['nombre'],data['genero'],data['username'],data['contra'],data['correo']):
                            return "{\"data\":\"true\"}"
                      else:
                            return "{\"data\":\"false\"}"
                else:
                      return "{\"data\":\"contrano1\"}"
          else:
                return "{\"data\":\"contrano2\"}"
    else:
          return "{\"data\":\"contrano3\"}"        


#iniciar sesion
@app.route('/login',methods=['POST'])
def iniciarsesion():
    userrr=request.json
    if (userrr['username']=="admin" and userrr['contra']=="admin@ipc1"):
        gestor.PosDeUserEnMiVector=0
    if (userrr['username']=="admin" and userrr['contra']=="admin@ipc1"):
        return "{\"data\":\"admin\"}"
    elif gestor.IniciarSession(userrr['username'],userrr['contra']):
        return "{\"data\":\"true\"}"        
    else:
        return "{\"data\":\"false\"}"  

@app.route('/estadoApp1')
def estadoapp1():
    if gestor.estadoUser==1: #ya se hizo la carga masiva de usuarios
        return "{\"data\":\"true\"}"
    else:
        return "{\"data\":\"false\"}" 

#Obtener todos los usuarios(nombre,appelido,username)
@app.route('/verTablita')
def TablaUsers():
    return gestor.obtenerUserSinC()  

#elimna user
@app.route('/idappE1', methods=['POST']) #elimina app
def elimanaapp1():
    modificarappE1=request.json    
    if gestor.ExisteIDE1(modificarappE1['username']):
        return "{\"data\":\"true\"}"
    else:
        return "{\"data\":\"false\"}"

#genera el pdf Users
@app.route('/pdf1', methods=['POST','GET'])
def GeneraPDF1():
    return gestor.Genera1()

       
          
#INICIAR EL SERVIDOR

if __name__ == "__main__":
    app.run(port=5000)