import streamlit as st
import pandas as pd

# ==========================================================
# CONFIGURACIÓN
# ==========================================================

st.set_page_config(
    page_title="EDEN HALL",
    page_icon="🍸",
    layout="wide"
)

# ==========================================================
# ESTILOS
# ==========================================================

st.markdown("""
<style>

.stApp {
    background-color: #080808;
    color: white;
}

.main {
    background-color: #080808;
}

h1 {
    color: #d4af37;
    text-align: center;
    font-family: Georgia, serif;
    font-style: italic;
    font-size: 60px;
}

h2 {
    color: #d4af37;
    font-family: Georgia, serif;
}

h3 {
    color: #ffffff;
}

.subtitulo {
    text-align: center;
    color: #ffffff;
    font-size: 22px;
    letter-spacing: 5px;
    margin-bottom: 30px;
}

.tarjeta {
    background-color: #151515;
    border: 1px solid #d4af37;
    border-radius: 15px;
    padding: 20px;
    margin-bottom: 15px;
}

.precio {
    color: #d4af37;
    font-size: 20px;
    font-weight: bold;
}

.info {
    background-color: #111111;
    border-left: 4px solid #d4af37;
    padding: 15px;
    border-radius: 8px;
}

.footer {
    text-align: center;
    color: #aaaaaa;
    padding: 30px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# ENCABEZADO
# ==========================================================

st.markdown("# EDEN HALL")
st.markdown(
    '<div class="subtitulo">RESTAURANTE & EXPERIENCIA</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="info">
<b>Bienvenido a EDEN HALL</b><br>
Un espacio gastronómico donde la elegancia, los sabores y
la experiencia se combinan para crear una propuesta diferente.
</div>
""", unsafe_allow_html=True)

st.write("")

# ==========================================================
# MENÚ LATERAL
# ==========================================================

st.sidebar.title("🍽️ EDEN HALL")

opcion = st.sidebar.radio(
    "Seleccione una sección:",
    [
        "Inicio",
        "Cócteles",
        "Carnes",
        "Tabla del menú",
        "Gráficos",
        "Chatbot"
    ]
)

# ==========================================================
# DATOS DE CÓCTELES
# ==========================================================

cocteles = [
    {
        "nombre": "Pousse-Café",
        "descripcion": "Bebida de presentación elegante con capas de diferentes sabores.",
        "precio": 18000,
        "ingredientes": "Jugos, jarabes y hielo."
    },
    {
        "nombre": "Yegua Negra",
        "descripcion": "Bebida oscura preparada con café frío y espuma de leche.",
        "precio": 20000,
        "ingredientes": "Café frío, leche, hielo y jarabe."
    },
    {
        "nombre": "Porn Star Martini",
        "descripcion": "Cóctel tropical de sabor dulce y refrescante.",
        "precio": 22000,
        "ingredientes": "Maracuyá, vainilla, limón y hielo."
    },
    {
        "nombre": "Cuba Libre",
        "descripcion": "Bebida oscura y refrescante con hielo visible.",
        "precio": 18000,
        "ingredientes": "Gaseosa de cola, limón y hielo."
    },
    {
        "nombre": "Caipiriña",
        "descripcion": "Bebida cítrica y refrescante.",
        "precio": 19000,
        "ingredientes": "Limón, azúcar, hielo y bebida cítrica."
    },
    {
        "nombre": "Cosmopolitan",
        "descripcion": "Bebida de sabor cítrico y apariencia elegante.",
        "precio": 21000,
        "ingredientes": "Arándano, naranja, limón y hielo."
    }
]

# ==========================================================
# DATOS DE CARNES
# ==========================================================

carnes = [
    {
        "nombre": "Costillas BBQ",
        "descripcion": "Costillas de cerdo con salsa BBQ.",
        "precio": 35000,
        "ingredientes": "Cerdo, salsa BBQ, sal, pimienta, ajo y paprika."
    },
    {
        "nombre": "Pollo Teriyaki",
        "descripcion": "Pollo preparado con una salsa teriyaki de sabor dulce.",
        "precio": 32000,
        "ingredientes": "Pollo, teriyaki, ajo, jengibre, miel y aceite."
    },
    {
        "nombre": "Salmón Asado",
        "descripcion": "Salmón asado acompañado de sabores cítricos.",
        "precio": 42000,
        "ingredientes": "Salmón, limón, ajo, aceite de oliva, sal y pimienta."
    },
    {
        "nombre": "Langosta Asada",
        "descripcion": "Langosta asada con mantequilla y limón.",
        "precio": 55000,
        "ingredientes": "Langosta, mantequilla, ajo, limón, sal y pimienta."
    },
    {
        "nombre": "Carne Asada",
        "descripcion": "Corte de res asado y sazonado.",
        "precio": 40000,
        "ingredientes": "Res, sal, pimienta, ajo, aceite y limón."
    },
    {
        "nombre": "Lomo de Cerdo Asado",
        "descripcion": "Lomo de cerdo asado con romero.",
        "precio": 36000,
        "ingredientes": "Cerdo, ajo, sal, pimienta, aceite, limón y romero."
    }
]

# ==========================================================
# INICIO
# ==========================================================

if opcion == "Inicio":

    st.header("Bienvenidos a EDEN HALL")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Cócteles", "6")

    with col2:
        st.metric("Platos principales", "6")

    with col3:
        st.metric("Experiencia", "EDEN")

    st.write("")

    st.markdown("""
    ### Nuestra propuesta

    EDEN HALL combina gastronomía, presentación y tecnología
    en una experiencia digital e interactiva.

    En esta versión desarrollada con Streamlit se incorporan:

    - Menú interactivo.
    - Tablas de información.
    - Gráficos.
    - Botones interactivos.
    - Chatbot de apoyo.
    - Diseño oscuro con detalles dorados.
    """)

# ==========================================================
# CÓCTELES
# ==========================================================

elif opcion == "Cócteles":

    st.header("🍸 Cócteles")

    columnas = st.columns(3)

    for i, bebida in enumerate(cocteles):

        with columnas[i % 3]:

            st.markdown(
                f"""
                <div class="tarjeta">
                    <h3>{bebida["nombre"]}</h3>
                    <p>{bebida["descripcion"]}</p>
                    <p class="precio">${bebida["precio"]:,}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                "Ver más",
                key=f"coctel_{i}"
            ):

                st.info(
                    f"""
                    **A.D.N. del producto:**  
                    {bebida["descripcion"]}

                    **Preparación:**  
                    Mezclar los ingredientes, agregar hielo y
                    presentar de acuerdo con el estilo de EDEN HALL.

                    **Ingredientes:**  
                    {bebida["ingredientes"]}
                    """
                )

# ==========================================================
# CARNES
# ==========================================================

elif opcion == "Carnes":

    st.header("🥩 Carnes")

    columnas = st.columns(3)

    for i, carne in enumerate(carnes):

        with columnas[i % 3]:

            st.markdown(
                f"""
                <div class="tarjeta">
                    <h3>{carne["nombre"]}</h3>
                    <p>{carne["descripcion"]}</p>
                    <p class="precio">${carne["precio"]:,}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                "Ver más",
                key=f"carne_{i}"
            ):

                st.info(
                    f"""
                    **A.D.N. del producto:**  
                    {carne["descripcion"]}

                    **Preparación:**  
                    Sazonar el producto y cocinarlo hasta alcanzar
                    una preparación adecuada. Finalmente se presenta
                    de manera elegante.

                    **Ingredientes:**  
                    {carne["ingredientes"]}
                    """
                )

# ==========================================================
# TABLA
# ==========================================================

elif opcion == "Tabla del menú":

    st.header("📋 Tabla del menú")

    datos = []

    for bebida in cocteles:
        datos.append([
            "Cóctel",
            bebida["nombre"],
            bebida["precio"]
        ])

    for carne in carnes:
        datos.append([
            "Carne",
            carne["nombre"],
            carne["precio"]
        ])

    tabla = pd.DataFrame(
        datos,
        columns=[
            "Categoría",
            "Producto",
            "Precio"
        ]
    )

    st.dataframe(
        tabla,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("Resumen")

    col1, col2 = st.columns(2)

    with col1:
        st.write("Cantidad de cócteles:", len(cocteles))

    with col2:
        st.write("Cantidad de carnes:", len(carnes))

# ==========================================================
# GRÁFICOS
# ==========================================================

elif opcion == "Gráficos":

    st.header("📊 Gráficos del menú")

    nombres = [x["nombre"] for x in cocteles]
    precios = [x["precio"] for x in cocteles]

    datos_grafico = pd.DataFrame(
        {
            "Producto": nombres,
            "Precio": precios
        }
    )

    st.subheader("Precios de los cócteles")

    st.bar_chart(
        datos_grafico.set_index("Producto")
    )

    st.subheader("Precios de las carnes")

    nombres_carne = [x["nombre"] for x in carnes]
    precios_carne = [x["precio"] for x in carnes]

    datos_carne = pd.DataFrame(
        {
            "Producto": nombres_carne,
            "Precio": precios_carne
        }
    )

    st.bar_chart(
        datos_carne.set_index("Producto")
    )

# ==========================================================
# CHATBOT
# ==========================================================

elif opcion == "Chatbot":

    st.header("🤖 Chatbot de EDEN HALL")

    st.write(
        "Este chatbot proporciona información básica sobre "
        "el restaurante y su menú."
    )

    pregunta = st.text_input(
        "Escriba su pregunta:"
    )

    if pregunta:

        pregunta = pregunta.lower()

        if "menú" in pregunta or "menu" in pregunta:

            st.success(
                "EDEN HALL cuenta con 6 cócteles y 6 opciones de carnes."
            )

        elif "cóctel" in pregunta or "coctel" in pregunta:

            st.success(
                "Tenemos Pousse-Café, Yegua Negra, "
                "Porn Star Martini, Cuba Libre, "
                "Caipiriña y Cosmopolitan."
            )

        elif "carne" in pregunta:

            st.success(
                "Tenemos Costillas BBQ, Pollo Teriyaki, "
                "Salmón Asado, Langosta Asada, "
                "Carne Asada y Lomo de Cerdo Asado."
            )

        elif "precio" in pregunta:

            st.success(
                "Los precios pueden consultarse directamente "
                "en las secciones Cócteles y Carnes."
            )

        elif "eden" in pregunta:

            st.success(
                "EDEN HALL es un proyecto de restaurante "
                "enfocado en gastronomía y experiencia."
            )

        else:

            st.info(
                "Puedo ayudarte con información sobre el menú, "
                "cócteles, carnes y precios."
            )

# ==========================================================
# PIE DE PÁGINA
# ==========================================================

st.markdown(
    """
    <div class="footer">
        EDEN HALL · RESTAURANTE & EXPERIENCIA<br>
        Proyecto académico desarrollado con Python y Streamlit
    </div>
    """,
    unsafe_allow_html=True
)