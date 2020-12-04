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

with temp as(
	select substancia, num_concelho, dia_da_semana, mes, sum(quant) as sum_quant, count(*) as c
	from f_presc_venda v
		natural join d_instituicao
		inner join d_tempo on v.id_data_registo = d_tempo.id_tempo
	where num_regiao = 2
		and trimestre = 1
		and ano = 2020
	group by rollup(substancia, num_concelho, dia_da_semana, mes)
	order by substancia, mes, dia_da_semana asc
)

select substancia, num_concelho, dia_da_semana, mes, sum_quant,
case
when dia_da_semana is null and mes is null then
	cast(cast(c as float)/90 as float(3))

when dia_da_semana is not null and mes is null then
	cast(cast(c as float)/13 as float(3))

when dia_da_semana is not null and mes is not null then
	cast(cast(c as float)/4 as float(3))
end as media
from temp sub
