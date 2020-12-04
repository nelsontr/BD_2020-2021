alter table regiao drop constraint regiao_nome_fkey;
alter table regiao add constraint regiao_nome_fkey foreign key(nome)
  references nome_regiao(nome) on update cascade on delete cascade;

alter table concelho drop constraint concelho_nome_fkey;
alter table concelho add constraint concelho_nome_fkey foreign key(nome)
  references nome_concelho(nome) on update cascade on delete cascade;
alter table concelho drop constraint concelho_num_regiao_fkey;
alter table concelho add constraint concelho_num_regiao_fkey foreign key(num_regiao)
  references regiao(num_regiao) on update cascade on delete cascade;

alter table instituicao drop constraint instituicao_num_concelho_num_regiao_fkey;
alter table instituicao add constraint instituicao_num_concelho_num_regiao_fkey foreign key(num_concelho,num_regiao)
  references concelho(num_concelho,num_regiao) on update cascade on delete cascade;
alter table instituicao drop constraint instituicao_tipo_fkey;
alter table instituicao add constraint instituicao_tipo_fkey foreign key(tipo)
  references tipo_instituicao(tipo) on update cascade on delete cascade;

alter table consulta drop constraint consulta_num_cedula_fkey;
alter table consulta add constraint consulta_num_cedula_fkey foreign key(num_cedula)
  references medico(num_cedula) on update cascade on delete cascade;

alter table consulta drop constraint consulta_nome_instituicao_fkey;
alter table consulta add constraint consulta_nome_instituicao_fkey foreign key(nome_instituicao)
  references instituicao(nome) on update cascade on delete cascade;

alter table prescricao drop constraint prescricao_num_cedula_num_doente_data_fkey;
alter table prescricao add constraint prescricao_num_cedula_num_doente_data_fkey foreign key(num_cedula, num_doente, data)
  references consulta(num_cedula, num_doente, data) on update cascade on delete cascade;

alter table analise drop constraint analise_num_cedula_num_doente_data_fkey;
alter table analise add constraint analise_num_cedula_num_doente_data_fkey foreign key(num_cedula, num_doente, data)
  references consulta(num_cedula, num_doente, data) on update cascade on delete cascade;
alter table analise drop constraint analise_inst_fkey;
alter table analise add constraint analise_inst_fkey foreign key(inst)
  references instituicao(nome) on update cascade on delete cascade;

alter table venda_farmacia drop constraint venda_farmacia_inst_fkey;
alter table venda_farmacia add constraint venda_farmacia_inst_fkey foreign key(inst)
  references instituicao(nome) on update cascade on delete cascade;

alter table prescricao_venda drop constraint prescricao_venda_num_cedula_num_doente_data_substancia_fkey;
alter table prescricao_venda add constraint prescricao_venda_num_cedula_num_doente_data_substancia_fkey foreign key(num_cedula, num_doente, data, substancia)
  references prescricao(num_cedula, num_doente, data, substancia) on update cascade on delete cascade;
