# estudandoG2
dsg

No contexto da organização de eventos acadêmico-científicos autores podem submeter trabalhos (artigos) para avaliação, com o objetivo de serem aprovados após uma avaliação. Na avaliação de artigos são usados critérios de avaliação: a) Qualidade técnica; b) Inovação; c) Resultados; d) Metodologia; e) Adequação à temática do evento.

Uma avaliação de artigo é realizada por um avaliador de artigo, que pontua cada critério com um número de 1 (um) a 5 (cinco), com o primeiro correspondendo a insuficiente e o último a excelente. A pontuação do artigo em uma avaliação é a média aritmética das pontuações para os critérios. Um artigo pode receber mais de uma avaliação (nunca do mesmo avaliador). Desta forma, a pontuação final de um artigo é a média aritmética das suas pontuações.

Considere essa situação apresentada acima e implemente os requisitos a seguir, utilizando Framework Django Rest Framework. Crie uma API que permita:

 ao usuário Administrador:
(0,5) Cadastrar, recuperar atualizar um evento;
(0,5) Excluir um evento, desde que não exista inscritos e ou artigos associados ao evento;

ao usuário (Autor):
(0,5) Recuperar uma lista dos eventos.
(1,0) Realizar a submissão de um artigo em um evento;
(0,5) Excluir um artigo, desde que não exista uma avaliação para o mesmo;
(0,5) Recuperar somente os próprios artigos;

ao usuário Avaliador:
(1,0) Recuperar artigos de um evento que ele esteja associado como avaliador; 
(2,0) Realizar uma avaliação de um artigo dentro dos critérios estabelecidos
(0,5) Excluir uma avaliação de um artigo;
