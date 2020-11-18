--####  QUERRIES TO PROBLEMS  ####

-- QUERY 1
-- Qual o concelho onde se fez o maior volume de vendas hoje?
SELECT i.num_concelho
FROM instituicao i
    INNER JOIN venda_farmacia v
    ON v.inst = i.nome
WHERE v.data_registo = CURRENT_DATE
GROUP BY i.num_concelho
HAVING SUM(preco) >= all(
    SELECT SUM(preco)
    FROM instituicao i 
        INNER JOIN venda_farmacia v 
        ON i.nome = v.inst
    WHERE v.data_registo = CURRENT_DATE
    GROUP BY num_concelho);


-- QUERY 2
--Qual o médico que mais prescreveu no 1º semestre de 2019 em cada região?
With temp as (
    SELECT num_regiao, num_cedula, COUNT(num_doente) as count
    FROM prescricao
    NATURAL JOIN consulta
    INNER JOIN instituicao
    ON consulta.nome_instituicao = instituicao.nome
    WHERE prescricao.data >= '2019/01/01' and prescricao.data <= '2019/06/30'
    GROUP BY num_regiao,num_cedula
    ORDER BY num_regiao ASC
)

SELECT num_regiao, num_cedula, count 
FROM temp sub 
    NATURAL JOIN 
    (SELECT num_regiao,MAX(sub.count) as count 
        FROM temp sub GROUP BY num_regiao) sub2;


-- QUERY 3
-- Quais são os médicos que já prescreveram aspirina em receitas aviadas em **todas** as farmácias
-- do concelho de Arouca este ano?
SELECT prescricao_venda.num_cedula
FROM prescricao_venda 
    NATURAL JOIN venda_farmacia
    INNER JOIN instituicao
    ON venda_farmacia.inst = instituicao.nome
WHERE prescricao_venda.substancia = 'aspirina'
    AND instituicao.tipo = 'farmacia'
    AND instituicao.num_concelho = 34
    AND EXTRACT(YEAR from prescricao_venda.data) = EXTRACT(YEAR from CURRENT_DATE)
GROUP BY prescricao_venda.num_cedula
HAVING COUNT(DISTINCT instituicao.nome) >= all(
	SELECT COUNT(instituicao.nome)
	FROM instituicao
    WHERE instituicao.tipo = 'farmacia'
        AND instituicao.num_concelho = 34
);


-- QUERY 4
-- Quais são os doentes que já fizeram análises mas ainda não aviaram prescrições este mês?
SELECT DISTINCT num_doente 
FROM analise
WHERE EXTRACT(MONTH from data_registo) = EXTRACT(MONTH from CURRENT_DATE)
	AND EXTRACT(YEAR from data_registo) = EXTRACT(YEAR from CURRENT_DATE)
	AND (num_cedula, num_doente, data) NOT IN 
        (
		SELECT num_cedula, num_doente, data
		FROM prescricao_venda 
		WHERE EXTRACT(MONTH from data_registo) = EXTRACT(MONTH from CURRENT_DATE)
			AND EXTRACT(YEAR from data_registo) = EXTRACT(YEAR from CURRENT_DATE)
	    );
