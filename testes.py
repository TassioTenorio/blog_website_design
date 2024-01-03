from main import app, database
from models import Usuario, Post


# with app.app_context():
   # database.create_all()

#with app.app_context():
    #usuario = Usuario(username="Tassio", email="tassio@gmail.com", senha="123456")
    #usuario2 = Usuario(username="Joao", email="joao@gmail.com", senha="123456")
    #database.session.add(usuario)
    #database.session.add(usuario2)
    #database.session.commit()

# with app.app_context():
#   usuario_teste = Usuario.query.filter_by(email='tassio@gmail.com').first()
#   print(usuario_teste)
#   print(usuario_teste.username)


# with app.app_context():
#     meu_post = Post(id_usuario=1, titulo="Primeiro Post do Tassio", corpo="Tassio Voando")
#     database.session.add(meu_post)
#     database.session.commit()

#
# with app.app_context():
#     post = Post.query.first()
#     print(post.titulo)
#     print(post.autor.email)


with app.app_context():
    database.drop_all()
    database.create_all()

