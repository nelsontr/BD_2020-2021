-- ################################################################################################
--  GRUPO 50
--    93695 Catarina Sofia dos Santos Sousa 33% 5h
--    93743 Nelson Alexandre Geada Trindade 34% 5h
--    93754 Rodrigo Rodrigues Major 33% 5h
-- ################################################################################################


-- ################################################################################################
-- #######################################  DROP TABLES  ##########################################
-- ################################################################################################
-- AUX TABLES
DROP TABLE nome_concelho CASCADE;
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

-- ################################################################################################
-- #####################################  CREATE TABLES  ##########################################
-- ################################################################################################
-- AUXILIAR Tables
CREATE TABLE nome_concelho ( nome varchar(24) NOT NULL UNIQUE PRIMARY KEY );
CREATE TABLE nome_regiao ( nome varchar(8) NOT NULL UNIQUE PRIMARY KEY );
CREATE TABLE tipo_instituicao ( tipo varchar(11) PRIMARY KEY );

REVOKE ALL PRIVILEGES ON Table nome_concelho FROM public;
REVOKE ALL PRIVILEGES ON Table nome_regiao FROM public;
REVOKE ALL PRIVILEGES ON Table tipo_instituicao FROM public;


-- Principal Tables
CREATE TABLE regiao (
  num_regiao int PRIMARY KEY,
  nome varchar(8) NOT NULL UNIQUE,
  num_habitantes double precision,

  UNIQUE(num_regiao, nome),
  FOREIGN KEY (nome) REFERENCES nome_regiao(nome)
);



CREATE TABLE concelho (
  num_concelho int UNIQUE,
  num_regiao int,
  nome varchar(24),
  num_habitantes double precision,

  PRIMARY KEY (num_concelho, num_regiao),
  FOREIGN KEY (num_regiao) REFERENCES regiao(num_regiao),
  FOREIGN KEY (nome) REFERENCES nome_concelho(nome)
);

REVOKE ALL PRIVILEGES ON Table regiao FROM public;
REVOKE ALL PRIVILEGES ON Table concelho FROM public;


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

  CHECK (EXTRACT(ISODOW from data) < 6), --RI-consulta-1
  UNIQUE (num_doente, data, nome_instituicao), --RI-consulta-2

  PRIMARY KEY (num_cedula, num_doente, data),
  FOREIGN KEY (num_cedula) REFERENCES medico(num_cedula),
  FOREIGN KEY (nome_instituicao) REFERENCES instituicao(nome)
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
  --RI: a consulta associada pode estar omissa; não estando,
  -- a especialidade da consulta tem de ser igual à do médico.
);



CREATE TABLE venda_farmacia (
  num_venda int PRIMARY KEY,
  data_registo date,
  substancia varchar(255),
  quant int,
  preco int,
  inst varchar(255),

  FOREIGN KEY (inst) REFERENCES instituicao(nome)
);



CREATE TABLE prescricao_venda (
  num_cedula int,
  num_doente int,
  data date,
  substancia varchar(255),
  num_venda int UNIQUE,

  PRIMARY KEY (num_cedula, num_doente, data, substancia, num_venda),
  FOREIGN KEY (num_cedula, num_doente, data, substancia)
    REFERENCES prescricao(num_cedula, num_doente, data, substancia)
);