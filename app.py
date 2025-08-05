import streamlit as st
import pickle
import pandas as pd

# importando o modelo
with open("KMeans Model.pkl", "rb") as f:
    modelo = pickle.load(f)

with st.sidebar:
    st.header('Options')
    options = st.selectbox("Modo", ['Analisar Perfil', 'Perfis Analisados'])
    st.markdown("### 🔗 Links Úteis")
    st.markdown("[📁 Este Projeto]()")
    st.markdown("[👨‍💻 Meu GitHub](https://github.com/IvandroMacheque/IvandroMacheque.git)")
    st.markdown("[💼 Meu LinkedIn](https://www.linkedin.com/in/ivandromacheque?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)")
    st.markdown("[🗂️ Outros Projetos](https://machequeivandro.notion.site/21c3f356a4b180d3a221ede7e8f1a0a3)")

# criar historico de clientes previstos
if "analisados" not in st.session_state:
    st.session_state.analisados = pd.DataFrame()

if options == 'Analisar Perfil':
    st.title("🧑‍💼 Customer Profile Prediction")

    st.write("## Insira os Dados do Cliente")

    # configurando os inputs
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Idade")
    with col2:
        annual_income_k = st.number_input("Renda Anual (U$)")
        annual_income = annual_income_k / 1000
    spending_score = st.slider("Índice de Gasto", 1, 100, 50)

    # criar o dataset para o modelo
    dataframe_modelo = {'Annual Income (k$)': annual_income,
                'Spending Score (1-100)': spending_score,}
    dados_do_modelo = pd.DataFrame(dataframe_modelo, index=[0])

    def clusterizar():
        # analisando os dados do input e normalizando
        Perfil = modelo.predict(dados_do_modelo)
        if Perfil == 0.0:
            Perfil = 'Regular'
        elif Perfil == 1.0:
            Perfil = 'Potencial'
        elif Perfil == 2.0:
            Perfil = 'VIP'
        elif Perfil == 3.0:
            Perfil = 'Econômico'
        else:
            Perfil = 'Gastador Arriscado'

        # dados gerais
        data = {'Age': age,
            'Annual Income (k$)': annual_income,
            'Spending Score (1-100)': spending_score,
            'Perfil': Perfil}
        dados = pd.DataFrame(data, index=[0])
        st.session_state.analisados = pd.concat([st.session_state.analisados, dados], ignore_index=True)

        # exibindo os resultados
        with container:
            if Perfil == 'Gastador Arriscado':
                st.error(f"O Cliente inserido é um {Perfil}")
            elif Perfil == 'Regular' or Perfil == 'Econômico':
                st.warning(f"O Cliente inserido é um Cliente {Perfil}")
            else:
                st.success(f"O Cliente inserido é um Cliente {Perfil}")

    container = st.container()
    st.button("Analisar Perfil", on_click=clusterizar)
else:

    st.title("🧑‍💼📜 Perfis Analisados")
    # visualizacao do histórico de previsão 
    st.dataframe(st.session_state.analisados)

    
    but1, but2 = st.columns(2)
    # limpar o historico
    with but1:
        if not st.session_state.analisados.empty:
            def limpar():
                st.session_state.analisados = pd.DataFrame()
            st.button("Limpar histórico", on_click=limpar)

    # salvar o historico
    with but2:
        if not st.session_state.analisados.empty:
            def convert_for_download(df):
                return df.to_csv(index=False)
            
            file = convert_for_download(st.session_state.analisados)
            st.download_button(
                label="Baixar Histórico",
                data=file,
                file_name='Perfis Analisados.csv',
                mime='text/csv'

            )
