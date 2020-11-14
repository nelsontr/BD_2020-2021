-- #### DROP TABLES ####
-- AUX TABLES
DROP TABLE nome_regiao CASCADE;
DROP TABLE tipo_instituicao CASCADE;
-- PRINCIPAL TABLES
DROP TABLE regiao CASCADE;
DROP TABLE concelho CASCADE;
DROP TABLE instituicao CASCADE;
DROP TABLE medico CASCADE;
DROP TABLE consulta CASCADE;
DROP TABLE prescricao CASCADE;
DROP TABLE analise CASCADE;
DROP TABLE venda_farmacia CASCADE;
DROP TABLE prescricao_venda CASCADE;

-- #### CREATE TABLES ####
-- AUXILIAR Tables
CREATE TABLE nome_regiao (
  nome varchar(8) NOT NULL UNIQUE PRIMARY KEY;
);
INSERT INTO nome_regiao VALUES
  ('Norte'), ('Centro'), ('Lisboa'), ('Alentejo'), ('Algarve');


CREATE TABLE tipo_instituicao (
  tipo varchar(11) PRIMARY KEY;
);
INSERT INTO tipo_instituicao VALUES
  ('farmacia'), ('laboratorio'), ('clinica'), ('hospital');

CREATE TABLE nome_concelho (
  nome varchar(24) NOT NULL UNIQUE PRIMARY KEY;
);

INSERT INTO nome_concelho VALUES
  ('ABRANTES'),
  ('AGUEDA'),
  ('AGUIARDABEIRA'),
  ('ALANDROAL'),
  ('ALBERGARIA-A-VELHA'),
  ('ALBUFEIRA'),
  ('ALCACERDOSAL'),
  ('ALCANENA'),
  ('ALCOBAÇA'),
  ('ALCOCHETE'),
  ('ALCOUTIM'),
  ('ALENQUER'),
  ('ALFANDEGADAFE'),
  ('ALIJO'),
  ('ALJEZUR'),
  ('ALJUSTREL'),
  ('ALMADA'),
  ('ALMEIDA'),
  ('ALMEIRIM'),
  ('ALMODOVAR'),
  ('ALPIARÇA'),
  ('ALTERDOCHÃO'),
  ('ALVAIAZERE'),
  ('ALVITO'),
  ('AMADORA'),
  ('AMARANTE'),
  ('AMARES'),
  ('ANADIA'),
  ('ANGRADOHEROISMO'),
  ('ANSIÃO'),
  ('ARCOSDEVALDEVEZ'),
  ('ARGANIL'),
  ('ARMAMAR'),
  ('AROUCA'),
  ('ARRAIOLOS'),
  ('ARRONCHES'),
  ('ARRUDADOSVINHOS'),
  ('AVEIRO'),
  ('AVIS'),
  ('AZAMBUJA'),
  ('BAIÃO'),
  ('BARCELOS'),
  ('BARRANCOS'),
  ('BARREIRO'),
  ('BATALHA'),
  ('BEJA'),
  ('BELMONTE'),
  ('BENAVENTE'),
  ('BOMBARRAL'),
  ('BORBA'),
  ('BOTICAS'),
  ('BRAGA'),
  ('BRAGANÇA'),
  ('CABECEIRASDEBASTO'),
  ('CADAVAL'),
  ('CALDASDARAINHA'),
  ('CALHETA(AÇORES)'),
  ('CALHETA(MADEIRA)'),
  ('CAMARADELOBOS'),
  ('CAMINHA'),
  ('CAMPOMAIOR'),
  ('CANTANHEDE'),
  ('CARRAZEDADEANSIÃES'),
  ('CARREGALDOSAL'),
  ('CARTAXO'),
  ('CASCAIS'),
  ('CASTANHEIRADEPERA'),
  ('CASTELOBRANCO'),
  ('CASTELODEPAIVA'),
  ('CASTELODEVIDE'),
  ('CASTRODAIRE'),
  ('CASTROMARIM'),
  ('CASTROVERDE'),
  ('CELORICODABEIRA'),
  ('CELORICODEBASTO'),
  ('CHAMUSCA'),
  ('CHAVES'),
  ('CINFÃES'),
  ('COIMBRA'),
  ('CONDEIXA-A-NOVA'),
  ('CONSTANCIA'),
  ('CORUCHE'),
  ('CORVO'),
  ('COVILHÃ'),
  ('CRATO'),
  ('CUBA'),
  ('ELVAS'),
  ('ENTRONCAMENTO'),
  ('ESPINHO'),
  ('ESPOSENDE'),
  ('ESTARREJA'),
  ('ESTREMOZ'),
  ('EVORA'),
  ('FAFE'),
  ('FARO'),
  ('FELGUEIRAS'),
  ('FERREIRADOALENTEJO'),
  ('FERREIRADOZEZERE'),
  ('FIGUEIRADAFOZ'),
  ('FIGUEIRADECASTELORODRIGO'),
  ('FIGUEIRODOSVINHOS'),
  ('FORNOSDEALGODRES'),
  ('FREIXODEESPADAACINTA'),
  ('FRONTEIRA'),
  ('FUNCHAL'),
  ('FUNDÃO'),
  ('GAVIÃO'),
  ('GOIS'),
  ('GOLEGÃ'),
  ('GONDOMAR'),
  ('GOUVEIA'),
  ('GRANDOLA'),
  ('GUARDA'),
  ('GUIMARÃES'),
  ('HORTA'),
  ('IDANHA-A-NOVA'),
  ('ILHAVO'),
  ('LAGOA(AÇORES)'),
  ('LAGOA(ALGARVE)'),
  ('LAGOS'),
  ('LAJESDASFLORES'),
  ('LAJESDOPICO'),
  ('LAMEGO'),
  ('LEIRIA'),
  ('LISBOA'),
  ('LOULE'),
  ('LOURES'),
  ('LOURINHÃ'),
  ('LOUSÃ'),
  ('LOUSADA'),
  ('MAÇÃO'),
  ('MACEDODECAVALEIROS'),
  ('MACHICO'),
  ('MADALENA'),
  ('MAFRA'),
  ('MAIA'),
  ('MANGUALDE'),
  ('MANTEIGAS'),
  ('MARCODECANAVESES'),
  ('MARINHAGRANDE'),
  ('MARVÃO'),
  ('MATOSINHOS'),
  ('MEALHADA'),
  ('MEDA'),
  ('MELGAÇO'),
  ('MERTOLA'),
  ('MESÃOFRIO'),
  ('MIRA'),
  ('MIRANDADOCORVO'),
  ('MIRANDADODOURO'),
  ('MIRANDELA'),
  ('MOGADOURO'),
  ('MOIMENTADABEIRA'),
  ('MOITA'),
  ('MONÇÃO'),
  ('MONCHIQUE'),
  ('MONDIMDEBASTO'),
  ('MONFORTE'),
  ('MONTALEGRE'),
  ('MONTEMOR-O-NOVO'),
  ('MONTEMOR-O-VELHO'),
  ('MONTIJO'),
  ('MORA'),
  ('MORTAGUA'),
  ('MOURA'),
  ('MOURÃO'),
  ('MURÇA'),
  ('MURTOSA'),
  ('NAZARE'),
  ('NELAS'),
  ('NISA'),
  ('NORDESTE'),
  ('OBIDOS'),
  ('ODEMIRA'),
  ('ODIVELAS'),
  ('OEIRAS'),
  ('OLEIROS'),
  ('OLHÃO'),
  ('OLIVEIRADEAZEMEIS'),
  ('OLIVEIRADEFRADES'),
  ('OLIVEIRADOBAIRRO'),
  ('OLIVEIRADOHOSPITAL'),
  ('OUREM'),
  ('OURIQUE'),
  ('OVAR'),
  ('PAÇOSDEFERREIRA'),
  ('PALMELA'),
  ('PAMPILHOSADASERRA'),
  ('PAREDES'),
  ('PAREDESDECOURA'),
  ('PEDROGÃOGRANDE'),
  ('PENACOVA'),
  ('PENAFIEL'),
  ('PENALVADOCASTELO'),
  ('PENAMACOR'),
  ('PENEDONO'),
  ('PENELA'),
  ('PENICHE'),
  ('PESODAREGUA'),
  ('PINHEL'),
  ('POMBAL'),
  ('PONTADELGADA'),
  ('PONTADOSOL'),
  ('PONTEDABARCA'),
  ('PONTEDELIMA'),
  ('PONTEDESOR'),
  ('PORTALEGRE'),
  ('PORTEL'),
  ('PORTIMÃO'),
  ('PORTO'),
  ('PORTODEMOS'),
  ('PORTOMONIZ'),
  ('PORTOSANTO'),
  ('POVOAÇÃO'),
  ('POVOADELANHOSO'),
  ('POVOADEVARZIM'),
  ('PROENÇA-A-NOVA'),
  ('REDONDO'),
  ('REGUENGOSDEMONSARAZ'),
  ('RESENDE'),
  ('RIBEIRABRAVA'),
  ('RIBEIRADEPENA'),
  ('RIBEIRAGRANDE'),
  ('RIOMAIOR'),
  ('S.BRASDEALPORTEL'),
  ('S.JOÃODAMADEIRA'),
  ('S.JOÃODAPESQUEIRA'),
  ('S.PEDRODOSUL'),
  ('S.ROQUEDOPICO'),
  ('S.VICENTE'),
  ('SABROSA'),
  ('SABUGAL'),
  ('SALVATERRADEMAGOS'),
  ('SANTACOMBADÃO'),
  ('SANTACRUZ'),
  ('SANTACRUZDAGRACIOSA'),
  ('SANTACRUZDASFLORES'),
  ('SANTAMARIADAFEIRA'),
  ('SANTAMARTADEPENAGUIÃO'),
  ('SANTANA'),
  ('SANTAREM'),
  ('SANTIAGODOCACEM'),
  ('SANTOTIRSO'),
  ('SARDOAL'),
  ('SATÃO'),
  ('SEIA'),
  ('SEIXAL'),
  ('SERNANCELHE'),
  ('SERPA'),
  ('SERTÃ'),
  ('SESIMBRA'),
  ('SETUBAL'),
  ('SEVERDOVOUGA'),
  ('SILVES'),
  ('SINES'),
  ('SINTRA'),
  ('SOBRALDEMONTEAGRAÇO'),
  ('SOURE'),
  ('SOUSEL'),
  ('TABUA'),
  ('TABUAÇO'),
  ('TAROUCA'),
  ('TAVIRA'),
  ('TERRASDEBOURO'),
  ('TOMAR'),
  ('TONDELA'),
  ('TORREDEMONCORVO'),
  ('TORRESNOVAS'),
  ('TORRESVEDRAS'),
  ('TRANCOSO'),
  ('TROFA'),
  ('VAGOS'),
  ('VALEDECAMBRA'),
  ('VALENÇA'),
  ('VALONGO'),
  ('VALPAÇOS'),
  ('VELAS'),
  ('VENDASNOVAS'),
  ('VIANADOALENTEJO'),
  ('VIANADOCASTELO'),
  ('VIDIGUEIRA'),
  ('VIEIRADOMINHO'),
  ('VILADEREI'),
  ('VILADOBISPO'),
  ('VILADOCONDE'),
  ('VILADOPORTO'),
  ('VILAFLOR'),
  ('VILAFRANCADEXIRA'),
  ('VILAFRANCADOCAMPO'),
  ('VILANOVADABARQUINHA'),
  ('VILANOVADECERVEIRA'),
  ('VILANOVADEFAMALICÃO'),
  ('VILANOVADEFOZCOA'),
  ('VILANOVADEGAIA'),
  ('VILANOVADEPAIVA'),
  ('VILANOVADEPOIARES'),
  ('VILAPOUCADEAGUIAR'),
  ('VILAPRAIADAVITORIA'),
  ('VILAREAL'),
  ('VILAREALDESANTOANTONIO'),
  ('VILAVELHADERODÃO'),
  ('VILAVERDE'),
  ('VILAVIÇOSA'),
  ('VIMIOSO'),
  ('VINHAIS'),
  ('VISEU'),
  ('VIZELA'),
  ('VOUZELA');

-- Principal Tables
CREATE TABLE regiao (
  num_regiao int PRIMARY KEY,
  nome varchar(8) NOT NULL UNIQUE,
  num_habitantes int,

  UNIQUE(num_regiao, nome),
  FOREIGN KEY (nome) REFERENCES nome_regiao(nome)
);


CREATE TABLE concelho (
  num_concelho int,
  num_regiao int,
  nome varchar(24),
  num_habitantes int,

  PRIMARY KEY (num_concelho, num_regiao),
  FOREIGN KEY (num_regiao) REFERENCES regiao(num_regiao),
  FOREIGN KEY (nome) REFERENCES nome_concelho(nome)
);


CREATE TABLE instituicao (
  nome varchar(255) PRIMARY KEY,
  tipo varchar(255) NOT NULL,
  num_regiao int NOT NULL,
  num_concelho int NOT NULL,

  FOREIGN KEY (num_concelho,num_regiao) REFERENCES concelho(num_concelho,num_regiao),
  FOREIGN KEY (tipo) REFERENCES tipo_instituicao(tipo)
);


CREATE TABLE medico (
  num_cedula int PRIMARY KEY,
  nome varchar(255),
  especialidade varchar(255)
);


CREATE TABLE consulta (
  num_cedula int,
  num_doente int,
  data varchar(255),
  nome_instituicao varchar(255),

  PRIMARY KEY (num_cedula, num_doente, data),
  FOREIGN KEY (num_cedula) REFERENCES medico(num_cedula),
  FOREIGN KEY (nome_instituicao) REFERENCES instituicao(nome)
  --RI-consulta-1: um médico não pode ver doentes ao fim de semana
  --RI-consulta-2: um doente não pode ter mais de uma consulta por dia na mesma instituição

);


CREATE TABLE prescricao (
  num_cedula int,
  num_doente int,
  data varchar(255),
  substancia varchar(255),
  quant int,

  PRIMARY KEY (num_cedula, num_doente, data, substancia),
  FOREIGN KEY (num_cedula, num_doente, data)
    REFERENCES consulta(num_cedula, num_doente, data)
);


CREATE TABLE analise (
  num_analise int PRIMARY KEY,
  especialidade varchar(255),
  num_cedula int,
  num_doente int,
  data varchar(255),
  data_registo varchar(255),
  nome varchar(255),
  quant int,
  inst varchar(255),

  FOREIGN KEY (num_cedula, num_doente, data)
    REFERENCES consulta(num_cedula, num_doente, data),
  FOREIGN KEY (inst) REFERENCES instituicao(nome)
  --RI: a consulta associada pode estar omissa; não estando, a especialidade da consulta tem de ser igual à do médico.
);


CREATE TABLE venda_farmacia (
  num_venda int,
  data_registo varchar(255),
  substancia varchar(255),
  quant int,
  preco int,
  inst varchar(255),

  PRIMARY KEY (num_venda),
  FOREIGN KEY (inst) REFERENCES instituicao(nome)
);


CREATE TABLE prescricao_venda (
  num_cedula int,
  num_doente int,
  data varchar(255),
  substancia varchar(255),
  num_venda int,

  PRIMARY KEY (num_cedula, num_doente, data, substancia, num_venda),
  FOREIGN KEY (num_cedula, num_doente, data, substancia)
    REFERENCES prescricao(num_cedula, num_doente, data, substancia)
);
