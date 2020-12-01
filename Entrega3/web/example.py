#!/usr/bin/python3

from wsgiref.handlers import CGIHandler
from flask import Flask
from flask import render_template, request, redirect

## Libs postgres
import psycopg2
import psycopg2.extras

app = Flask(__name__)

## SGBD configs
DB_HOST="localhost"
DB_USER="postgres" 
DB_DATABASE=DB_USER
DB_PASSWORD="NT18/19"
DB_CONNECTION_STRING = "host=%s dbname=%s user=%s password=%s" % (DB_HOST, DB_DATABASE, DB_USER, DB_PASSWORD)


## Runs the function once the root page is requested.
## The request comes with the folder structure setting ~/web as the root
@app.route('/')
def list_index():
  try:
    return render_template("index.html", params=request.args)
  except Exception as e:
    return str(e)

@app.route('/instituicao')
def list_instituicao_edit():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "SELECT * FROM instituicao;"
    print(cursor.execute(query))
    return render_template("instituicao.html", cursor=cursor, params=request.args)
  except Exception as e:
    return str(e) 
  finally:
    cursor.close()
    dbConn.close()

@app.route('/instituicao/insert')
def insert_instituicao():
  try:
    return render_template("instituicaoInsert.html", params=request.args)
  except Exception as e:
    return str(e)

@app.route('/instituicao/insert/done', methods=["POST"])
def insert_instituicao_done():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = f'''INSERT into instituicao(nome, tipo, num_regiao, num_concelho) VALUES(
      '{request.form["nome_novo"]}','{request.form["tipo"]}',
      '{request.form["regiao"]}','{request.form["concelho"]}');'''
    cursor.execute(query)
    return redirect('/instituicao')
  except Exception as e:
    return str(e) 
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()


@app.route('/instituicao/update')
def update_instituicao():
  try:
    return render_template("instituicaoUpdate.html", params=request.args)
  except Exception as e:
    return str(e)


@app.route('/instituicao/update/done', methods=["POST"])
def update_instituicao_done():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = f'''UPDATE instituicao
      SET nome='{request.form["nome_novo"]}',
      tipo='{request.form["tipo"]}',
      num_regiao ='{request.form["regiao"]}',
      num_concelho ='{request.form["concelho"]}'
      WHERE nome='{request.form["nome"]}';'''
    cursor.execute(query)
    return redirect('/instituicao')
  except Exception as e:
    return str(e) 
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

@app.route('/instituicao/delete')
def delete_instituicao():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = f'''DELETE FROM instituicao
      WHERE nome='{request.args["nome"]}';'''
    cursor.execute(query)
    return redirect('/instituicao')
  except Exception as e:
    return str(e) 
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()



@app.route('/medico')
def list_medico_edit():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "SELECT * FROM medico;"
    print(cursor.execute(query))
    return render_template("medico.html", cursor=cursor, params=request.args)
  except Exception as e:
    return str(e) 
  finally:
    cursor.close()
    dbConn.close()

@app.route('/medico/insert')
def insert_medico():
  try:
    return render_template("medicoInsert.html", params=request.args)
  except Exception as e:
    return str(e)

@app.route('/medico/insert/done', methods=["POST"])
def insert_medico_done():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = f'''INSERT into medico VALUES(
      {request.form["num_cedulaNovo"]},'{request.form["nome"]}','{request.form["especialidade"]}');'''
    cursor.execute(query)
    return redirect('/medico')
  except Exception as e:
    return str(e) 
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()


@app.route('/medico/update')
def update_medico():
  try:
    return render_template("medicoUpdate.html", params=request.args)
  except Exception as e:
    return str(e)


@app.route('/medico/update/done', methods=["POST"])
def update_medico_done():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = f'''UPDATE medico
      SET num_cedula='{request.form["num_cedulaNovo"]}',
      nome='{request.form["nome"]}',
      especialidade ='{request.form["especialidade"]}'
      WHERE num_cedula={request.form["num_cedula"]};'''
    cursor.execute(query)
    return redirect('/medico')
  except Exception as e:
    return str(e) 
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

@app.route('/medico/delete')
def delete_medico():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = f'''DELETE FROM medico
      WHERE num_cedula='{request.args["num_cedula"]}';'''
    cursor.execute(query)
    return redirect('/medico')
  except Exception as e:
    return str(e) 
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

  


@app.route('/prescricao')
def list_prescricao_edit():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "SELECT * FROM prescricao;"
    print(cursor.execute(query))
    return render_template("prescricao.html", cursor=cursor, params=request.args)
  except Exception as e:
    return str(e) 
  finally:
    cursor.close()
    dbConn.close()

@app.route('/prescricao/insert')
def insert_prescricao():
  try:
    return render_template("prescricaoInsert.html", params=request.args)
  except Exception as e:
    return str(e)

@app.route('/prescricao/insert/done', methods=["POST"])
def insert_prescricao_done():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = f'''INSERT into prescricao VALUES(
      {request.form["num_cedula"]},{request.form["num_doente"]},'{request.form["data"]}', '{request.form["substancia"]}','{request.form["quantidade"]}');'''
    cursor.execute(query)
    return redirect('/prescricao')
  except Exception as e:
    return str(e) 
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()


@app.route('/prescricao/update')
def update_prescricao():
  try:
    return render_template("prescricaoUpdate.html", params=request.args)
  except Exception as e:
    return str(e)


@app.route('/prescricao/update/done', methods=["POST"])
def update_prescricao_done():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = f'''UPDATE prescricao
      SET num_cedula='{request.form["num_cedulaNovo"]}',
      num_doente='{request.form["num_doenteNovo"]}',
      data='{request.form["dataNovo"]}',
      substancia ='{request.form["substanciaNovo"]}',
      quantidade = '{request.form["quantidade"]}'
      WHERE num_cedula={request.args["num_cedula"]}
      AND num_doente={request.args["num_doente"]}
      AND data='{request.args["data"]}'
      AND substancia ='{request.args["substancia"]}';'''
    cursor.execute(query)
    return redirect('/prescricao')
  except Exception as e:
    return str(e) 
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

@app.route('/prescricao/delete')
def delete_prescricao():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = f'''DELETE FROM prescricao
      WHERE num_cedula={request.args["num_cedula"]}
      AND num_doente={request.args["num_doente"]}
      AND data='{request.args["data"]}'
      AND substancia ='{request.args["substancia"]}';'''
    cursor.execute(query)
    return redirect('/prescricao')
  except Exception as e:
    return str(e) 
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()


if __name__ == '__main__':
    app.run()
