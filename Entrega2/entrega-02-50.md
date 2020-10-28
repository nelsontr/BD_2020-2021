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
-> ID nunca existe em Intervenção e Medição ao mesmo tempo;
-> ID tem de existir em Intervenção ou em Medição;
**

** (dupla seta entre AnáliseLab e TemplateAnálise);
-> para todo o ID da tabela AnáliseLab tem de existir pelo menos uma entrada na tabela TemplateAnálise;
**

**

(RI-1): Para cada Médico cuja #Cédula está presente na tabela Consulta, a sua especialidade tem de ser igual à especialidade presente também na tabela Consulta;

(RI-2): Para cada quarteto NºProtocolo, Nome, Morada e ID presente na tabela TemplateAnalise tem de existir uma entrada na tabela Faz ou na tabela Validado;

(RI-3): Para todo o #numero na tabela Acto Médico, não pode existir uma entrada nas tabelas TemplateAnálise e Consulta que seja igual;

# Álgebra Relacional

### Pergunta 1:
    π #Cédula(σ Data = "20-11-2020" ∧ Hora = "14:00" (Consulta))

### Pergunta 2:
    Aux <- π(#Doente, ID) (Observação ⋈ AnaliseLab)
    Counter <- pCounter(2->Analises)#Doente Gcount(ID)(Aux)
    π#Doente(σAnalises = MAX(Counter * pR(1->MAX)(GMax(Analises)(Counter))))

### Pergunta 3:
    AuxProtocolos <- pAuxProtocolos(1->Limite)Gcount(Nr.Protocolo)(Protocolo)
    AuxDoentes <- π(#Doente, ID, NrProtocolo) (Observação ⋈ TemplateAnalise)
    ProtocolosAnalise <- pProtocolosAnalise(3->counter)#Doente, ID G count-distinct(NrProtocolo) (AuxDoentes)
    π#Doente(σ AuxProtocolos.Limite = ProtocolosAnalise.counter(AuxProtocolos * ProtocolosAnalise))

### Pergunta 4:

    

### Pergunta 5:

    (π #Cédula, especialidade(Médico)) / (π especialidade(σ Data >= "1-1-2020" ∧ Data <= "2-2-2020" (Consulta)))

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
  SELECT o.customer_street as Nome_Doente, COUNT(a.customer_name) as num_Analises
  FROM customer o NATURAL JOIN depositor a
  GROUP BY o.customer_name
  ORDER BY num_Analises DESC, Nome_Doente ASC
)

SELECT Nome_Doente
From tempr sub
WHERE sub.num_Analises = (SELECT MAX(sub.num_Analises) FROM tempr sub);

-------

With tempr as (
  SELECT o.Doente as Nome_Doente, COUNT(DISTINCT a.ID) as num_Analises
  FROM Observação o, AnáliseLab a
  WHERE a.ID = o.ID
  GROUP BY Nome_Doente
  ORDER BY Nome_Doente ASC, num_Analises DESC
)

SELECT Nome_Doente
From tempr sub
WHERE sub.num_Analises = (SELECT MAX(sub.num_Analises) FROM tempr sub);
```
### Pergunta 3
```sql
With tempr as (
  SELECT a.customer_name as Nome, COUNT(DISTINCT a.account_number) as Protocolos
  FROM account o NATURAL JOIN depositor a
  GROUP BY a.customer_name
  ORDER BY Protocolos DESC, Nome ASC
)

SELECT *
From tempr sub
WHERE sub.Protocolos < (SELECT COUNT(o.account_number) FROM account o);

-------

With tempr as (
  SELECT o.Doente as Doente, COUNT(DISTINCT t.NrProtocolo) as CounterProtocolos
  FROM TemplateAnalise t NATURAL JOIN Observação o
  GROUP BY Doente
  ORDER BY CounterProtocolos DESC, Doente ASC
)

SELECT *
From tempr sub
WHERE sub.CounterProtocolos < (SELECT COUNT(p.NrProtocolo) FROM Protocolo p);
```
