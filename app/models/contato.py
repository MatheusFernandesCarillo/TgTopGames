from app import db
from sqlalchemy import Float,Column,Integer,String,ForeignKey,DateTime,Time,Boolean


class Contato(db.Model):
    __tablename__ = "contatos"

    id          = Column(Integer(),primary_key=True,autoincrement = True)
    nome        = Column(String(),nullable = False)
    email       = Column(String(),nullable = False)
    mensagem    = Column(String(),nullable = False)
    
    def __init__(self,nome,email,mensagem):
        self.nome        = nome        
        self.email       = email      
        self.mensagem    = mensagem    

    def __repr__(self):
        return "<Contato %r>" % self.id
    
    def save(self):
        if self.id is None:
            db.session.add(self)
        db.session.commit()   

    


