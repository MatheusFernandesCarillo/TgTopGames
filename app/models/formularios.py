from flask_wtf import Form
from wtforms.fields.html5 import EmailField
from wtforms import StringField,TextAreaField,PasswordField
from wtforms.validators import DataRequired,Email
from app.models.contato import Contato


class NovoContato(Form):
    nome                = StringField("nome",validators=[DataRequired()])
    email               = EmailField("email",validators=[DataRequired(),Email()])
    mensagem            = TextAreaField("mensagem",validators=[DataRequired()])

   
    def create(self):
        return Contato(self.nome.data,self.email.data,self.mensagem.data)


class loginForm(Form):
    senha             = PasswordField("nome",validators=[DataRequired()])