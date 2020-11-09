CREATE TABLE regiao (
  regiaoregiaoregiaoregiao int,
  nome varchar(255),
  num_habitantes int,
  
  PRIMARY KEY (num_regiao),
  --FOREIGN KEY (y) REFERENCES X(ID)
  --VER RESTRIÇÃO
);


CREATE TABLE concelho (
  num_concelho int,
  num_regiao int,
  nome varchar(255),
  num_habitantes int,

  PRIMARY KEY (num_concelho, num_regiao),
  FOREIGN KEY (num_regiao) REFERENCES regiao(regiao)
  --VER RESTRIÇÃO
);


CREATE TABLE instituicao (
  nome varchar(255),
  tipo varchar(255),
  num_regiao int,
  num_concelho int,

  PRIMARY KEY (nome),
  FOREIGN KEY (num_regiao) REFERENCES concelho(num_regiao),
  FOREIGN KEY (num_concelho) REFERENCES concelho(num_concelho)
  --VER RESTRIÇÃO
);


CREATE TABLE medico (
  num_cedula int,
  nome varchar(255),
  especialidade varchar(255),

  PRIMARY KEY (num_cedula)
);


CREATE TABLE consulta (
  num_cedula int,
  num_doente int,
  data varchar(255),
  nome_instituicao varchar(255),

  PRIMARY KEY (num_cedula, num_doente, data),
  FOREIGN KEY (num_cedula) REFERENCES medico(num_cedula),
  FOREIGN KEY (nome_instituicao) REFERENCES instituicao(nome)
  --VER RESTRIÇÃO
);


CREATE TABLE prescricao (
  num_cedula int,
  num_doente int,
  data varchar(255),
  substancia varchar(255),
  quant int,

  PRIMARY KEY (num_cedula, num_doente, data, substancia),
  FOREIGN KEY (num_cedula) REFERENCES consulta(num_cedula),
  FOREIGN KEY (num_doente) REFERENCES consulta(num_doente),
  FOREIGN KEY (data) REFERENCES consulta(data)
);


CREATE TABLE analise (
  num_analise int,
  especialidade varchar(255),
  num_cedula int,
  num_doente int,
  data varchar(255),
  data_registo varchar(255),
  nome varchar(255),
  quant int,
  inst varchar(255),

  PRIMARY KEY (num_analise),
  FOREIGN KEY (num_cedula) REFERENCES consulta(num_cedula),
  FOREIGN KEY (num_doente) REFERENCES consulta(num_doente),
  FOREIGN KEY (data) REFERENCES consulta(data),
  FOREIGN KEY (inst) REFERENCES instituicao(nome)
  --VER RESTRIÇÃO
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
  FOREIGN KEY (num_venda) REFERENCES venda_farmacia(num_venda),
  FOREIGN KEY (num_cedula) REFERENCES prescricao(num_cedula),
  FOREIGN KEY (num_doente) REFERENCES prescricao(num_doente),
  FOREIGN KEY (data) REFERENCES prescricao(data),
  FOREIGN KEY (substancia) REFERENCES prescricao(substancia)
);
