# d_tempo
With temp as (
	SELECT DISTINCT data from prescricao_venda pv
	UNION
	SELECT DISTINCT data from analise a
)
INSERT INTO d_tempo(dia, dia_da_semana, semana, mes, trimestre, ano)
SELECT extract(day from data), 
		extract(dow from data),
		extract(week from data),
		extract(month from data),
		extract(quarter from data),
		extract(year from data)
FROM temp sub;

# d_instituicao
INSERT INTO d_instituicao(nome, tipo, num_regiao, num_concelho)
SELECT inst.nome,
		inst.tipo,
		inst.num_regiao,
		inst.num_concelho
FROM instituicao inst

# f_presc_venda
With temp as (
	SELECT num_cedula, num_doente, id_tempo, substancia, num_venda
	FROM prescricao_venda pv 
	INNER JOIN d_tempo dt
	ON (
		dt.ano = extract(year from pv.data) and
		dt.mes = extract(month from pv.data) and
		dt.dia = extract(day from pv.data)
		)
)
INSERT INTO f_presc_venda(id_presc_venda, id_medico, num_doente, id_data_registo, id_inst, substancia, quant)
SELECT t.num_venda, num_cedula, num_doente, id_tempo, id_inst, substancia, quant
FROM temp t
INNER JOIN (
	SELECT num_venda, id_inst, quant
	FROM venda_farmacia vf
	INNER JOIN d_instituicao di
	ON vf.inst = di.nome
	) t2
ON t.num_venda = t2.num_venda

# f_analise
with temp as(
	SELECT num_analise, num_cedula, num_doente, id_tempo, inst, nome, quant
	FROM analise a 
	INNER JOIN d_tempo dt
	ON (
		dt.ano = extract(year from a.data) and
		dt.mes = extract(month from a.data) and
		dt.dia = extract(day from a.data)
	)
)
INSERT INTO f_analise(id_analise, id_medico, num_doente, id_data_registo, id_inst, nome, quant)
SELECT num_analise, num_cedula, num_doente, id_tempo, id_inst, t.nome, quant
FROM temp t
INNER JOIN d_instituicao di
ON di.nome = t.inst
