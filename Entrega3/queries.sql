--####  ADDING QUERRIES TO PROBLEMS  ####

-- Qual o concelho onde se fez o maior volume de vendas hoje?
SELECT nome
FROM concelho 
    INNER JOIN instituicao
    ON instituicao.num_regiao = concelho.num_regiao
    AND instituicao.num_concelho = concelho.num_concelho
    INNER JOIN venda_farmacia
    ON venda_farmacia.inst = instituicao.nome
WHERE venda_farmacia.data_registo = CURRENT_DATE
GROUP BY nome
HAVING count(*) >= all (
    SELECT count(*)
    FROM concelho
    GROUP BY nome);
    
--Qual o médico que mais prescreveu no 1º semestre de 2019 em cada região?
SELECT num_regiao, num_cedula
FROM consulta
    NATURAL JOIN prescricao
    INNER JOIN instituicao
    ON consulta.nome_instituicao = instituicao.nome
WHERE prescricao.data >= '2019/01/01' and prescricao.data <= '2019/06/30'
GROUP BY instituicao.num_regiao, consulta.num_cedula
HAVING count(*) >= all(
    SELECT count(*)
    FROM instituicao, consulta
    GROUP BY num_regiao, num_cedula 
)

-- QUERY 3
-- Quais são os médicos que já prescreveram aspirina em receitas aviadas em todas as farmácias
-- do concelho de Arouca este ano?
SELECT num_cedula
FROM prescricao_venda 
    INNER JOIN venda_farmacia
    ON prescricao_venda.num_venda = venda_farmacia.num_venda
    INNER JOIN instituicao
    ON venda_farmacia.inst = instituicao.nome
    INNER JOIN concelho
    ON instituicao.num_concelho = concelho.num_concelho
WHERE prescricao_venda.substancia = 'aspirina'
    AND instituicao.tipo = 'farmacia'
    AND concelho.nome = 'Arouca'
    AND YEAR(data) = YEAR(CURRENT_DATE);


-- QUERY 4
-- Quais são os doentes que já fizeram análises mas ainda não aviaram prescrições este mês?
SELECT num_doente 
FROM analise
WHERE MONTH(data) = MONTH(CURRENT_DATE)
    AND num_doente NOT IN (SELECT num_doente 
                            FROM prescricao_venda 
                            WHERE MONTH(data) = MONTH(CURRENT_DATE)
                            );
