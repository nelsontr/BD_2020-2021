
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
