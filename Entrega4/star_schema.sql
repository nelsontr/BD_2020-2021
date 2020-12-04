DROP TABLE d_tempo CASCADE;
DROP TABLE d_instituicao CASCADE;
DROP TABLE f_analise CASCADE;
DROP TABLE f_presc_venda CASCADE;

CREATE TABLE d_tempo (
    id_tempo serial PRIMARY KEY,
    dia int,
    dia_da_semana int,
    semana int,
    mes int,
    trimestre int,
    ano int
);

CREATE TABLE d_instituicao (
    id_inst serial PRIMARY KEY,
    nome varchar(255),
    tipo varchar(11),
    num_regiao int,
    num_concelho int,

    FOREIGN KEY (nome) REFERENCES instituicao(nome),
    FOREIGN KEY (num_regiao) REFERENCES regiao(num_regiao),
    FOREIGN KEY (num_concelho) REFERENCES concelho(num_concelho)
);

CREATE TABLE f_presc_venda (
    id_presc_venda int PRIMARY KEY,
    id_medico int,
    num_doente int,
    id_data_registo int,
    id_inst int,
    substancia varchar(255),
    quant int,

    FOREIGN KEY (id_presc_venda) REFERENCES prescricao_venda(num_venda),
    FOREIGN KEY (id_medico) REFERENCES medico(num_cedula),
    FOREIGN KEY (id_data_registo) REFERENCES d_tempo(id_tempo),
    FOREIGN KEY (id_inst) REFERENCES d_instituicao(id_inst)
);

CREATE TABLE f_analise (
    id_analise int PRIMARY KEY,
    id_medico int,
    num_doente int,
    id_data_registo int,
    id_inst int,
    nome varchar(255),
    quant int,

    FOREIGN KEY (id_analise) REFERENCES analise(num_analise),
    FOREIGN KEY (id_data_registo) REFERENCES d_tempo(id_tempo),
    FOREIGN KEY (id_inst) REFERENCES d_instituicao(id_inst)
);
