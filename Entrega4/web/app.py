#!/usr/bin/python3

from wsgiref.handlers import CGIHandler
from flask import Flask
from flask import render_template, request, redirect, url_for

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
    query = "SELECT * FROM instituicao ORDER BY nome ASC;"
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
    query = f'''INSERT into instituicao(nome, tipo, num_regiao, num_concelho) VALUES(%s,%s,%s,%s);'''
    data = (request.form["nome_novo"],
      request.form["tipo"],
      request.form["regiao"],
      request.form["concelho"])
    cursor.execute(query,data)
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
      SET nome=%s,
      tipo=%s,
      num_regiao =%s,
      num_concelho =%s
      WHERE nome=%s;'''
    data = (request.form["nome_novo"],
      request.form["tipo"],
      request.form["regiao"],
      request.form["concelho"],
      request.form["nome"])
    cursor.execute(query, data)
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
    query = f'''DELETE FROM instituicao WHERE nome=%s;'''
    data = (request.args["nome"],)
    cursor.execute(query,data)
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
    query = "SELECT * FROM medico ORDER BY num_cedula ASC;"
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
    query = f'''INSERT into medico VALUES(%s,%s,%s);'''
    data = (request.form["num_cedulaNovo"],
      request.form["nome"],
      request.form["especialidade"])
    cursor.execute(query,data)
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
      SET num_cedula=%s,
      nome=%s,
      especialidade=%s
      WHERE num_cedula=%s;'''
    data = (request.form["num_cedulaNovo"],
        request.form["nome"],
        request.form["especialidade"],
        request.form["num_cedula"])
    cursor.execute(query, data)
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
      WHERE num_cedula=%s;'''
    data = (request.args["num_cedula"],)
    cursor.execute(query, data)
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
    query = "SELECT * FROM prescricao ORDER BY num_cedula ASC, num_doente ASC;"
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
    query = f'''INSERT into prescricao VALUES(%s,%s,%s, %s, %s);'''
    data = (request.form["num_cedula"],
        request.form["num_doente"],
        request.form["data"],
        request.form["substancia"],
        request.form["quantidade"])
    cursor.execute(query,data)
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
      SET num_cedula=%s, num_doente=%s, data=%s,
      substancia =%s, quantidade = '%s
      WHERE num_cedula=%s
        AND num_doente=%s
        AND data=%s
        AND substancia =%s;'''
    data = (request.form["num_cedulaNovo"],
      request.form["num_doenteNovo"], request.form["dataNovo"],
      request.form["substanciaNovo"], request.form["quantidade"],
      request.args["num_cedula"], request.args["num_doente"],
      request.args["data"], request.args["substancia"])
    cursor.execute(query,data)
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
      WHERE num_cedula=%s
      AND num_doente=%s
      AND data=%s
      AND substancia=%s;'''
    data = (request.args["num_cedula"], request.args["num_doente"],\
      request.args["data"],request.args["substancia"])
    cursor.execute(query, data)
    return redirect('/prescricao')
  except Exception as e:
    return str(e)
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()



@app.route('/analise')
def list_analise_edit():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "SELECT * FROM analise;"
    cursor.execute(query)
    return render_template("analise.html", cursor=cursor, params=request.args)
  except Exception as e:
    return str(e)
  finally:
    cursor.close()
    dbConn.close()

@app.route('/analise/insert')
def insert_analise():
  try:
    return render_template("analiseInsert.html", params=request.args)
  except Exception as e:
    return str(e)

@app.route('/analise/insert/done', methods=["POST"])
def insert_analise_done():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = f'''INSERT into analise VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);'''
    data = ( request.form["num_analise"], request.form["especialidade"], request.form["num_cedula"],request.form["num_doente"],
      request.form["data"], request.form["data_registo"], request.form["nome"],request.form["quantidade"], request.form["instituicao"])
    cursor.execute(query,data)
    return redirect('/analise')
  except Exception as e:
    return str(e)
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()


@app.route('/analise/update')
def update_analise():
  try:
    return render_template("analiseUpdate.html", params=request.args)
  except Exception as e:
    return str(e)


@app.route('/analise/update/done', methods=["POST"])
def update_analise_done():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = f'''UPDATE analise
      SET num_analise=%s, especialidade=%s,
      num_cedula=%s, num_doente=%s,
      data=%s, data_registo=%s,
      nome=%s, quant=%s, inst=%s
      WHERE num_analise=%s;'''
    data = (request.form["num_analise"], request.form["especialidade"],
      request.form["num_cedula"], request.form["num_doente"],
      request.form["data"], request.form["data_registo"],
      request.form["nome"], request.form["quantidade"],
      request.form["instituicao"], request.form["num_analise"])
    cursor.execute(query, data)
    return redirect('/analise')
  except Exception as e:
    return str(e)
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

@app.route('/analise/delete')
def delete_analise():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = f'''DELETE FROM analise
      WHERE num_analise=%s;'''
    data = (request.args["num_analise"],)
    cursor.execute(query,data)
    return redirect('/analise')
  except Exception as e:
    return str(e)
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()


@app.route('/perguntad')
def perguntad_form():
  try:
    return render_template("perguntad.html", params=request.args)
  except Exception as e:
    return str(e)

@app.route('/perguntad/done', methods=["POST"])
def perguntad_done():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "SELECT DISTINCT(substancia)\
        FROM prescricao\
        WHERE EXTRACT(MONTH from data)=%s \
        AND EXTRACT(YEAR from data)=%s;"
    data = (request.form["mes"],request.form["ano"])
    print(query, data)
    cursor.execute(query, data)
    return render_template("perguntadTable.html", cursor=cursor, params=request.args)
  except Exception as e:
    return str(e)
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()


@app.route('/registoVenda')
def registoVenda_form():
  try:
    return render_template("registoVenda.html", params=request.args)
  except Exception as e:
    return str(e)

@app.route('/venda_farmacia')
def venda_farmacia_list():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "SELECT * FROM venda_farmacia ORDER BY num_venda DESC;"
    cursor.execute(query)
    return render_template("venda_farmacia.html", cursor=cursor, params=request.args)
  except Exception as e:
    return str(e)
  finally:
    cursor.close()
    dbConn.close()

@app.route('/prescricao_venda')
def prescricao_venda_list():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "SELECT * FROM prescricao_venda ORDER BY num_venda DESC;"
    cursor.execute(query)
    return render_template("prescricao_venda.html", cursor=cursor, params=request.args)
  except Exception as e:
    return str(e)
  finally:
    cursor.close()
    dbConn.close()

@app.route('/registoVenda/prescricao', methods=["POST"])
def registoVenda_prescricao():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query =\
    f'''INSERT INTO venda_farmacia
    SELECT (SELECT num_venda
    FROM venda_farmacia
    ORDER BY num_venda DESC
    LIMIT 1)+1 as num_venda, data as data_registo, substancia, quant, %s as preco,nome_instituicao as inst
    FROM prescricao NATURAL JOIN consulta
    WHERE num_cedula=%s
    AND num_doente=%s
    AND data=%s
    AND substancia=%s;'''
    data = (request.form["preco"],request.form["num_cedula"],\
      request.form["num_doente"],request.form["data"], request.form["substancia"])
    cursor.execute(query, data)

    query =\
    f'''INSERT INTO prescricao_venda
    SELECT num_cedula, num_doente, data, substancia, (SELECT num_venda
    FROM venda_farmacia
    ORDER BY num_venda DESC
    LIMIT 1) as num_venda
    FROM prescricao NATURAL JOIN consulta
    WHERE num_cedula=%s
    AND num_doente=%s
    AND data=%s
    AND substancia=%s;'''
    data = (request.form["num_cedula"],request.form["num_doente"],\
      request.form["data"], request.form["substancia"])
    cursor.execute(query,data)
    return redirect('/prescricao_venda')
  except Exception as e:
    return str(e)
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

@app.route('/registoVenda/vendaUnica', methods=["POST"])
def registoVenda_venda():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = f'''INSERT INTO venda_farmacia VALUES(%s, %s,%s,%s, %s, %s);'''
    data = (request.form["num_venda"],request.form["data"],request.form["substancia"],\
      request.form["quantidade"],request.form["preco"],request.form["instituicao"])
    cursor.execute(query,data)
    return redirect("/venda_farmacia")
  except Exception as e:
    return str(e)
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

@app.route('/perguntae')
def perguntae():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = f'''
    With temp as (
    SELECT num_concelho, num_doente, COUNT(a.nome) as counter
    FROM analise a
    INNER JOIN instituicao i
    ON a.inst = i.nome
    WHERE a.nome='glicemia'
    GROUP BY num_concelho, num_doente
    ORDER BY num_concelho ASC
    )
	
    SELECT *
    FROM (SELECT num_concelho, num_doente as maxi_id, counter as maxi
        FROM temp sub 
          NATURAL JOIN 
          (SELECT num_concelho,MAX(sub.counter) as counter 
            FROM temp sub GROUP BY num_concelho) sub2) al
      NATURAL JOIN (SELECT num_concelho, num_doente as minimo_id, counter as mini
        FROM temp sub 
          NATURAL JOIN 
          (SELECT num_concelho,MIN(sub.counter) as counter 
              FROM temp sub GROUP BY num_concelho) sub2)  al2
      ORDER BY num_concelho ASC, maxi DESC, mini DESC'''
    cursor.execute(query)
    return render_template("perguntae.html", cursor=cursor, params=request.args)
  except Exception as e:
    return str(e)
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()


if __name__ == '__main__':
    app.run()