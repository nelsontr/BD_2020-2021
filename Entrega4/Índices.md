## ÍNDICES

#### Query 1: 

​	-> Não é necessário criar nenhum índice porque é criado implicitamente para as chaves primárias. 
Assim, apenas é preciso alterar a ordem dos campos das chaves primárias na declaração da tabela consulta para que o num_doente seja o primeiro atributo. Concluindo, o índice criado para a chave primária é o único necessário para acelerar a execução desta query;

#### Query 2:

​	Provavelmente, índice do tipo Hash:

​	São os melhores para seleção por igualdade;

​	Há uma estrutura;
 
 Criar um índice do tipo Hash para o atributo especialidade da tabela medico porque fica dividido            
 por vários contentores e assim cada contentor guarda um conjunto de entradas e o acesso fica otimizado 
 através da função de dispersão.

#### Query 3:
Blocos do disco são de 2KBytes e cada registo ocupa 1kByte, ou seja, cada bloco leva 2 registos. Seletividade de (1/6) = 0.16666667 ou seja, a probabilidade de um bloco não ter respostas é de (1-0.16666667)^2 (por serem dois registos por bloco), que é aproximadamente 69%. Logo, teremos de ler 31% dos blocos. Quanto menor for a resposta, maior é o benefício dos índices a reduzir leituras do disco. Assim, é útil, criar um índice.
(???) do tipo Hash na tabela medico no atributo especialidade:
CREATE INDEX index_especialidade ON medico(especialidade)

​	Provavelmente, índice do tipo Hash:

​	São os melhores para seleção por igualdade;

​	Há uma estrutura;
 
 Criar um índice do tipo Hash para o atributo especialidade da tabela medico porque fica dividido            
 por vários contentores e assim cada contentor guarda um conjunto de entradas e o acesso fica otimizado 
 através da função de dispersão.
 
 

#### Query 4:
​	São criados índices implicitamente para as primary keys e assim, pode ser utilizado neste caso para acelerar a execução desta query, uma vez que o atributo num_cedula é o primeiro atributo da chave primária na declaração da tabela consulta. Se o atributo num_cedula não fosse o primeiro da chave primária, então tinhamos de alterar a ordem dos campos das chaves primárias.

​	Para além deste índice, deve-se criar um índice do tipo BTree para o atributo "data" da tabela consulta para otimizar a comparação entre as duas datas dadas. Este tipo de índice é o apropriado para acelerar esta query porque as folhas do índice estão sempre ordenadas, o que facilita a comparação entre as datas:
	CREATE INDEX idx_data on consulta USING B-TREE(data)

	
