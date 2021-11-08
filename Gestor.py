from Usuarios import Usuario
from reportlab.platypus import (SimpleDocTemplate, PageBreak, Image, Spacer,
Paragraph, Table, TableStyle)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
import getpass #para vobtener el nombre del user
#---------------
import random
import json
import re

class Gestor:
    def __init__(self):
        self.estadoUser=0
        self.mivector=[["Darwin Arevalo","M","admin","admin@ipc1","admin@ipc1.com"]]
        self.PosDeUserEnMiVector=0


    #inicia sesión con cuenta existente en mivector 
    def IniciarSession(self,username,contra):
        for i in range(0,len(self.mivector)): 
            for j in range(0,5): 
                #si username=username y contraseña=contraseña entonces hace esto:
                if j==2 and self.mivector[i][j]==username and self.mivector[i][j+1]==contra:
                    self.PosDeUserEnMiVector=i                  
                    return True #la cuenta existe dale acceso 
                    break
        return False #contraseña o username invalidos

    #Crear Usuario
    def CrearUsuario(self,nombre,genero,username,contra,correo):      
        for i in range(0,len(self.mivector)): #verificar si el user existe(recorre filas)
            for j in range(0,5): #recorre columnas
                if j==2 and self.mivector[i][j]==username or self.mivector[i][j]+"admin"==username or self.mivector[i][j]==username+"admin": #verifica si el user existe                  
                    return False #el dato ya existia(no se puede insertar)
                    break #me cierra el proceso porque ya existe
        # si la funcion no se quiebra es True es decir que si se puede insertar
        nuevo=[nombre,genero,username,contra,correo] #de esa forma le digo que no est tupla
        self.mivector.append(nuevo)
        return True
    
    #datos para que mostrare en una tablita
    def obtenerUserSinC(self):
        texto="[\n"
        for i in range(0,len(self.mivector)):
                texto+="{" 
                for j in range(0,5):
                    if j==0:
                        texto+="\"nombre\":\""+self.mivector[i][j]+"\","                                      
                    elif j==1:
                        texto+="\"genero\":\""+self.mivector[i][j]+"\"," 
                    elif j==2:
                        texto+="\"username\":\""+self.mivector[i][j]+"\","
                    elif j==3:
                        texto+="\"contra\":\""+self.mivector[i][j]+"\"," 
                    elif j==4:
                        texto+="\"correo\":\""+self.mivector[i][j]+"\"}," 
        texto+='{'+"\"f\":\"\"}]"
        return texto  
    
    def ExisteIDE1(self,username):
        for i in range(0,len(self.mivector)):
            for j in range(0,3):
                if username ==self.mivector[i][2]:
                    self.mivector.pop(i)
                    return True
                    break
        else:
            return False 
    
    def Genera1(self):
        from reportlab.lib.pagesizes import A4
        doc = SimpleDocTemplate("C:/Users/"+getpass.getuser()+"/Downloads/Reporte_Apps.pdf", pagesize = A4)
        story=[]
        datos = []
        for i in range(0,len(self.mivector)):
            nuevo=[self.mivector[i][0],self.mivector[i][1],self.mivector[i][2],self.mivector[i][3],self.mivector[i][4]]
            datos.append(nuevo)
        
        tabla = Table(data = datos,
        style = [
        ('GRID',(0,0),(-1,-1),0.5,colors.grey),
        ('BOX',(0,0),(-1,-1),2,colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.pink),
        ]
        )
        story.append(tabla)
        story.append(Spacer(0,15))
        doc.build(story)
        return "{\"data\":\"true\"}" 