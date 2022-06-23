import streamlit as st
import numpy as np
st.set_page_config(layout="wide")
import microfita

st.title("Projeto Antena de Microfita")

escolha = st.radio("Escolha o tipo de análise:",("Encontrar as características", "Encontrar as dimensões"), horizontal=True)

if escolha=="Encontrar as características":
    col1, col2 = st.columns(2)

    with col1:
        h = st.text_input("Digite a largura do dielétrico: ")
        w = st.text_input("Digite a largura da linha: ")
        unidade = st.selectbox("Escolha unidade das larguras: ", ("mm", "cm", "m"))
        e = st.text_input("Digite o valor da permissividade relativa do dielétrico: ")
        beta = st.radio("Calcular β?", ("Sim", "Não"))
        if beta=="Sim":
            f = st.text_input("Digite a frequência: ")
        calcular = st.button("Projetar!")

    with col2:
        if(calcular==True):
            st.markdown('<h3>Resultados:', unsafe_allow_html=True)
            ef = microfita.e_efetiva(float(e), float(w), float(h))
            st.text("A permissividade relativa efetiva é: "+str(round(ef, 2)))
            st.text("A velocidade de propagação é: "+str(round(microfita.velocidade(ef), 2))+"m/s")
            st.text("A impedância característica é: "+str(round(microfita.impedancia(float(ef), float(w), float(h)), 2))+"Ω")
            if beta=="Sim":
                k0 = (2*np.pi*float(f))/(300000000)
                b = k0*np.sqrt(ef)
                st.text("β = "+str(round(b, 2)))

elif escolha=="Encontrar as dimensões":
    col1, col2 = st.columns(2)
    with col1:
        z = st.text_input("Digite a impedância desejada: ")
        h2 = st.text_input("Digite a largura do dielétrico: ")
        unidade = st.selectbox("Escolha unidade das larguras: ", ("mm", "cm", "m"))
        e2 = st.text_input("Digite o valor da permissividade relativa do dielétrico: ")
        coe = st.radio("Calcular coeficientes?", ("Sim", "Não"))
        if coe=="Sim":
            f = st.text_input("Digite a frequência: ")
            d = st.text_input("Digite δ: ")
            zs = st.text_input("Digite a impedância da fonte: ")
        calcular = st.button("Projetar!")


    with col2:
        if(calcular==True):
            st.markdown('<h3>Resultados:', unsafe_allow_html=True)
            w = microfita.w_h(float(e2), microfita.A(float(z), float(e2)), microfita.B(float(z), float(e2)), float(h2))
            ef = microfita.e_efetiva(float(e2), w, float(h2))
            st.text("A largura da linha deverá ser de: "+str(round(w, 2))+unidade)
            st.text("A permissividade relativa efetiva será de: "+str(round(ef, 2)))
            st.text("A velocidade de propagação será de: "+str(round(microfita.velocidade(ef), 2))+"m/s")
            if coe=="Sim":
                k0 = (2*np.pi*float(f))/(300000000)
                st.text("σd = "+str(round((k0*float(e2)*(ef-1)*np.tan(float(d)))/(2*np.sqrt(ef)*(float(e2)-1)), 2))+"Np/m")
                st.text("σc = "+str(round(float(zs)/(float(z)*w), 2))+"Np/m")