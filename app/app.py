from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def home():
    return "Olá, mundo! Aplicação rodando no Docker."

    
if __name__ == "__main__":
    ## EM TESTES
    # app.run(debug=True)
    
    # EM PRODUÇÃO
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
    # app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))