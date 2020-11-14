--####  ADDING QUERRIES TO PROBLEMS  ####

-- Qual o concelho onde se fez o maior volume de vendas hoje?
select nome
from concelho 
    INNER JOIN instituicao
    ON instituicao.num_regiao = concelho.num_regiao
    AND instituicao.num_concelho = concelho.num_concelho
    INNER JOIN venda_farmacia
    ON venda_farmacia.inst = instituicao.nome
WHERE venda_farmacia.data_registo = CAST(CURRENT_TIMESTAMP AS DATE)
GROUP BY nome
HAVING count(*) >= all (
    SELECT count(*)
    FROM concelho
    GROUP BY nome);
    
--Qual o médico que mais prescreveu no 1º semestre de 2019 em cada região?

