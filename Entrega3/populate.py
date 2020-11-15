import random
import datetime

f = open('populate.sql','w')

# set values

nr_inst = 10
nr_medicos = 30
nr_doentes = 50
nr_consultas = 100
nr_ano_max = 2020
nr_ano_min = 2015
qt_substancia = 1000
nr_analises = 40
nr_prescricoes = 0 #alterado no create_prescricao
nr_vendas = 60
preco_max = 10.00
nr_vendas_prescicoes = 0 #alterado no prescricao_venda

tipos =  ['farmacia', 'laboratorio', 'clinica', 'hospital']
especialidades = ['otorrino', 'pediatra', 'cirurgiao']
substancias = ['aspirina','cannabis', 'ibuprofeno', 'paracetamol', 'maxilase', 'viagra', 'stepfen', 'calcitrin', 'cogumelos do tempo']

#fk
farmacias = []
inst_names = []
medico_cels = {}
consultas_pres = []
substancias_pres = []
vendas = []
vendas_subs = []

class Data:
    def __init__(self,ano,mes,dia):
        self.ano = ano
        self.mes = mes
        self.dia = dia
        self.weekday = datetime.datetime(ano, mes, dia, 0, 0, 1, 1).weekday()

    def __repr__(self):
        return '{}-{}-{}'.format(self.ano,self.mes,self.dia)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.ano == other.ano and self.mes == other.mes and self.dia == other.dia
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)


def create_instituicoes():
    query = 'INSERT INTO instituicao (nome, tipo, num_regiao, num_concelho) VALUES\n'
    regioes = 5
    conselhos = 305
    #integrity constraint
    for x in range(1,nr_inst+1):
        nome = str(x)
        tipo = random.choice(tipos)
        num_regiao = random.randint(1, 5)
        num_concelho = random.randint(1, 305)

        if tipo == 'farmacia':
            farmacias.append(nome)
        else:
            inst_names.append(nome)
        query += "('{}','{}',{},{}),\n".format(nome, tipo, num_regiao, num_concelho)

    query += '();\n'
    f.write(query)



def create_medicos():
    query = 'INSERT INTO medico (num_cedula, nome, especialidade) VALUES\n'

    for x in range(1,nr_medicos+1):
        cedula = x
        nome = 'nome ' + str(x)
        especialidade = random.choice(especialidades)

        if not cedula in medico_cels:
            medico_cels[cedula] = []
        medico_cels[cedula].append(especialidade)

        query += "({},'{}','{}'),\n".format(cedula, nome, especialidade)

    query += '();\n'
    f.write(query)



def create_consultas():
    query = 'INSERT INTO consulta (num_cedula, num_doente, data, nome_instituicao) VALUES\n'
    
    mes_dia = [31,28,31,30,31,30,31,31,30,31,30,31]

    query_list = []
    medicos = list(medico_cels.keys())
    for x in range(1,nr_consultas+1):
        dont_add = False
        medico = random.choice(medicos)
        doente = random.randint(1, nr_doentes)
        mes = random.randint(1, 12)
        d = Data(random.randint(nr_ano_min, nr_ano_max),mes,random.randint(1, mes_dia[mes-1]))
        i = random.choice(inst_names)

        #1st integrity constraint
        if d.weekday >= 5:
            dont_add = True

        #2nd integrity constraint
        if not (dont_add):
            for y in query_list:
                if doente == y[0] and d == y[1] and i == y[2]:
                    dont_add = True
        

        if not (dont_add):
            query_list.append([doente,d,i])
            consultas_pres.append([medico, doente, d])
            query += "({},{},'{}','{}'),\n".format(medico , doente, d, i)

    query += '();\n'
    f.write(query)


def create_prescricao():
    query = 'INSERT INTO prescricao (num_cedula, num_doente, data, substancia, quant) VALUES\n'

    global nr_prescricoes
    nr_prescricoes = random.randint(1,len(consultas_pres))

    for x in range(0, nr_prescricoes):
        cedula = consultas_pres[x][0]
        doente = consultas_pres[x][1]
        data = consultas_pres[x][2]
        substancia = random.choice(substancias)
        qtd = random.randint(1,qt_substancia)

        substancias_pres.append([substancia,qtd])
        query += "({},{},'{}', '{}', {}),\n".format(cedula, doente, data, substancia, qtd)

    query += '();\n'
    f.write(query)


def create_analise():
    query = 'INSERT INTO analise (num_analise, especialidade, num_cedula, num_doente, data, data_registo, nome, quant, inst) VALUES\n'

    for x in range (0, nr_analises):
        consulta = random.randint(0, len(consultas_pres)-1)
        medico = consultas_pres[consulta][0]
        
        analise = x
        # integrity constraint
        especialidade = medico_cels[medico][0]
        cedula = medico
        doente = consultas_pres[consulta][1]
        data = consultas_pres[consulta][2]
        data_registo = data
        nome = 'nome ' + str(x)
        quant = 'qtd ' + str(x)
        inst = random.choice(inst_names)

        query += "({},'{}',{},{},'{}','{}','{}','{}','{}'),\n".format(analise, especialidade, cedula, doente, data, data_registo, nome, quant, inst)
        
    query += '();\n'
    f.write(query)

def create_venda_farmacia():
    query = 'INSERT INTO venda_farmacia (num_venda, data_registo, substancia, quant, preco, inst) VALUES\n'

    subs_pres = []

    for x in range(0, nr_vendas):
        venda = x+1
        data_registo = Data(2020,11,15)
        if not substancias_pres == []:
            ya = random.choice(substancias_pres)
            subs = ya[0]
            qtd = ya[1]
            substancias_pres.remove(ya)
            vendas_subs.append([subs,venda])
        else:
            subs = random.choice(substancias)
            qtd = random.randint(1,qt_substancia)

        
        preco = random.uniform(0.00, preco_max)
        inst = random.choice(farmacias)

        vendas.append(venda)
        query += "({},'{}','{}',{},{:.2f},{}),\n".format(venda, data_registo, subs, qtd, preco, inst)
        
    query += '();\n'
    f.write(query)

def create_prescricao_venda():
    query = 'INSERT INTO prescricao_venda (num_cedula, num_doente, data, substancia, num_venda) VALUES\n'
    
    nr_vendas_prescicoes = random.randint(1,min(nr_vendas, nr_prescricoes))
    
    feitas = []
    for x in range(0, nr_vendas_prescicoes):
        cedula = consultas_pres[x][0]
        doente = consultas_pres[x][1]
        data = consultas_pres[x][2]
        substancia = vendas_subs[x][0]
        venda = vendas_subs[x][1]
        
        if not venda in feitas:
            feitas.append(venda)
            query += "({},{},'{}','{}',{}),\n".format(cedula, doente, data, substancia, venda)

    query += '();\n'
    f.write(query)


create_instituicoes()
create_medicos()
create_consultas()
create_prescricao()
create_analise()
create_venda_farmacia()
create_prescricao_venda()