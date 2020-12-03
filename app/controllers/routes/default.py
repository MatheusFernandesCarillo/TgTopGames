from app import app
from flask import render_template,redirect,url_for,flash
from app.models.formularios import NovoContato,loginForm
from app.models.contato import Contato


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/jogado2020")
def jogado2020():
    return render_template("jogado2020.html")

@app.route("/cyberpunk")
def cyberpunk():
    return render_template("cyberpunk.html")

@app.route("/lancamentos")
def lançamentos():
    return render_template("lançamentos.html")



@app.route("/adm",methods=["GET","POST"])
def adm():
    form  = loginForm()
    logado = False
    if form.validate_on_submit():
        if form.senha.data == "admin123":
            logado = True

    messages = Contato.query.all()
    return render_template("adm.html",form = form,logado=logado,messages = messages)


@app.route("/contato",methods=["GET","POST"])
def contato():
    form = NovoContato()
    if form.validate_on_submit():
        contato = form.create()
        contato.save()
        form.nome.data = ""
        form.email.data = ""
        form.mensagem.data = ""
        flash("Sua mensagem foi encaminhada com sucesso! em breve entraremos em contato!","success")

    return render_template("contato.html",form = form)


@app.route("/jogos")
def jogos():
    return render_template("jogos.html")

@app.route("/pc")
def pc():
    return render_template("pc.html")

@app.route("/ps3")
def ps3():
    return render_template("ps3.html")

@app.route("/ps4")
def ps4():
    return render_template("ps4.html")

@app.route("/x360")
def x360():
    return render_template("x360.html")

@app.route("/xone")
def xone():
    return render_template("xone.html")

