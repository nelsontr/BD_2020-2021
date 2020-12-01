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
		raise exception 'O médico % não pode dar mais de 100 consultas por semana na mesma instituição', new.num_cedula;
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
begin
	
  return new;
 
 END;
 $$ Language plpgsql;
 
create trigger verifica_medico_trigger before insert on consulta
for each row execute procedure verifica_medico();
```

