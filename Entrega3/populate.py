import random
import datetime

f = open('populate-aux.sql','w')

# set values

nr_inst = 10
nr_medicos = 30
nr_doentes = 30
nr_consultas = 100
nr_ano_max = 2020
nr_ano_min = 2015
qt_substancia = 1000
nr_analises = 40
nr_prescricoes = 0 #alterado no create_prescricao
nr_vendas = 120
preco_max = 10.00
nr_vendas_prescicoes = 0 #alterado no prescricao_venda

tipos =  ['farmacia', 'laboratorio', 'clinica', 'hospital']
especialidades = ['otorrino', 'pediatra', 'cirurgiao']
substancias = ['aspirina','cannabis', 'ibuprofeno', 'paracetamol', 'maxilase', 'viagra', 'stepfen', 'calcitrin', 'cogumelos do tempo']
concelhos = {'1':2,'2':2,'3':1,'4':4,'5':2,'6':5,'7':3,'8':2,'9':2,'10':3,'11':5,'12':3,'13':1,'14':1,'15':5,'16':4,'17':3,'18':1,'19':2,'20':4,'21':2,'22':4,'23':2,'24':4,'25':3,'26':1,'27':1,'28':2,'29':0,'30':2,'31':1,'32':2,'33':1,'34':2,'35':4,'36':4,'37':3,'38':2,'39':4,'40':3,'41':1,'42':1,'43':4,'44':3,'45':2,'46':4,'47':2,'48':2,'49':2,'50':4,'51':1,'52':1,'53':1,'54':1,'55':3,'56':2,'57':0,'58':0,'59':0,'60':1,'61':4,'62':2,'63':1,'64':1,'65':2,'66':3,'67':2,'68':2,'69':2,'70':4,'71':1,'72':5,'73':4,'74':1,'75':1,'76':2,'77':1,'78':1,'79':2,'80':2,'81':2,'82':2,'83':0,'84':2,'85':4,'86':4,'87':4,'88':2,'89':2,'90':1,'91':2,'92':4,'93':4,'94':1,'95':5,'96':1,'97':4,'98':2,'99':2,'100':1,'101':2,'102':1,'103':1,'104':4,'105':0,'106':2,'107':4,'108':2,'109':2,'110':1,'111':1,'112':3,'113':1,'114':1,'115':0,'116':2,'117':2,'118':0,'119':5,'120':5,'121':0,'122':0,'123':1,'124':2,'125':3,'126':5,'127':3,'128':3,'129':2,'130':1,'131':2,'132':1,'133':0,'134':0,'135':3,'136':1,'137':1,'138':1,'139':1,'140':2,'141':4,'142':1,'143':2,'144':1,'145':1,'146':4,'147':1,'148':2,'149':2,'150':1,'151':1,'152':1,'153':1,'154':3,'155':1,'156':5,'157':1,'158':4,'159':1,'160':4,'161':2,'162':3,'163':4,'164':1,'165':4,'166':4,'167':1,'168':2,'169':2,'170':1,'171':4,'172':0,'173':2,'174':4,'175':3,'176':3,'177':2,'178':5,'179':2,'180':1,'181':2,'182':2,'183':2,'184':4,'185':2,'186':1,'187':3,'188':2,'189':1,'190':1,'191':2,'192':2,'193':1,'194':1,'195':2,'196':1,'197':2,'198':2,'199':1,'200':1,'201':2,'202':0,'203':0,'204':1,'205':1,'206':4,'207':4,'208':4,'209':5,'210':1,'211':2,'212':0,'213':0,'216':0,'214':1,'215':1,'217':2,'218':4,'219':4,'220':1,'221':0,'222':1,'223':0,'224':2,'225':5,'226':2,'227':1,'228':1,'229':0,'230':0,'231':1,'232':1,'233':2,'234':1,'235':0,'236':0,'237':0,'238':2,'239':1,'240':0,'241':2,'242':3,'243':1,'244':2,'245':1,'246':1,'247':3,'248':1,'249':4,'250':2,'251':3,'252':3,'253':2,'254':5,'255':3,'256':3,'257':3,'258':2,'259':4,'260':2,'261':1,'262':1,'263':5,'264':1,'265':2,'266':1,'267':1,'268':2,'269':3,'270':1,'271':1,'272':2,'273':2,'274':1,'275':1,'276':1,'277':0,'278':4,'279':4,'280':1,'281':4,'282':1,'283':2,'284':5,'285':1,'286':0,'287':1,'288':3,'289':0,'290':2,'291':1,'292':1,'293':1,'294':1,'295':1,'296':2,'297':1,'298':0,'299':1,'300':5,'301':2,'302':1,'303':4,'304':1,'305':1,'306':1,'307':1,'308':1}

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
        num_concelho = random.randint(1, 305)
        num_regiao = concelhos[str(num_concelho)]

        if tipo == 'farmacia':
            farmacias.append(nome)
        else:
            inst_names.append(nome)
        query += "  ('{}','{}',{},{}),\n".format(nome, tipo, num_regiao, num_concelho)

    query = query[:-2]
    query += ';\n\n'
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

        query += "  ({},'{}','{}'),\n".format(cedula, nome, especialidade)

    query = query[:-2]
    query += ';\n\n'
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
            query += "  ({},{},'{}','{}'),\n".format(medico , doente, d, i)

    query = query[:-2]
    query += ';\n\n'
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

        print([substancia,qtd])
        substancias_pres.append([substancia,qtd])
        query += "  ({},{},'{}', '{}', {}),\n".format(cedula, doente, data, substancia, qtd)

    query = query[:-2]
    query += ';\n\n'
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
        quant = x
        inst = random.choice(inst_names)

        query += "  ({},'{}',{},{},'{}','{}','{}',{},'{}'),\n".format(analise, especialidade, cedula, doente, data, data_registo, nome, quant, inst)
        
    query = query[:-2]
    query += ';\n\n'
    f.write(query)

def create_venda_farmacia():
    query = 'INSERT INTO venda_farmacia (num_venda, data_registo, substancia, quant, preco, inst) VALUES\n'

    subs_pres = []

    for x in range(0, nr_vendas):
        venda = x+1
        data_registo = Data(2020,11,16)
        if x < len(substancias_pres):
            ya = substancias_pres[x]
            subs = ya[0]
            qtd = ya[1]
            vendas_subs.append([subs,venda])
            print([subs,venda])
        else:
            subs = random.choice(substancias)
            qtd = random.randint(1,qt_substancia)

        
        preco = random.uniform(0.00, preco_max)
        inst = random.choice(farmacias)

        vendas.append(venda)
        query += "  ({},'{}','{}',{},{:.2f},'{}'),\n".format(venda, data_registo, subs, qtd, preco, inst)
        
    query = query[:-2]
    query += ';\n\n'
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
            query += "  ({},{},'{}','{}',{}),\n".format(cedula, doente, data, substancia, venda)

    query = query[:-2]
    query += ';\n\n'
    f.write(query)


create_instituicoes()
create_medicos()
create_consultas()
create_prescricao()
print()
create_analise()
create_venda_farmacia()
create_prescricao_venda()