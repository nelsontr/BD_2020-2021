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



Consulta (***#Cédula, Data, Hora, ID, #numero***, especialidade) {

​	#Cédula: FK(Médico)

​	Data, Hora: FK(Agenda.Data, Agenda.Hora)

​	ID, #numero: FK(ActoMédico.ID, ActoMédico.#numero)

}

Protocolo(*NºProtocolo*, data de homologação, descrição) 

AnáliseLab(*ID*) {

​	ID: FK(Medição)

}

TemplateAnalise(***NºProtocolo, Nome, Morada, ID***){
    
    NºProtocolo: FK(Protocolo)
    
    Nome, Morada: FK(Instituição.Nome, Instituição.Morada)
    
    ID: FK(AnáliseLab)
}

#TODO -> COLOCAR IDAtoMedico = AtoMédico.ID

Validado(***Nome, Morada, NºProtocolo, IDTemplateAnálise***, #numero, IDAtoMedico){
    Nome, Morada, NºProtocolo, IDTemplateAnálise: FK(TemplateAnálise.Nome, TemplateAnálise.Morada, TemplateAnálise.NºProtocolo, TemplateAnálise.ID)
    #numero, IDAtoMedico NOT NULL
}

Faz(#cédula, NºProtocolo, Nome, Morada, ID***){
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


