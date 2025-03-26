# from flask import Flask
from flask import Flask, render_template


import mysql.connector
from mysql.connector import Error


app = Flask(__name__)


# Função para testar a conexão ao MySQL
def test_mysql_connection():
    connection = None  # Inicializando connection como None
    try:
        connection = mysql.connector.connect(
            host='db',  # Nome do container do MySQL no Docker Compose
            port=3306,
            user='flask_user',
            password='flask_password',
            database='flask_db'
        )
        if connection.is_connected():
            print("Conexão ao MySQL foi bem-sucedida!")
            return "Conexão bem-sucedida!"
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return f"Erro: {e}"
    finally:
        if connection and connection.is_connected():
            connection.close()


@app.route("/")
def home():
    # return "Olá, mundo! Aplicação rodando no Docker."
    # return render_template('index.html')
    connection_status = test_mysql_connection()
    return render_template('index.html', connection_status=connection_status)
    

@app.route('/user/<username>')
def show_user(username):
    return f"Bem-vindo, {username}!"


@app.route("/sobre")
def sobre():
    return render_template('sobre.html')


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=8000)
    app.run(debug=True)