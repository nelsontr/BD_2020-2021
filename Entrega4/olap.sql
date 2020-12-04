--1

SELECT especialidade, mes, ano, count(*)
FROM f_analise a 
	INNER JOIN medico ON a.id_medico = medico.num_cedula
	INNER JOIN d_tempo ON a.id_data_registo = d_tempo.id_tempo
WHERE d_tempo.ano >= 2017 
	AND d_tempo.ano <= 2020
	AND a.nome = 'glicemia'
GROUP BY CUBE(especialidade, mes, ano)
ORDER BY especialidade, ano, mes ASC;
	
--2

WITH TEMP AS(
	SELECT substancia, num_concelho, dia_da_semana, mes, SUM(quant) AS sum_quant, COUNT(*) AS c
	FROM f_presc_venda v
		NATURAL JOIN d_instituicao
		INNER JOIN d_tempo on v.id_data_registo = d_tempo.id_tempo
	WHERE num_regiao = 2
		AND trimestre = 1
		AND ano = 2020
	GROUP BY ROLLUP(substancia, num_concelho, dia_da_semana, mes)
	ORDER BY substancia, mes, dia_da_semana asc
)

SELECT substancia, num_concelho, dia_da_semana, mes, sum_quant,
CASE
WHEN dia_da_semana IS NULL AND mes IS NULL THEN
	CAST(CAST(c AS FLOAT)/90 AS FLOAT(3))

WHEN dia_da_semana IS NOT NULL AND mes IS NULL THEN
	CAST(CAST(c AS FLOAT)/13 AS FLOAT(3))

WHEN dia_da_semana IS NOT null AND mes IS NOT null THEN
	CAST(CAST(c AS FLOAT)/4 AS FLOAT(3))
END AS media
FROM TEMP sub
