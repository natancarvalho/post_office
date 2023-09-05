from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def home_post_office():
    return render_template("main.html")

@app.route("/login", methods = ["POST"])
def login():

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        return render_template("opcoes.html")  
        
       



               

           



        #if email == "Buda" and password =="Buda":
          
      #    return render_template("opcoes.html")
       # else:
        #  print("entrei aqui")
         # return render_template("index.html")