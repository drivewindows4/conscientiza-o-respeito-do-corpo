import streamlit as st

# ============================================================
# 💪 O CORPO É TEMPLO DE DEUS – Versão Devocional com Design
# Desenvolvido por Roger | 2025
# ============================================================

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="💪 O Corpo é Templo de Deus",
    page_icon="🌿",
    layout="centered"
)

# --- ESTILO PERSONALIZADO (CSS) ---
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1521334884684-d80222895322?auto=format&fit=crop&w=1920&q=80");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

[data-testid="stHeader"] {
    background-color: rgba(0,0,0,0);
}

h1, h2, h3 {
    text-align: center;
    color: #1f2937;
    text-shadow: 1px 1px 2px #ffffff;
}

div[data-testid="stMarkdownContainer"] p {
    font-size: 17px;
    color: #111827;
}

.block-container {
    background-color: rgba(255,255,255,0.90);
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0px 0px 15px rgba(0,0,0,0.2);
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --- CONTEÚDO PRINCIPAL ---
st.title("💪 O Corpo é Templo de Deus")
st.markdown("### “Ou não sabeis que o vosso corpo é templo do Espírito Santo, que habita em vós?” *(1 Coríntios 6:19)*")
st.markdown("---")

st.write("""
Cuidar do corpo é uma forma de **adorar a Deus**, expressando gratidão pela vida e pela saúde.  
O Senhor deseja que sejamos **equilibrados**, mantendo o corpo, a mente e o espírito em harmonia.  
""")

st.markdown("---")

# --- ENTRADA DE DADOS ---
col1, col2 = st.columns(2)
with col1:
    peso = st.number_input("⚖️ Peso (kg):", min_value=20.0, max_value=300.0, step=0.1)
with col2:
    altura = st.number_input("📏 Altura (m):", min_value=1.0, max_value=2.5, step=0.01)

# --- BOTÃO DE AÇÃO ---
if st.button("📊 Calcular e Ver Resultado"):
    if peso and altura:
        imc = peso / (altura ** 2)
        st.markdown(f"### 💬 Seu IMC é: **{imc:.2f}**")
        st.markdown("---")

        if imc < 18.5:
            st.warning("🩻 Você está **abaixo do peso ideal.**")
            st.write("""
            ⚠️ O corpo enfraquecido pode sofrer com **baixa imunidade e fadiga**.  
            🍽️ Fortaleça-se com alimentação equilibrada e orientação médica.  
            🙏 Lembre-se: Deus quer que você tenha **vida em abundância** (João 10:10).
            """)
        elif 18.5 <= imc < 25:
            st.success("✅ Parabéns! Você está com **peso ideal!**")
            st.write("""
            🌿 Continue cuidando do seu corpo com moderação e alegria.  
            🕊️ O equilíbrio é um ato de **sabedoria espiritual** e **gratidão a Deus.**
            """)
        elif 25 <= imc < 30:
            st.warning("⚠️ Você está com **sobrepeso.**")
            st.write("""
            🍎 O excesso de peso pode trazer **cansaço e sobrecarga ao coração.**  
            🚶 Caminhe, hidrate-se e reduza alimentos processados.  
            💡 Cuidar-se é também **amar o templo onde Deus habita**.
            """)
        else:
            st.error("❗ Você está em **obesidade.**")
            st.write("""
            💔 O corpo em sobrecarga corre risco de **hipertensão, diabetes e doenças cardíacas.**  
            🍃 Mas há esperança: uma rotina saudável e fé podem restaurar seu vigor.  
            🙏 Cuide-se, porque **Deus valoriza o corpo que Ele criou.**
            """)

        st.markdown("---")
        st.info("🌿 *“Amado, desejo que te vá bem em todas as coisas e que tenhas saúde, assim como bem vai a tua alma.”* (3 João 1:2)")
    else:
        st.warning("Por favor, insira valores válidos de peso e altura.")
