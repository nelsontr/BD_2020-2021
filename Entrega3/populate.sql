--####  ADDING DATA  ####
INSERT INTO instituicao (nome, tipo, num_regiao, num_concelho) VALUES
  ();


INSERT INTO medico (num_cedula, nome, especialidade) VALUES
  ();


INSERT INTO consulta (num_cedula, num_doente, data, nome_instituicao) VALUES
  ();


INSERT INTO prescricao (num_cedula, num_doente, data, substancia, quant) VALUES
  ();

INSERT INTO analise 
(num_analise, especialidade, num_cedula, num_doente, data, data_registo, nome, quant, inst)
  VALUES ();


INSERT INTO venda_farmacia (num_venda, data_registo, substancia, quant, preco, inst)
  VALUES ();



INSERT INTO prescricao_venda (num_cedula, num_doente, data, substancia, num_venda)
  VALUES ();
