# 🧑‍💼 Análise de Perfil de Cliente por Agrupamento (Clusterização)

O objetivo deste projeto é clusterizar clientes de um shopping com base em sua renda anual e comportamento de compra. A partir dessa segmentação, foram criados perfis de marketing distintos para possibilitar o direcionamento de campanhas e estratégias de engajamento mais eficazes.

# 🚀 Tecnologias Utilizadas

**Análise e Modelagem**: Python, Pandas, Matplotlib, Seaborn, Scikit-learn

**Aplicação Web**: Streamlit

**Serialização do Modelo**: Pickle

# ⚙️ Pipeline do Projeto

O projeto seguiu o seguinte pipeline de ponta a ponta:

**Coleta** → **Limpeza** → **Análise Exploratória** → **Clusterização** → **Avaliação** → **Insights**

# 📊 Análise e Decisões de Modelagem

O notebook *main.ipynb* contém todo o processo de análise de dados e treinamento do modelo. As principais decisões técnicas foram:

**Seleção de Algoritmos**: Foram testados os algoritmos de clusterização KMeans e DBSCAN para identificar os agrupamentos naturais nos dados.

**Seleção de Features**: Após a análise de correlação e testes de hipóteses, o melhor desempenho foi alcançado utilizando as duas features mais relevantes: Renda Anual (Annual Income) e Índice de Gasto (Spending Score).

**Avaliação e Escolha do Modelo**: O KMeans apresentou o melhor desempenho. O número ideal de clusters (K) foi definido como 5, obtendo um coeficiente de silhueta de 0.57, o que indica uma boa separação entre os clusters.

# 🖼️ Principais Visualizações

Abaixo estão os gráficos mais importantes gerados durante a análise, que fundamentaram as conclusões do projeto.

1. **Clusterização de Clientes por Renda e Gasto**

Este gráfico de dispersão mostra a distribuição dos 5 clusters identificados pelo KMeans. Cada cor representa um perfil de cliente distinto, segmentado claramente com base na renda anual e no índice de gasto.

2. **Distribuição dos Perfis de Clientes**

O gráfico de pizza ilustra a proporção de cada perfil de cliente no dataset. O perfil "Regular" compõe a maior parte da base de clientes (45,2%), seguido pelo perfil "VIP" (17,5%).

3. **Relação entre Perfil, Idade e Gênero**

Este gráfico de barras analisa a média de idade para cada perfil, segmentado por gênero. Ele revela, por exemplo, que os perfis "Gastador Arriscado" e "VIP" são compostos por clientes mais jovens.

# 💡 Insights e Recomendações Finais

A análise dos 5 clusters revelou os seguintes perfis e recomendações estratégicas:

**VIP (17.5%)**:

**Insight**: Clientes de alta renda e alto gasto, com idade média de 32 anos. São o público-alvo ideal para produtos de luxo e programas de fidelidade exclusivos.

**Recomendação**: Campanhas de marketing direcionadas com ofertas premium, acesso antecipado a coleções e eventos exclusivos para manter o engajamento e a alta frequência de compra.

**Regular (45.2%)**:

**Insight**: O maior grupo de clientes, com renda e gastos moderados e idade média de 43 anos. Representam a base sólida do shopping.

**Recomendação**: Manter o engajamento através de programas de fidelidade, promoções gerais e comunicação sobre novidades para incentivar um aumento gradual no ticket médio.

**Econômico** (15.3%):

**Insight**: Possuem alta renda, mas baixo índice de gasto, com idade média de 43 anos. Têm potencial financeiro, mas são compradores cautelosos.

**Recomendação**: Campanhas focadas em custo-benefício, produtos de alta qualidade e durabilidade, ou itens de luxo específicos que possam despertar seu interesse de compra.

**Gastador Arriscado (11.3%)**:

**Insight**: Clientes jovens (idade média de 24 anos) com baixa renda, mas que gastam muito. São impulsivos e provavelmente sensíveis a tendências.

**Recomendação**: Oferecer promoções agressivas, descontos e opções de parcelamento. Marketing digital focado em redes sociais pode ser altamente eficaz com este grupo.

**Potencial (10.7%)**:

**Insight**: Baixa renda e baixo índice de gasto, com uma faixa etária mais elevada (média de 45 anos). São o grupo mais conservador.

**Recomendação**: Nutrir o relacionamento com ofertas de entrada e descontos progressivos para aumentar a confiança e o valor gasto ao longo do tempo.

# 💻 Como Usar a Aplicação Web (app.py)

A aplicação foi projetada para ser intuitiva e possui dois modos de operação, que podem ser selecionados na barra lateral.

**Modo 1: Analisar Perfil**

Esta é a funcionalidade principal, onde você pode prever o perfil de um novo cliente.

**Selecione o Modo**: Na barra lateral à esquerda, certifique-se de que a opção *"Analisar Perfil"* está selecionada.

**Insira os Dados do Cliente**:

**Idade**: Digite a idade do cliente.

**Renda Anual (U$)**: Insira o valor da renda anual em dólares (ex: 70000).

**Índice de Gasto**: Use o controle deslizante para definir o índice de gasto do cliente, que varia de 1 a 100.

**Execute a Análise**: Clique no botão *"Analisar Perfil"*.

**Visualize o Resultado**: A aplicação exibirá instantaneamente o perfil do cliente, utilizando um código de cores para destaque:

**Verde (Success)**: Para perfis de alto valor, como "VIP" e "Potencial".

**Amarelo (Warning)**: Para perfis neutros, como "Regular" e "Econômico".

**Vermelho (Error)**: Para o perfil "Gastador Arriscado", que pode exigir atenção.

**Modo 2: Perfis Analisados**

Este modo permite visualizar e gerenciar o histórico de todas as análises feitas na sessão atual da aplicação.

**Selecione o Modo**: Na barra lateral, mude a opção para *"Perfis Analisados"*.

**Visualize o Histórico**: Uma tabela aparecerá na tela principal, mostrando todos os clientes que você analisou, juntamente com seus dados de entrada e o perfil previsto.

**Gerenciar o Histórico**:

**Limpar histórico**: Se desejar apagar todos os registros da sessão, clique neste botão.

**Baixar Histórico**: Clique neste botão para fazer o download da tabela de perfis analisados como um arquivo Perfis Analisados.csv. Isso é útil para salvar os resultados e analisá-los posteriormente.

**Links Úteis (na Sidebar)**

A barra lateral também contém links diretos para o repositório do projeto, meu perfil no GitHub e no LinkedIn, além de uma galeria com outros projetos.

# 🔗 Link da Aplicação

