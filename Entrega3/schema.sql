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
  nome varchar(8) NOT NULL UNIQUE PRIMARY KEY
);
INSERT INTO nome_regiao VALUES
  ('Norte'), ('Centro'), ('Lisboa'), ('Alentejo'), ('Algarve');

CREATE TABLE tipo_instituicao (
  tipo varchar(11) PRIMARY KEY
);
INSERT INTO tipo_instituicao VALUES
  ('farmacia'), ('laboratorio'), ('clinica'), ('hospital');

CREATE TABLE nome_concelho (
  nome varchar(24) NOT NULL UNIQUE PRIMARY KEY;
);
--INSERT

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
  tipo varchar(11) NOT NULL,
  num_regiao int NOT NULL,
  num_concelho int NOT NULL,

  FOREIGN KEY (num_concelho,num_regiao) REFERENCES concelho(num_concelho,num_regiao),
  FOREIGN KEY (tipo) REFERENCES tipo_instituicao(tipo)
);


CREATE TABLE medico (
  num_cedula int PRIMARY KEY,
  nome varchar(255),
  especialidade varchar(25)
);


CREATE TABLE consulta (
  num_cedula int,
  num_doente int,
  data date,
  nome_instituicao varchar(255),

  CHECK (EXTRACT(DOW from data) < 6.0),
  PRIMARY KEY (num_cedula, num_doente, data),
  FOREIGN KEY (num_cedula) REFERENCES medico(num_cedula),
  FOREIGN KEY (nome_instituicao) REFERENCES instituicao(nome)
  
  --RI-consulta-2: um doente não pode ter mais de uma consulta por dia na mesma ins tuição
);


CREATE TABLE prescricao (
  num_cedula int,
  num_doente int,
  data date,
  substancia varchar(255),
  quant int,

  PRIMARY KEY (num_cedula, num_doente, data, substancia),
  FOREIGN KEY (num_cedula, num_doente, data)
    REFERENCES consulta(num_cedula, num_doente, data)
);


CREATE TABLE analise (
  num_analise int PRIMARY KEY,
  especialidade varchar(25),
  num_cedula int,
  num_doente int,
  data date,
  data_registo date,
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
  data_registo date,
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
  data date,
  substancia varchar(255),
  num_venda int,

  PRIMARY KEY (num_cedula, num_doente, data, substancia, num_venda),
  FOREIGN KEY (num_cedula, num_doente, data, substancia)
    REFERENCES prescricao(num_cedula, num_doente, data, substancia)
);
