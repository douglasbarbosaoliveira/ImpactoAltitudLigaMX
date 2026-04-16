import streamlit as st
import pandas as pd
import joblib
import statsmodels.api as sm

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Liga MX - Altitude Intelligence",
    page_icon="logos/Liga_MX_logo.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- SISTEMA DE IDIOMAS (Leve e Rápido) ---
col_vazia, col_lang = st.columns([8, 2])
with col_lang:
    idioma = st.selectbox("Idioma / Language", ["Português - PT-BR", "Español - ES-MX", "English - EN-US"])

# Dicionário de Traduções
txt = {
    "Português - PT-BR": {
        "title": "LIGA MX: O FATOR ALTITUDE",
        "sub": "Simulador de Impacto Geográfico no Campeonato Mexicano",
        "choose": "Escolha os times",
        "home": "MANDANTE",
        "away": "VISITANTE",
        "city": "Cidade",
        "stad": "Estádio",
        "alt": "Altitude",
        "btn": "PROCESSAR ALGORITMOS DE PREDIÇÃO",
        "ols_title": "REGRESSÃO LINEAR (OLS)",
        "ols_desc": "EXPECTATIVA DE PONTOS CONQUISTADOS PELO VISITANTE",
        "mlp_title": "REDE NEURAL (MULTILAYER PERCEPTRON)",
        "mlp_desc": "PROBABILIDADE DE PONTUAR DO VISITANTE (Vitória ou Empate)",
        "dossier": "Dados do Projeto",
        "tabs": ["O Peso da Altitude", "Como a IA analisa o jogo", "Dados e Pipeline", "Links e Relatórios", "Referências", "Sobre"],
        "t1_title": "O 'Imposto do Oxigênio' na Liga MX",
        "t1_body": """Quem acompanha futebol sabe que jogar nas altitudes de La Paz (3600m) ou Quito (2850m) é muitas vezes um pesadelo. No Campeonato Mexicano (Liga MX) isso é mais comum do que em outras ligas! Temos times que jogam ao nível do mar (Mazatlán e Tijuana) e times que mandam seus jogos "quase nas nuvens" (Toluca, a 2.660 metros).<br><br>Este projeto usa Inteligência Artificial para responder: <b>quantos pontos um time visitante pode perder pelo fator altitude?</b> A teoria é que a diferença de altura funciona como uma "mochila de pedras" invisível nas costas dos jogadores.<br><br><i><b>Delimitação do estudo:</b> O futebol não é só o cansaço causado pela altitude. Qualidade do elenco, tática, lesões ou investimento financeiro decidem jogos. Deixamos isso de lado de propósito para olhar com uma lupa <b>apenas para a altitude</b>. O oxigênio explica uma pequena fatia do resultado, mas em condições extremas, esse "detalhe" é crucial.</i>""",
        "t2_title": "Tática de Jogo: Colocando a IA em Campo",
        "t2_body": """Usamos duas estratégias como nossos analistas de desempenho:<br><br><b>1. Regressão Linear - OLS:</b> É a estatística pura. Diz o óbvio através de números: "A cada metro que o visitante sobe, mais difícil fica respirar e menor é a chance de pontuar". Traça uma linha reta da queda de desempenho.<br><br><b>2. Rede Neural (MLP):</b> É o nosso modelo de Inteligência Artificial. Ele entende que jogar na altitude não é uma máquina linear. Subir 500 metros quase não muda nada, mas pular dos 800m para os 2600m faz uma grande diferença biológica.""",
        "t3_title": "Pipeline e Tratamento de Dados",
        "t3_body": """• <b>Web Scraping:</b> Resultados oficiais da Liga MX (2021-2025) extraídos do site FBRef.<br>• <b>Geolocalização:</b> Coordenadas de cada estádio validadas no site do INEGI.<br>• <b>Feature Engineering:</b> Criação da variável <code>Dif_Altitud</code> e do alvo (Sucesso vs Derrota).<br>• <b>Normalização:</b> Dados passam por um <code>StandardScaler</code> para alinhar os deltas com a Rede Neural.""",
        "t4_title": "Sobre o Projeto",
        "t4_body": """<b>Douglas Barbosa de Oliveira</b><br>Este portal analítico é parte do projeto da disciplina de <b>Inteligência Artificial I</b>.<br><br>Desenvolvido durante o intercâmbio acadêmico na <b>Universidad de Monterrey (UDEM)</b> - México, em parceria com o curso de Desenvolvimento de Software Multiplataforma da <b>FATEC Mauá</b> - Brasil.""",
        "t5_title": "Repositórios e Relatórios",
        "t5_body": """Acesse os códigos-fonte e os relatórios acadêmicos completos:<br><br>🔗 <a href='https://github.com/douglasbarbosaoliveira/ImpactoAltitudLigaMX' style='color:#006847;'>GitHub Repository (Código e Datasets)</a>""",
        "t6_title": "Referências Bibliográficas",
        "t6_body": """• <b>FBRef:</b> Sports Reference LLC. "Liga MX Stats and History". Disponível em: fbref.com.<br>• <b>INEGI:</b> Instituto Nacional de Estadística y Geografía. "Relieve e Información Geográfica de México". Disponível em: inegi.org.mx.<br>• <b>Scikit-Learn:</b> Pedregosa et al., 2011. "Scikit-learn: Machine Learning in Python". JMLR 12, pp. 2825-2830.<br>• <b>StatsModels:</b> Seabold, Skipper, and Josef Perktold. "Statsmodels: Econometric and statistical modeling with python." Proceedings of the 9th Python in Science Conference. 2010."""
    },
    "Español - ES-MX": {
        "title": "LIGA MX: EL FACTOR ALTITUD",
        "sub": "Simulador de Impacto Geográfico en el Fútbol Mexicano",
        "choose": "Elige los equipos",
        "home": "LOCAL",
        "away": "VISITANTE",
        "city": "Ciudad",
        "stad": "Estadio",
        "alt": "Altitud",
        "btn": "PROCESAR ALGORITMOS DE PREDICCIÓN",
        "ols_title": "REGRESIÓN LINEAL (OLS)",
        "ols_desc": "EXPECTATIVA DE PUNTOS OBTENIDOS POR EL VISITANTE",
        "mlp_title": "RED NEURONAL (MULTILAYER PERCEPTRON)",
        "mlp_desc": "PROBABILIDAD DE PUNTUAR DEL VISITANTE (Victoria o Empate)",
        "dossier": "Radiografía del Proyecto",
        "tabs": ["El Peso de la Altitud", "Cómo la IA analiza el juego", "Datos y Pipeline", "Enlaces y Reportes", "Referencias", "Sobre"],
        "t1_title": "El 'Impuesto del Oxígeno' en la Liga MX",
        "t1_body": """Cualquiera que siga el fútbol sabe que jugar en la altitud de La Paz (3600m) o Quito (2850m) es a menudo una pesadilla. ¡En la Liga MX esto es más común que en otras ligas! Tenemos equipos que juegan al nivel del mar (Mazatlán y Tijuana) y otros "casi en las nubes" (Toluca, a 2660m).<br><br>Este proyecto usa Inteligencia Artificial para responder: <b>¿cuántos puntos puede perder un visitante por la altitud?</b> La teoría es que la diferencia de altura funciona como una "mochila de piedras" invisible.<br><br><i><b>Delimitación:</b> El fútbol no es solo cansancio. Calidad del plantel, táctica o inversión deciden partidos. Dejamos eso de lado a propósito para mirar <b>solo la altitud</b>. El oxígeno explica una pequeña porción del resultado, pero en condiciones extremas es crucial.</i>""",
        "t2_title": "Táctica: Poniendo la IA en la Cancha",
        "t2_body": """Usamos dos estrategias:<br><br><b>1. Regresión Lineal - OLS:</b> Estadística pura. "A cada metro que el visitante sube, es más difícil respirar y menor la chance de puntuar".<br><br><b>2. Red Neuronal (MLP):</b> Entiende que jugar en la altitud no es lineal. Subir 500m casi no cambia nada, pero saltar de 800m a 2600m hace una gran diferencia biológica.""",
        "t3_title": "Pipeline de Datos",
        "t3_body": """• <b>Web Scraping:</b> Resultados oficiales (2021-2025) de FBRef.<br>• <b>Geolocalización:</b> Coordenadas de estadios validadas en el INEGI.<br>• <b>Feature Engineering:</b> Creación de <code>Dif_Altitud</code> y variable objetivo.<br>• <b>Normalización:</b> <code>StandardScaler</code> para la Red Neuronal.""",
        "t4_title": "Sobre el Proyecto",
        "t4_body": """<b>Douglas Barbosa de Oliveira</b><br>Portal analítico para la clase de <b>Inteligencia Artificial I</b>.<br><br>Desarrollado durante el intercambio en la <b>Universidad de Monterrey (UDEM)</b>, en conjunto con <b>FATEC Mauá</b> - Brasil.""",
        "t5_title": "Repositorios y Reportes",
        "t5_body": """Accede al código y reportes:<br><br>🔗 <a href='https://github.com/douglasbarbosaoliveira/ImpactoAltitudLigaMX' style='color:#006847;'>Repositorio GitHub</a>""",
        "t6_title": "Referencias",
        "t6_body": """• <b>FBRef:</b> Sports Reference LLC. "Liga MX Stats and History". Disponible en: fbref.com.<br>• <b>INEGI:</b> Instituto Nacional de Estadística y Geografía. "Relieve e Información Geográfica de México". Disponible en: inegi.org.mx.<br>• <b>Scikit-Learn:</b> Pedregosa et al., 2011. "Scikit-learn: Machine Learning in Python". JMLR 12, pp. 2825-2830.<br>• <b>StatsModels:</b> Seabold, Skipper, and Josef Perktold. "Statsmodels: Econometric and statistical modeling with python." Proceedings of the 9th Python in Science Conference. 2010."""
    },
    "English - EN-US": {
        "title": "LIGA MX: THE ALTITUDE FACTOR",
        "sub": "Geographical Impact Simulator in the Mexican League",
        "choose": "Choose the teams",
        "home": "HOME",
        "away": "AWAY",
        "city": "City",
        "stad": "Stadium",
        "alt": "Altitude",
        "btn": "PROCESS PREDICTION ALGORITHMS",
        "ols_title": "LINEAR REGRESSION (OLS)",
        "ols_desc": "EXPECTED POINTS SECURED BY THE AWAY TEAM",
        "mlp_title": "NEURAL NETWORK (MULTILAYER PERCEPTRON)",
        "mlp_desc": "AWAY TEAM PROBABILITY TO SCORE (Win or Draw)",
        "dossier": "Project X-Ray",
        "tabs": ["The Weight of Altitude", "How AI analyzes the game", "Data Pipeline", "Links & Reports", "References", "About"],
        "t1_title": "The 'Oxygen Tax' in Liga MX",
        "t1_body": """Anyone who follows soccer knows that playing at the altitude of La Paz (3600m) is a nightmare. In Liga MX, this is highly common! We have teams playing at sea level (Mazatlán) and teams playing "in the clouds" (Toluca, at 2660m).<br><br>This project uses AI to answer: <b>how many points does an away team lose due to altitude?</b><br><br><i><b>Delimitation:</b> Soccer is not just about fatigue. Roster quality, tactics, and money decide games. We purposely left those aside to look <b>only at altitude</b>. Oxygen explains a small slice of the result, but in extreme conditions, it is crucial.</i>""",
        "t2_title": "Tactics: Putting AI on the Pitch",
        "t2_body": """We use two strategies:<br><br><b>1. Linear Regression (OLS):</b> Pure statistics. "Every meter you climb, it gets harder to breathe."<br><br><b>2. Neural Network (MLP):</b> Understands that altitude is not linear. Climbing 500m changes little, but jumping from 800m to 2600m makes a huge biological difference.""",
        "t3_title": "Data Pipeline",
        "t3_body": """• <b>Web Scraping:</b> Official results (2021-2025) from FBRef.<br>• <b>Geolocation:</b> Stadium coordinates validated by INEGI.<br>• <b>Feature Engineering:</b> <code>Dif_Altitud</code> creation.<br>• <b>Normalization:</b> <code>StandardScaler</code> integration.""",
        "t4_title": "About the Project",
        "t4_body": """<b>Douglas Barbosa de Oliveira</b><br>Analytical portal for the <b>Artificial Intelligence I</b> class.<br><br>Developed during the exchange program at <b>Universidad de Monterrey (UDEM)</b> - Mexico, in partnership with <b>FATEC Mauá</b> - Brazil.""",
        "t5_title": "Repositories and Reports",
        "t5_body": """Access the source code:<br><br>🔗 <a href='https://github.com/douglasbarbosaoliveira/ImpactoAltitudLigaMX' style='color:#006847;'>GitHub Repository</a>""",
        "t6_title": "References",
        "t6_body": """• <b>FBRef:</b> Sports Reference LLC. "Liga MX Stats and History". Available at: fbref.com.<br>• <b>INEGI:</b> Instituto Nacional de Estadística y Geografía. "Relieve e Información Geográfica de México". Available at: inegi.org.mx.<br>• <b>Scikit-Learn:</b> Pedregosa et al., 2011. "Scikit-learn: Machine Learning in Python". JMLR 12, pp. 2825-2830.<br>• <b>StatsModels:</b> Seabold, Skipper, and Josef Perktold. "Statsmodels: Econometric and statistical modeling with python." Proceedings of the 9th Python in Science Conference. 2010."""
    }
}
t = txt[idioma] 

# 2. BANCO DE DADOS COMPLETO LIGA MX
times_db = {
    'América': {'alt': 2240, 'cidade': 'Ciudad de México', 'estadio': 'Estadio Azteca', 'logo': 'logos/america.png'},
    'Atlas': {'alt': 1566, 'cidade': 'Guadalajara', 'estadio': 'Estadio Jalisco', 'logo': 'logos/atlas.png'},
    'Atlético San Luis': {'alt': 1864, 'cidade': 'San Luis Potosí', 'estadio': 'Estadio Alfonso Lastras', 'logo': 'logos/atleticosl.png'},
    'Chivas Guadalajara': {'alt': 1566, 'cidade': 'Guadalajara', 'estadio': 'Estadio Akron', 'logo': 'logos/guadalajara.png'},
    'Cruz Azul': {'alt': 2240, 'cidade': 'Ciudad de México', 'estadio': 'Estadio Ciudad de los Deportes', 'logo': 'logos/cruzazul.png'},
    'FC Juárez': {'alt': 1140, 'cidade': 'Ciudad Juárez', 'estadio': 'Estadio Olímpico Benito Juárez', 'logo': 'logos/juarez.png'},
    'León': {'alt': 1815, 'cidade': 'León', 'estadio': 'Estadio León', 'logo': 'logos/leon.png'},
    'Mazatlán': {'alt': 4, 'cidade': 'Mazatlán', 'estadio': 'Estadio El Encanto', 'logo': 'logos/mazatlan.png'},
    'Monterrey': {'alt': 540, 'cidade': 'Monterrey', 'estadio': 'Estadio BBVA', 'logo': 'logos/monterrey.png'},
    'Necaxa': {'alt': 1888, 'cidade': 'Aguascalientes', 'estadio': 'Estadio Victoria', 'logo': 'logos/necaxa.png'},
    'Pachuca': {'alt': 2432, 'cidade': 'Pachuca', 'estadio': 'Estadio Hidalgo', 'logo': 'logos/pachuca.png'},
    'Puebla': {'alt': 2135, 'cidade': 'Puebla', 'estadio': 'Estadio Cuauhtémoc', 'logo': 'logos/puebla.png'},
    'Pumas UNAM': {'alt': 2250, 'cidade': 'Ciudad de México', 'estadio': 'Estadio Olímpico Universitario', 'logo': 'logos/pumas.png'},
    'Querétaro': {'alt': 1820, 'cidade': 'Querétaro', 'estadio': 'Estadio Corregidora', 'logo': 'logos/queretaro.png'},
    'Santos Laguna': {'alt': 1120, 'cidade': 'Torreón', 'estadio': 'Estadio Corona (TSM)', 'logo': 'logos/santos.png'},
    'Tigres UANL': {'alt': 540, 'cidade': 'Monterrey', 'estadio': 'Estadio Universitario', 'logo': 'logos/tigres.png'},
    'Tijuana': {'alt': 20, 'cidade': 'Tijuana', 'estadio': 'Estadio Caliente', 'logo': 'logos/tijuana.png'},
    'Toluca': {'alt': 2660, 'cidade': 'Toluca', 'estadio': 'Estadio Nemesio Díez', 'logo': 'logos/toluca.png'}
}

lista_times = list(times_db.keys())
total_times = len(lista_times)

# 3. LÓGICA DE ESTADO (MEMÓRIA DAS SETAS COM ANTI-ESPELHO)
if 'home_idx' not in st.session_state:
    st.session_state.home_idx = 17  # Toluca
if 'away_idx' not in st.session_state:
    st.session_state.away_idx = 8   # Monterrey

def prev_home(): 
    st.session_state.home_idx = (st.session_state.home_idx - 1) % total_times
    if st.session_state.home_idx == st.session_state.away_idx:
        st.session_state.home_idx = (st.session_state.home_idx - 1) % total_times

def next_home(): 
    st.session_state.home_idx = (st.session_state.home_idx + 1) % total_times
    if st.session_state.home_idx == st.session_state.away_idx:
        st.session_state.home_idx = (st.session_state.home_idx + 1) % total_times

def prev_away(): 
    st.session_state.away_idx = (st.session_state.away_idx - 1) % total_times
    if st.session_state.away_idx == st.session_state.home_idx:
        st.session_state.away_idx = (st.session_state.away_idx - 1) % total_times

def next_away(): 
    st.session_state.away_idx = (st.session_state.away_idx + 1) % total_times
    if st.session_state.away_idx == st.session_state.home_idx:
        st.session_state.away_idx = (st.session_state.away_idx + 1) % total_times

# 4. DESIGN SYSTEM CSS (Com Alinhamento Central para Abas)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Jura:wght@300;500;700&family=Montserrat:wght@400;700&display=swap');
    
    html, body, [class*="css"] { font-family: 'Jura', sans-serif; color: #FFFFFF; }

    .stApp {
        background-color: #020502;
        background-image: linear-gradient(rgba(0, 0, 0, 0.9), rgba(0, 0, 0, 0.97)), 
                          url('https://populous.com/uploads/2018/01/MNTRYMXSOC_0363_JorgeToboada-1200x900-c-center-1200x0-c-default.webp');
        background-size: cover; background-attachment: fixed;
    }

    [data-testid="column"] { background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.05); padding: 30px !important; border-radius: 4px; transition: 0.4s; }
    [data-testid="column"]:nth-of-type(1) { border-left: 5px solid #006847; } 
    [data-testid="column"]:nth-of-type(3) { border-right: 5px solid #CE1126; } 

    .team-name { font-family: 'Montserrat', sans-serif; font-size: 28px; font-weight:700; letter-spacing: -1px; margin-bottom: 20px; text-transform: uppercase; text-align: center; color: #FFF; }
    .stat-label { color: #666; font-size: 11px; text-transform: uppercase; letter-spacing: 2px; text-align: center; margin-top: 15px;}
    .stat-value { font-family: 'Montserrat', sans-serif; font-size: 18px; font-weight: 700; color: #DDD; text-align: center; margin-bottom: 5px;}

    .stButton>button { background: transparent; color: #AAA; border: 1px solid rgba(255,255,255,0.1); border-radius: 4px; width: 100%; transition: 0.3s; padding: 10px; font-size: 18px; }
    .stButton>button:hover { background: rgba(255,255,255,0.1); color: #FFF; border-color: #FFF; }
    
    /* Configuração das Abas Centralizadas e Espaçadas */
    .stTabs [data-baseweb="tab-list"] { 
        background-color: transparent; 
        justify-content: center; 
        gap: 35px; 
    }
    .stTabs [data-baseweb="tab"] { 
        color: #888; 
        font-family: 'Montserrat', sans-serif; 
        letter-spacing: 1px; 
        font-size: 16px;
        padding-bottom: 10px;
    }
    .stTabs [aria-selected="true"] { 
        color: #FFF !important; 
        font-weight: 700 !important;
        border-bottom: 3px solid #006847 !important; 
    }
    
    .doc-title { color: #006847; font-family: 'Montserrat', sans-serif; font-weight: 700; font-size: 24px; margin-bottom: 10px; margin-top: 20px;}
    .doc-text { color: #CCC; font-size: 16px; line-height: 1.6; font-family: 'Jura', sans-serif; text-align: justify;}
    
    .lang-selector { margin-bottom: -50px;}
    </style>
    """, unsafe_allow_html=True)

# 5. CARREGAMENTO DOS MODELOS
@st.cache_resource
def load_all():
    models = {"reg_linear": joblib.load('modelo_ols_puntos.pkl'), "nn_clf": joblib.load('modelo_nn.pkl')}
    scaler = joblib.load('scaler_liga_mx.pkl')
    return models, scaler

try:
    models, scaler = load_all()
except:
    st.warning("⚠️ Carregue os modelos .pkl na pasta para simular.")

# --- HEADER COM LOGO OFICIAL E TRADUÇÕES ---
col_logo, col_t = st.columns([1, 6], vertical_alignment="center")
with col_logo:
    st.image("logos/Liga_MX_logo.png", width=120)
with col_t:
    st.markdown(f'<p style="color:#FFF; font-family:\'Montserrat\', sans-serif; font-size:40px; font-weight:700; margin-bottom:0px; letter-spacing:2px;">{t["title"]}</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="color:#666; letter-spacing:5px; font-size:14px; text-transform:uppercase;">{t["sub"]}</p>', unsafe_allow_html=True)

st.write("---")

# --- INSTRUÇÃO DE USO ---
st.markdown(f'<p style="color:#FFF; text-align: center; letter-spacing:5px; font-size:16px; text-transform:uppercase;">{t["choose"]}</p>', unsafe_allow_html=True)

# --- PALCO VS ---
home_name = lista_times[st.session_state.home_idx]
away_name = lista_times[st.session_state.away_idx]

c_left, c_mid, c_right = st.columns([2.5, 1, 2.5])

# CARD MANDANTE
with c_left:
    st.markdown(f'<p class="stat-label" style="margin-top:0px; color:#006847; font-weight:bold;">{t["home"]}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="team-name">{home_name}</p>', unsafe_allow_html=True)
    
    col_nav1, col_img, col_nav2 = st.columns([1, 1.5, 1], vertical_alignment="center")
    with col_nav1:
        st.button("◀", key="h_prev", on_click=prev_home, use_container_width=True)
    with col_img:
        st.image(times_db[home_name]['logo'], use_container_width=True) 
    with col_nav2:
        st.button("▶", key="h_next", on_click=next_home, use_container_width=True)

    st.markdown(f'<p class="stat-label">{t["city"]}</p><p class="stat-value">{times_db[home_name]["cidade"]}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="stat-label">{t["stad"]}</p><p class="stat-value">{times_db[home_name]["estadio"]}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="stat-label">{t["alt"]}</p><p class="stat-value">{times_db[home_name]["alt"]} M</p>', unsafe_allow_html=True)

# CARD VS
with c_mid:
    st.markdown("<h1 style='text-align: center; margin-top: 250px; opacity: 0.15; font-size: 70px; font-family:\'Montserrat\';'>VS</h1>", unsafe_allow_html=True)

# CARD VISITANTE
with c_right:
    st.markdown(f'<p class="stat-label" style="margin-top:0px; color:#CE1126; font-weight:bold;">{t["away"]}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="team-name">{away_name}</p>', unsafe_allow_html=True)
    
    col_nav3, col_img2, col_nav4 = st.columns([1, 1.5, 1], vertical_alignment="center")
    with col_nav3:
        st.button("◀", key="a_prev", on_click=prev_away, use_container_width=True)
    with col_img2:
        st.image(times_db[away_name]['logo'], use_container_width=True)
    with col_nav4:
        st.button("▶", key="a_next", on_click=next_away, use_container_width=True)

    st.markdown(f'<p class="stat-label">{t["city"]}</p><p class="stat-value">{times_db[away_name]["cidade"]}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="stat-label">{t["stad"]}</p><p class="stat-value">{times_db[away_name]["estadio"]}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="stat-label">{t["alt"]}</p><p class="stat-value">{times_db[away_name]["alt"]} M</p>', unsafe_allow_html=True)

# --- EXECUÇÃO (RESULTADOS) ---
st.write("")
dif_alt = times_db[home_name]['alt'] - times_db[away_name]['alt']

if st.button(t["btn"], use_container_width=True):
    try:
        X_input = pd.DataFrame([[dif_alt]], columns=['Dif_Altitud'])
        X_scaled = scaler.transform(X_input)
        
        r1, r2 = st.columns(2)
        with r1:
            X_const = sm.add_constant(X_input, has_constant='add')
            pontos = models['reg_linear'].predict(X_const)[0]
            st.markdown(f"""
            <div style='background:rgba(255,255,255,0.03); padding:30px; border:1px solid rgba(255,255,255,0.1); text-align:center;'>
                <p class="stat-label" style="margin-top:0;">{t["ols_title"]}</p>
                <h1 style='font-size:60px; color:#FFF; font-family:"Montserrat";'>{pontos:.2f}</h1>
                <p style="color:#888; font-size: 12px; letter-spacing:2px;">{t["ols_desc"]}</p>
            </div>
            """, unsafe_allow_html=True)
            
        with r2:
            prob = models['nn_clf'].predict_proba(X_scaled)[0][1] * 100
            st.markdown(f"""
            <div style='background:rgba(255,255,255,0.03); padding:30px; border:1px solid rgba(255,255,255,0.1); text-align:center;'>
                <p class="stat-label" style="margin-top:0;">{t["mlp_title"]}</p>
                <h1 style='font-size:60px; color:#FFF; font-family:"Montserrat";'>{prob:.1f}%</h1>
                <p style="color:#888; font-size: 12px; letter-spacing:2px;">{t["mlp_desc"]}</p>
            </div>
            """, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Erro: {e}")

# --- DOSSIÊ DO PROJETO MULTI-IDIOMA ---
st.write("---")
st.markdown(f'<p style="color:#FFF; text-align: center; letter-spacing:5px; font-size:16px; text-transform:uppercase;">{t["dossier"]}</p>', unsafe_allow_html=True)

# Geração das Abas mapeando a ordem correta ("Sobre" no final)
tb1, tb2, tb3, tb4, tb5, tb6 = st.tabs(t["tabs"])

with tb1:
    st.markdown(f'<p class="doc-title">{t["t1_title"]}</p><p class="doc-text">{t["t1_body"]}</p>', unsafe_allow_html=True)
with tb2:
    st.markdown(f'<p class="doc-title">{t["t2_title"]}</p><p class="doc-text">{t["t2_body"]}</p>', unsafe_allow_html=True)
with tb3:
    st.markdown(f'<p class="doc-title">{t["t3_title"]}</p><p class="doc-text">{t["t3_body"]}</p>', unsafe_allow_html=True)
with tb4:
    st.markdown(f'<p class="doc-title">{t["t5_title"]}</p><p class="doc-text">{t["t5_body"]}</p>', unsafe_allow_html=True)
with tb5:
    st.markdown(f'<p class="doc-title">{t["t6_title"]}</p><p class="doc-text">{t["t6_body"]}</p>', unsafe_allow_html=True)
with tb6:
    st.markdown(f'<p class="doc-title">{t["t4_title"]}</p><p class="doc-text">{t["t4_body"]}</p>', unsafe_allow_html=True)

st.write("---")
st.caption("© 2026 Liga MX Altitude Intelligence | Monterrey, NL - México")