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

INSERT INTO d_instituicao(nome, tipo, num_regiao, num_concelho)
SELECT inst.nome,
		inst.tipo,
		inst.num_regiao,
		inst.num_concelho
FROM instituicao inst
