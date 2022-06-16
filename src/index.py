#Archiv Principal de Arranque del Servidor
from app import app

#Arrancando el Servidor
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)
