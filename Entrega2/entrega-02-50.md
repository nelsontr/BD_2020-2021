# Relacional

Observação(*ID*, #Doente, Valor)

Intervenção(*ID*, data observação) {

​	ID: FK(Observação)

}

Medição(*ID*, tipo) {

​	ID: FK(Observação)

}

Acto Médico(*ID*, *#número*){

​	ID: FK(Intervenção)

}

Médico(*#Cédula*, Nome, Especialidade) 

Agenda(***Data, Hora***)

Instituição(*Nome*, *Morada*)



Consulta (***#Cédula, Data, Hora***, ID, #numero, especialidade) {

​	#Cédula: FK(Médico)

​	Data, Hora: FK(Agenda.Data, Agenda.Hora)

​	ID, #numero: FK(ActoMédico.ID, ActoMédico.#numero) NOT NULL

}

Protocolo(***NºProtocolo***, data de homologação, descrição) 

AnáliseLab(*ID*) {

​	ID: FK(Medição)

}

TemplateAnalise(***NºProtocolo, Nome, Morada, ID***){
    
    NºProtocolo: FK(Protocolo)
    
    Nome, Morada: FK(Instituição.Nome, Instituição.Morada)
    
    ID: FK(AnáliseLab)
}



Validado(***Nome, Morada, NºProtocolo, IDTemplateAnálise***, #numero, IDAtoMedico, data){
    
    Nome, Morada, NºProtocolo, IDTemplateAnálise: FK(TemplateAnálise.Nome, TemplateAnálise.Morada, TemplateAnálise.NºProtocolo, TemplateAnálise.ID)
    
    #numero, IDAtoMedico: FK(AtoMédico.#numero, AtoMédico.ID) NOT NULL

}

Faz(**#cédula, NºProtocolo, Nome, Morada, ID***){
    
    #cédula: FK(Médico)
    
    NºProtocolo, Nome, Morada, ID: FK(TemplateAnálise.NºProtocolo, TemplateAnálise.Nome, TemplateAnálise.Morada, TemplateAnálise.ID)

}

LeituraLocal(*ID*) {

​	ID: FK(Medição)

}

Segundo(***NºProtocolo, ID***){

    NºProtocolo: FK(Protocolo)
    
    ID: FK(LeituraLocal)

}


# Restrições
** (seta total)
-> ID nunca existe em Intervenção e Medição ao mesmo tempo
-> ID tem de existir em Intervenção ou em Medição
**

** (dupla seta entre AnáliseLab e TemplateAnálise)
-> para todo o ID da tabela AnáliseLab tem de existir pelo menos uma entrada na tabela TemplateAnálise
**



# Algebra Relacional

### Pergunta 1:
    Join da consulta com médico?
    π #Cédula, Nome, Especialidade(σ Data = "20-11-2020" ∧ Hora = "14:00" (Consulta) ⋈Consulta.#cédula = Médico.#cédula Médico)

### Pergunta 2:



# SQL
### Pergunta 1
```sql
SELECT m.cedula
FROM Médico m, Consulta c
WHERE m.cedula = c.cedula
	AND c.data = "20-11-2020" 
	And c.hora = "14:00"
```
### Pergunta 2
```sql
With tempr as (
  SELECT d.customer_name as costu, COUNT(DISTINCT d.account_number) as anali
  FROM depositor d
  GROUP BY d.customer_name
  ORDER BY anali DESC
)

SELECT sub.costu
From tempr sub
WHERE sub.anali = (SELECT MAX(tempr.anali) From tempr)
```
### Pergunta 3
```sql
SELECT o.#Doente as doente
FROM Observação o, TemplateAnalise t
WHERE (SELECT COUNT(DISTINCT t.NºProtocolo) FROM TemplateAnalise t)
			= (SELECT COUNT(DISTINCT p.NºProtocolo) FROM Protocolo p)
	AND t.ID == o.ID
```
