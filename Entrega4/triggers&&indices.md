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
declare especialidade char(25)
begin
	select m.especialidade into especialidade
	from consulta c natural join medico m
	where c.num_cedula = new.num_cedula
	and c.num_doente = new.num_doente
	and c.data = new.data;
	
	if especialidade != new.especialidade then
		raise exception 'O médico % não tem a especialidade necessária para analisar.', new.num_cedula;
  	end if;
  return new;
 
 END;
 $$ Language plpgsql;
 
create trigger verifica_especialidade_trigger before insert on analise
for each row execute procedure verifica_especialidade();
```



## ÍNDICES (???)

##### Query 1:

​	-> Criar um índice, na tabela consulta para o atributo num_doente;

##### Query 2:

​	Provavelmente, índice do tipo Hash:

​	São os melhores para seleção por igualdade;

​	Há uma estrutura;
 
 Criar um índice do tipo Hash para o atributo especialidade da tabela medico porque fica dividido            
 por vários contentores e assim cada contentor guarda um conjunto de entradas e o acesso fica otimizado 
 através da função de dispersão.

##### Query 3:

##### Query 4:

​	Provavelmente, índice do tipo BTree:

​	As folhas do índice estão sempre ordenadas e é útil na procura de "ranges" (maior, menor, entre);

​	Criar um índice do tipo BTree para o atributo "data" da tabela consulta para otimizar a comparação entre as duas datas dadas. Esta otimização acontece porque as folhas do índice estão sempre ordenadas.

