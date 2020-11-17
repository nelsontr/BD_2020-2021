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
SELECT num_regiao, num_cedula
FROM prescricao
    NATURAL JOIN consulta
    INNER JOIN instituicao
    ON consulta.nome_instituicao = instituicao.nome
WHERE prescricao.data >= '2019/01/01' and prescricao.data <= '2019/06/30'
GROUP BY num_regiao, num_cedula
HAVING COUNT(data) >= all(
	SELECT COUNT(data)
	FROM prescricao
    NATURAL JOIN consulta
    INNER JOIN instituicao
    ON consulta.nome_instituicao = instituicao.nome
	WHERE prescricao.data >= '2019/01/01' and prescricao.data <= '2019/06/30'
	GROUP BY num_regiao, num_cedula
);


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
HAVING COUNT(prescricao_venda.num_cedula) >= all(
	SELECT COUNT(instituicao.nome)
	FROM instituicao
    WHERE instituicao.tipo = 'farmacia'
        AND instituicao.num_concelho = 34
    GROUP BY instituicao.nome
);


-- QUERY 4
-- Quais são os doentes que já fizeram análises mas ainda não aviaram prescrições este mês?
SELECT DISTINCT num_doente 
FROM analise
WHERE EXTRACT(MONTH from data) = EXTRACT(MONTH from CURRENT_DATE)
	AND EXTRACT(YEAR from data) = EXTRACT(YEAR from CURRENT_DATE)
	AND num_doente NOT IN 
        (
		SELECT num_doente 
		FROM prescricao_venda 
		WHERE EXTRACT(MONTH from data) = EXTRACT(MONTH from CURRENT_DATE)
			AND EXTRACT(YEAR from data) = EXTRACT(YEAR from CURRENT_DATE)
	    );