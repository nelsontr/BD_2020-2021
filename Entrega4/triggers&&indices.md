## Triggers
```sql
--RI-100: um médico não pode dar mais de 100 consultas por semana na mesma instituição
drop trigger if exists verifica_medico_trigger on consulta;

create or replace function verifica_medico() returns trigger as $$
declare consultas decimal(20,2);

begin
	select count(*) into consultas
	from consulta c
	where c.num_cedula = new.num_cedula
	and c.nome_instituicao = new.nome_instituicao
	and EXTRACT(YEAR from c.data) = EXTRACT(YEAR from new.data)
	and EXTRACT(WEEK from c.data) = EXTRACT(WEEK from new.data);
	
	if consultas >= 100 then
		raise exception 'O médico % não pode dar mais de 100 consultas por semana na mesma instituição.', new.num_cedula;
  	end if;
  return new;
 
 END;
 $$ Language plpgsql;
 
create trigger verifica_medico_trigger before insert on consulta
for each row execute procedure verifica_medico();
```

```sql
--RI-análise: numa análise, a consulta associada pode estar omissa; não estando, a especialidade
--da consulta tem de ser igual à do médico.
drop trigger if exists verifica_especialidade_trigger on analise;

create or replace function verifica_especialidade() returns trigger as $$
declare especialidade varchar(25);
begin
	select m.especialidade into especialidade
	from consulta c natural join medico m
	where c.num_cedula = new.num_cedula
	and c.num_doente = new.num_doente
	and c.data = new.data;
	
	if especialidade is not null and especialidade != new.especialidade then
		raise exception 'O médico % não tem a especialidade necessária para analisar.', new.num_cedula;
  	end if;
  return new;
 
 END;
 $$ Language plpgsql;
 
create trigger verifica_especialidade_trigger before insert on analise
for each row execute procedure verifica_especialidade();
```



## ÍNDICES (???)

#### Query 1:

​	-> (Se for criado um índice para o trio): Criar um índice, na tabela consulta para o atributo num_doente; 

​	-> (Se for criado um índice por cada atributo que é chave): não é necessário criar nenhum índice porque é criado implicitamente para as chaves primárias e assim, o atributo num_doente, sendo chave da tabela consulta já tem um índice associado. Pode ser preciso alterar a ordem dos campos das chaves primárias na declaração da tabela consulta para que o num_doente seja o primeiro atributo;

#### Query 2:

​	Provavelmente, índice do tipo Hash:

​	São os melhores para seleção por igualdade;

​	Há uma estrutura;
 
 Criar um índice do tipo Hash para o atributo especialidade da tabela medico porque fica dividido            
 por vários contentores e assim cada contentor guarda um conjunto de entradas e o acesso fica otimizado 
 através da função de dispersão.

#### Query 3:
Blocos do disco são de 2KBytes e cada registo ocupa 1kByte, ou seja, cada bloco leva 2 registos. Seletividade de (1/6) = 0.16666667 ou seja, a probabilidade de um bloco não ter respostas é de (1-0.16666667)^2 (por serem dois registos por bloco), que é aproximadamente 69%. Logo, teremos de ler 31% dos blocos. Quanto menor for a resposta, maior é o benefício dos índices a reduzir leituras do disco. Assim, é útil, criar um índice.
(???) do tipo Hash na tabela medico no atributo especialidade:
CREATE INDEX index_especialidade ON medico(especialidade)

​	Provavelmente, índice do tipo Hash:

​	São os melhores para seleção por igualdade;

​	Há uma estrutura;
 
 Criar um índice do tipo Hash para o atributo especialidade da tabela medico porque fica dividido            
 por vários contentores e assim cada contentor guarda um conjunto de entradas e o acesso fica otimizado 
 através da função de dispersão.
 
 

#### Query 4:

​	Provavelmente, índice do tipo BTree:

​	As folhas do índice estão sempre ordenadas e é útil na procura de "ranges" (maior, menor, entre);

​	Como num_cedula é foreign key na tabela consulta, não tem nenhum índice criado implicitamente. Assim, é útil criar um índice na tabela consulta no atributo num_cedula. 
CREATE INDEX idx_cedula on consulta(num_cedula).

​	Criar um índice do tipo BTree para o atributo "data" da tabela consulta para otimizar a comparação entre as duas datas dadas. Esta otimização acontece porque as folhas do índice estão sempre ordenadas, .
CREATE INDEX idx_data on consulta USING B-TREE(data)

	
