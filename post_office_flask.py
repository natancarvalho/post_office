from flask import Flask, render_template, request
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import post_office_lib


app = Flask(__name__)

@app.route("/")
def home_post_office():
    return render_template("main.html")

@app.route("/login", methods = ["POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
       
        
    with open('login.txt', 'r') as arquivo:
        dados_login = {}

        for linha in arquivo:
            partes = linha.strip().split(':')

            if len(partes) == 2:
                email_bd = partes[0].strip()  
                senha_bd = partes[1].strip()

                dados_login[email_bd] = senha_bd 

    if email in dados_login:
        validar_login = dados_login[email]

        if validar_login == password:
            return render_template("opcoes.html")
        
        else:
            return render_template("main.html")
        
@app.route("/opcoes", methods = ["POST"])
def opcoes():
    quebra_linha = "\n"
    if request.method == "POST":
        opcao = request.form["botao"]
        if opcao == "Enviar":
            data = request.form.get("data")
            destinatario = request.form.get("destinatario")
            mensagem = request.form.get("freeform")
            remetente = request.form.get("rementente")

            carta = "<" + data + ">" +  quebra_linha + "<" + destinatario + ">"  + quebra_linha + "<" + remetente + ">" 

            print(carta)

            post_office_lib.escrever_carta(destinatario, data, carta)   

            return render_template("opcoes.html")