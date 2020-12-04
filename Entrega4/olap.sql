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
	
