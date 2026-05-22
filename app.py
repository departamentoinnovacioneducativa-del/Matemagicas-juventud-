import streamlit as st
from openai import OpenAI
import streamlit.components.v1 as components
import random

# CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="Conty - UNAM 1704",
    page_icon="🧮",
    layout="centered"
)

# INFORMACIÓN TEXTUAL ÍNTEGRA DEL PLAN 1704 (Base de Conocimiento)
SYLLABUS_1704 = """


UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO ESCUELA NACIONAL PREPARATORIA
Plan de estudios 1996
Programa
Contabilidad y Gestión Administrativa
Clave 1704	Semestre / Año
6to.	Créditos 12	Área	III Ciencias Sociales
			Campo de
conocimiento	Histórico-social
			Etapa	Propedéutica

Modalidad	
Curso (X) Taller ( ) Lab. ( ) Sem. ( )	
Tipo	
T (X)	P ( )	T/P ( )

Carácter	Obligatorio ( ) Optativo ( )
Obligatorio de elección ( )
Optativo de elección (X)	
Horas
	Semana	Semestre / Año
	Teóricas 3	Teóricas 90
	Prácticas 0	Prácticas 0
	Total 3	Total 90

Seriación
Ninguna (X)
Obligatoria ( )
Asignatura antecedente	
Asignatura subsecuente	
Indicativa ( )
Asignatura antecedente	
Asignatura subsecuente	








Aprobado por el H. Consejo Técnico el 13 de abril 2018


1
 
I.	Presentación

La asignatura de Contabilidad y Gestión Administrativa dirige y encausa al alumno en el desarrollo de una sólida formación académica con conocimientos y habilidades administrativas, económicas y contables, así como la identificación de los fundamentos legales que apoyen en la creación de una actitud analítica, propositiva y de servicio, para generar una riqueza intelectual y aplicar alternativas de solución a situaciones cotidianas que se le presenten como: problemas de carácter contable, toma de decisiones en relación a la administración de los recursos, entre otros; todo ello mediante la comprensión del contexto socioeconómico y de las organizaciones actuales.

La asignatura proporciona un enfoque interdisciplinario e integral al conjuntar y vincular en un todo aquellos elementos contables y administrativos que son la base para el desarrollo de una visión en planeación estratégica y prospectiva, a través del análisis de los fenómenos socioeconómicos desde una postura humanística, modelos de negocios actuales y desarrollo de habilidades requeridas en los sectores público y privado, con responsabilidad y compromiso ciudadano, fomentando en el alumno el deseo de continuar aprendiendo por iniciativa propia.

Esta asignatura permite el desarrollo de forma integral al vincular toda la experiencia previa con los conocimientos académicos, técnicos, conceptuales e incluso culturales que se adquieren durante su proceso de formación académica, proyectándolo a la solución de problemas en situaciones cotidianas reales para el alumno.

El programa contempla cinco unidades en las cuales están incluidos los contenidos conceptuales, procedimentales y actitudinales que permiten el logro de los objetivos de esta asignatura. La primera unidad comprende la clasificación, derechos, obligaciones y requisitos de organizaciones y comerciantes, como los títulos de crédito en las operaciones mercantiles. Las teorías y técnicas administrativas concretas en el contexto de las organizaciones (empresas) actuales, sus recursos y organización conforman la segunda unidad. La tercera unidad refiere la vinculación de las bases de organización de la administración y el análisis de la cuenta pública. Los contenidos anteriores se relacionan de forma contable en la cuarta unidad a través de los métodos de registro de las actividades cotidianas en las organizaciones, análisis e interpretación de la información financiera. Finalmente, la última unidad se enfoca, como factor esencial, al capital humano y su relación directa con la organización.

Con respecto al perfil de egreso, la asignatura aporta: a) la identificación de los procedimientos de búsqueda, selección y organización de la información procedentes de diversas fuentes y campos disciplinarios relacionados con la contabilidad y la administración; b) la motivación para proponer soluciones a problemas de su entorno natural y social referidos a la administración de recursos mediante la aplicación de principios, métodos, técnicas y lenguajes de estas disciplinas; y c) favorece una mentalidad flexible y abierta a la innovación, adopción de hábitos de estudio y trabajo colaborativo.

II.	Objetivo general
 
El alumno establecerá la vinculación de los conocimientos previos con temas administrativos y contables de actualidad mediante la aplicación de principios, métodos, procedimientos, técnicas, considerando la interdisciplinariedad de los contenidos, aplicando el razonamiento contable financiero en la comprensión y representación de aquellos elementos que integralmente se presentan de forma directa o indirecta, para la traducción de objetivos, solución de problemas de carácter personal, toma de decisiones y defensa de una postura propia estableciendo la relación con los medios de información y comunicación.


III.	Unidades y número de horas

Unidad 1. Las organizaciones y su ámbito
Número de horas: 15

Unidad 2. La Administración contemporánea y el entorno
Número de horas:18

Unidad 3. Estructura administrativa de las instituciones públicas
Número de horas: 6

Unidad 4. La práctica contable en las organizaciones
Número de horas: 36

Unidad 5. El capital humano y las tendencias actuales
Número de horas 15


IV.	Descripción por unidad

Unidad 1. Las organizaciones y su ámbito Objetivo específico
El alumno:

●	Analizará los elementos y características del comercio, comercio electrónico y títulos de crédito, identificando los requisitos, marco legal y responsabilidad social de la empresa refiriendo los derechos y obligaciones de los comerciantes con el fin de actuar en un marco de legalidad al incursionar en el ámbito comercial y valorará las empresas como generadoras de empleo, desarrollo social y económico del país.
 
1.1	Concepto, elementos y clasificación de empresa, comercio y comercio electrónico
1.2	Funcionamiento de una empresa: requisitos, marco legal y responsabilidad social
1.3	Derechos y obligaciones legales de los comerciantes
1.4	Concepto, elementos y sujetos de títulos de crédito (cheque, pagaré y contratos adicionados)

Contenidos procedimentales

1.5	Comparación entre acto de comercio, comercio y comercio electrónico
1.6	Explicación (oral o escrita) de los requisitos, marco legal y responsabilidad social de una empresa
1.7	Investigación de la normatividad referente a derechos y obligaciones de los comerciantes en fuentes impresas y/o electrónicas
1.8	Ejemplificación de empresas según su capital, giro, finalidad, dimensión o tipo
1.9	Identificación de tipos, elementos y sujetos del cheque, pagaré y contratos adicionados

Contenidos actitudinales

1.10	Disposición para actuar en un marco de legalidad al incursionar en el ámbito comercial
1.11	Valoración de las empresas como generadoras de empleos, desarrollo social y económico del país
1.12	Aplicación de la ética en los negocios, transacciones comerciales, elaboración y manejo de los títulos de crédito (cheque, pagaré y contratos adicionados)

Unidad 2. La Administración contemporánea y el entorno Objetivo específico
El alumno:

●	Reflexionará y describirá las características, elementos, herramientas y aplicación de la administración mediante la identificación de las principales aportaciones de las teorías y escuelas administrativas, proceso administrativo, áreas funcionales, recursos que conforman la empresa, así como de la vinculación de las teorías modernas de la administración y los modelos administrativos actuales, todo lo anterior con el fin de desarrollar un pensamiento científico al valorar la trascendencia de la aplicación de la administración en el ámbito empresarial y, del mismo modo, promover una mentalidad crítica, flexible y abierta para la resolución de problemas y la toma de decisiones.
 
2.1	Conceptos básicos, características, elementos y campo laboral de la administración
2.2	Principales teorías, escuelas administrativas y su aplicación en la actualidad
2.3	Tendencias actuales de la administración
2.4	Proceso administrativo
2.5	Recursos que conforman la empresa
2.6	Áreas funcionales y estructura organizacional
2.7	Sistema de control de calidad aplicable en la empresa: concepto y elementos

Contenidos procedimentales

2.8	Búsqueda y descripción de las características, elementos y aplicación de la administración en el campo laboral
2.9	Análisis de las principales aportaciones de las teorías y escuelas administrativas
2.10	Vinculación entre las teorías modernas de la administración y los modelos administrativos actuales
2.11	Análisis de características y herramientas propias de las etapas del proceso administrativo
2.12	Identificación y explicación de los recursos que conforman a la empresa
2.13	Representación mediante organigramas de las principales áreas funcionales, sus actividades y utilidad
2.14	Identificación y descripción de los sistemas de control de calidad aplicados en la empresa

Contenidos actitudinales

2.15	Valoración de la trascendencia de la administración en el ámbito empresarial y en la vida diaria
2.16	Reconocimiento del pensamiento científico en la administración y la aplicación de esta mediante la experiencia
2.17	Disposición para asumir una mentalidad crítica, flexible y abierta en la resolución de problemas y la toma de decisiones

Unidad 3. Estructura administrativa de las instituciones públicas Objetivo específico
El alumno:

●	Identificará el marco normativo, clasificación y elementos que integran la Administración Pública, así como el origen y los propósitos de la cuenta pública, desarrollando actividades escolares específicas de investigación con el fin de enriquecer su formación como ciudadano comprometido, solidario y responsable con la sociedad.
 
3.1	Marco normativo de la Administración Pública y su clasificación
3.2	Principales elementos de la Cuenta Pública

Contenidos procedimentales

3.3	Explicación (oral o escrita) del sustento legal de la Administración Pública (Federal) y su clasificación
3.4	Explicación (oral o escrita) de los elementos integrales, propósitos y origen de la cuenta pública

Contenidos actitudinales

3.5	Aceptación de sí como ciudadano comprometido, solidario y responsable con la sociedad
3.6	Disposición para consultar fuentes bibliográficas y hemerográficas específicas

Unidad 4. La práctica contable en las organizaciones Objetivo específico
El alumno:

●	Identificará y analizará los elementos, postulados, marco legal de la contabilidad y la clasificación vigente de las cuentas como parte integral de los estados financieros básicos; del mismo modo, las contribuciones del Impuesto Sobre la Renta (ISR) y el Impuesto al Valor Agregado (IVA), lo anterior a partir de la resolución de casos prácticos y el uso de las Tecnologías de la Información y Comunicación (TIC) o las Tecnologías del Aprendizaje y del Conocimiento (TAC), con el fin de asumir una actuación basada en el marco de legalidad en el ámbito empresarial y gubernamental.

Contenidos conceptuales

4.1	Concepto, fundamento legal, elementos y campo laboral de la Contabilidad
4.2	Las cuentas:
a)	Concepto y elementos
b)	Clasificación y catálogo
4.3	Tipos de contribuciones vigentes: ISR, IVA, entre otros
4.4	Estados Financieros Básicos
4.5	La contabilidad electrónica y los Comprobantes Fiscales Digitales por Internet (CFDI)
4.6	TIC y TAC en la contabilidad

Contenidos procedimentales
 
4.7	Identificación del marco legal, principales elementos y postulados que integran el concepto de contabilidad
4.8	Vinculación de las Normas de Información Financiera (NIF) en la contabilidad
4.9	Descripción del ámbito de la contabilidad y las áreas de oportunidad para su ejercicio
4.10	Identificación de elementos y aplicación de la partida doble
4.11	Análisis de la clasificación vigente de las cuentas según su naturaleza y características principales
4.12	Integración de elementos que conforman el catálogo de cuentas
4.13	Identificación del concepto de contribuciones y clasificación: ISR e IVA
4.14	Resolución de casos prácticos contables
4.15	Elaboración de los principales estados financieros (balance general o estado de situación financiera y estado de resultados)
4.16	Investigación de requisitos y elementos de la contabilidad electrónica en fuentes impresas y digitales
4.17	Utilización de hojas de cálculo, aplicaciones y/o software especializado para la contabilidad

Contenidos actitudinales

4.18	Disposición para actuar en un marco de legalidad al incursionar en el ámbito contable
4.19	Valoración de la trascendencia de la contabilidad en el ámbito empresarial y gubernamental
4.20	Reconocimiento de los principios éticos en la práctica profesional contable
4.21	Responsabilidad ética en el registro de las operaciones contables

Unidad 5. El capital humano y las tendencias actuales Objetivo específico
El alumno:

●	Conocerá e identificará, dentro de la relación del capital humano y las organizaciones, los principales tipos de contratación y los elementos contractuales que le representan al trabajador (ingresos, erogaciones y prestaciones de ley), a partir de la realización de casos prácticos con la finalidad de vincular la teoría con alguna solución a problemas en los diferentes escenarios laborales donde se requieran hacer valer los derechos del trabajador.


Contenidos conceptuales

5.1	Modelos de contratación actual
5.2	Prestaciones de ley
 
5.3	Elementos principales que integran la nómina
5.4	El sistema de retiro

Contenidos procedimentales

5.5	Análisis de los modelos de contratación: Independiente, Asimilado y Subordinado
5.6	Investigación de las prestaciones mínimas de ley entre otras
5.7	Clasificación de los elementos que integran la nómina y prestaciones mínimas de ley vigente
5.8	Resolución de casos prácticos relacionados con los modelos de contratación
5.9	Investigación de las opciones en el sistema de retiro

Contenidos actitudinales

5.10	Valoración del impacto de los nuevos modelos de contratación en el ámbito empresarial y laboral
5.11	Toma de conciencia respecto a los problemas y desafíos de la realidad y la importancia de los derechos laborales


V.	Sugerencias de trabajo

Se sugiere que las estrategias didácticas se centren en el aprendizaje del alumno, el manejo de distintas fuentes de información, materiales educativos en formatos diversos y el desarrollo de actividades que favorezcan la adquisición y construcción de conocimientos, así como el desarrollo de habilidades transversales y específicas de la disciplina, para su aplicación en el ámbito académico y en el relacionado con los escenarios de la vida cotidiana, la actualidad y el futuro inmediato. En suma, se trata de que las tareas de enseñanza y aprendizaje promuevan en el alumno el desarrollo de conocimientos, habilidades, actitudes y valores necesarios para el análisis, mediante:

●	El desarrollo de habilidades de pensamiento, comunicación, adquisición de nuevos conocimientos disciplinares y transversales.

●	La activación de los conocimientos previos y la inducción a los nuevos contenidos de aprendizaje.

●	La promoción de aprendizajes significativos en contextos reales, atractivos y que aborden temas relevantes de actualidad, como el impacto de la innovación tecnológica en el ejercicio profesional.

●	La motivación para que valore las ventajas de representar un problema mediante los posibles supuestos para reducir su complejidad, visualizarlo, comprenderlo, relacionarlo y solucionarlo bajo el enfoque más efectivo.
 
●	La búsqueda de información y recursos de apoyo, en fuentes confiables, respetando los derechos de autor mediante el uso de referencias y citas en un formato establecido (sistema APA).

●	La identificación de algún software especializado (como por ejemplo, Conta2000, Compact, entre otros) que permita visualizar, experimentar y manipular diferentes casos de aplicación contable.

Del mismo modo, es necesario incluir estrategias que ubiquen a los alumnos en el centro del proceso educativo y realizar trabajos a través de:

●	Exposiciones vinculando los conocimientos, eventos y fenómenos que se presentan de manera cotidiana, haciendo el análisis de estos elementos mediante una visión integrada, coherente; asimismo, sensibilizar, problematizar y despertar el interés al organizar la información bajo criterios de vida como introducción a la presentación de resultados e incluso conclusiones de aplicación práctica en situaciones futuras.

●	Actividades colaborativas favoreciendo el desarrollo de múltiples capacidades, habilidades y actitudes positivas en los alumnos al aprender a exponer conceptos, teorías y fundamentos, al discutir, problemas e incluso proponer soluciones o propuestas de forma analítica, con una postura particular y grupal.

●	Trabajos de investigación y/o proyectos fomentando el aprendizaje colaborativo (en tiempos largos) y acercando al alumno a una realidad concreta desde un ambiente académico, asimismo estimular el desarrollo de habilidades para resolver situaciones reales.

●	Prácticas que fortalezcan el aprendizaje interactivo, al explicar el proceso a seguir y resolviendo las dudas de los alumnos, proporcionando estrategias para analizar y resolver problemas e identificando el nivel de conocimientos y comprensión de los alumnos para aplicar la teoría a la práctica.

●	Trabajo con Casos y Aprendizaje basado en problemas al generan la elaboración de análisis y opiniones razonadas sobre alternativas de solución, logrando establecer un sistema de recopilación de datos bajo un contexto propio y un entendimiento de su realidad.

●	Discusión de pequeños grupos mediante la comunicación y participación de todo el grupo hasta llegar a conclusiones o acuerdos.

●	Redes semánticas o mapas conceptuales gestionando de modo óptimo la expresión de posturas o propuestas en forma de cadena, por ramificaciones o niveles jerárquicos
 
mediante el enlace de ideas, conceptos, proposiciones y/o palabras de enlace, logrando con ello una visión sintética e integradora, además de valorar los niveles de concreción del aprendizaje.


VI.	Sugerencias de evaluación del aprendizaje

Se sugiere que los criterios e instrumentos para la evaluación del aprendizaje tomen como referencia esencial los contenidos conceptuales, procedimentales y actitudinales, tanto de orden disciplinar como transversal, previstos en el objetivo general y los específicos del programa, en el desglose de las unidades temáticas y en las sugerencias de trabajo. De ahí que sea necesario evaluar en los alumnos los procesos y productos presentados bajo criterios coherentes con el enfoque disciplinar y didáctico de la asignatura, la habilidad de análisis de la actualidad desde una perspectiva que integre los distintos aspectos de la realidad, de acuerdo con la estructura interna de la disciplina, reforzando la habilidad para elaborar proyectos de investigación que expliquen procesos con la utilización de información procedente de fuentes diversas en formatos tradicionales o asociados a las tecnologías tanto de forma individual como colaborativa.

Asimismo, llevar a cabo una evaluación continua, rigurosa y sistemática, tanto en su carácter cuantitativo como cualitativo, con la finalidad de que permita a los alumnos apreciar sus logros y, a los profesores, hacer con oportunidad los ajustes pertinentes para alcanzar los aprendizajes previstos; siempre contando con una actitud crítica y consciente de los conocimientos conceptuales, procedimentales y actitudinales, de igual manera, se requiere de la implementación de instrumentos que van más allá de las pruebas objetivas por lo que se recomiendan utilizar rúbricas. Lo anterior, considerando como evidencias los exámenes, trabajos y tareas, presentación de tema, participación en clase, rúbricas, listas de cotejo, ensayos, reseñas, exposiciones, aprendizaje basado en problemas, análisis de casos, portafolio de evidencias, aprendizaje mediante proyectos, así como las de trabajo cotidiano y aquellas antes contempladas.





VII.	Fuentes básicas

Álvarez, M. R. y Morales, J. A. (2014). Contabilidad de Sociedades. México: Planeta. Castro, P. (2016). Preguntas y Respuestas sobre Contabilidad Digital. México: ISEF.
Celaya, R. (2013). Contabilidad Básica: Un Enfoque basado en Competencias. México: Cengage Learnin.
Chiavenato, I. (2016). Administración de Recursos Humanos: el capital humano de las organizaciones. (9a. Ed.). México: Mc Graw Hill Interamericana.
 
Contreras, A. L., Medina, C. C. y Padilla, G. (2016). Introducción al Estudio de la Información Financiera. Un enfoque para el futuro administrador. México: Publicaciones Empresariales/FCyA/UNAM.
González, R., Yáñez, D. y Zaragoza, O. (2014). Administración I. México: Santillana.
Guajardo, G. y Andrade, N. E. (2014). Contabilidad Financiera. (6a. Ed.). México: Mc Graw-Hill Interamericana.
Guerrero, J. C., y Galindo, J. F. (2014). Contabilidad para administradores. México: Grupo editorial Patria.
Hernández, M. A., Galindo, M. I. y Hernández, J. (2015). Estudio Práctico de la Contabilidad Electrónica. México: ISEF.
Montijo, B. E. (2013). Títulos de Crédito: Manual práctico para el uso de cheques, pagarés, acciones y otros. México: Oxford.
Moreno, J. (2014). Contabilidad de Sociedades. México: Grupo editorial Patria. Paolini, N. A., y Álvarez, D. (2013). El Proceso Administrativo. La Plata: Haber. Pérez, V. L. (2014). Contabilidad I. México: Santillana.
Romero, Á. J. (2013). Contabilidad Práctica para no Contadores. México: Mc Graw Hill Interamericana.
Romero, Á. J. (2014) Principios de contabilidad. Mc Graw Hill Interamericana. Quinta Edición.
Secretaria de Gobernación. (11 de enero de 2018) Leyes Federales Vigentes. Diario oficial de la federación. Recuperado de: http://www.diputados.gob.mx/LeyesBiblio/index.htm


VIII.	Fuentes complementarias

Cadavid, L. A., Valencia, H., y Cardona, J. (2014) Fundamentos de derecho comercial, tributario y contable. Bogota: Mc Graw Hill Interamericana.
Cámara	de	Diputados	(2016)	Auditoria	Superior	de	la	Federación.	Recuperado	de http://www.asf.gob.mx
Comisión Nacional del Sistema de Ahorro para el Retiro. (s.f.) GOB. Recuperado de https://www.gob.mx/consar
CONCANACO/SERVYTUR.	(s.f.)	Revista.	Recuperado	de http://www.concanaco.com.mx/category/revista/
Diez, I. (2012). Introduction to business administration. Madrid: Civitas.
GOB. (s.f) Portal único de trámites, información y participación ciudadana. Recuperado de https://www.gob.mx/se/
Instituto Nacional de Estadística y Geografía. (s.f.) Recuperado de http://www.inegi.org.mx/ Lara, E. (2017). Primer curso de contabilidad. (22a. Ed.). México: Trillas.
Moreno, J. A. (2014). Contabilidad Básica. México: Patria.
Münch, L. y García, J. G. (2015). Fundamentos de administración. (11a. Ed.). México: Editorial Trillas.
Navarro, E. (2013). The basics of financial accounting II. Madrid: Edisofer S.L. Revista Emprendedores. (s.f.) Recuperado de http://emprendedores.unam.mx/ Reyes, Agustín. (2013). Administración Moderna. (7a. Ed.) México: Limusa.
 
Secretaría del Trabajo y Previsión Social. (s.f.) Recuperado de https://www.gob.mx/stps/ Servicio de Administración Tributaria (SAT). Recuperado de http://sat.gob.mx
UAEM. Sistema de Información Científica Redalyc. Red de Revistas Científicas de América Latina y el Caribe, España y Portugal. (s.f.) Recuperado de http://www.redalyc.org/BusquedaRevistaPorNombre.oa?q=comercio%20electronico
UNAM / FCA / SUAyED. (2017) Materiales Digitales: Plan de Estudios Actualizados. Recuperado de http://fcasua.contad.unam.mx/apuntes/interiores/plan2016_1.php

"""

# ESTILO CSS PERSONALIZADO
st.markdown("""
<style>
    .stApp { background-color: #f8fafc; }
    .main-header {
        text-align: center;
        background: #1e293b;
        padding: 1.5rem;
        border-radius: 10px;
       color: #1a365d; /* Aquí cambiamos el blanco por azul marino */
        border-bottom: 4px solid #fbbf24;
        margin-bottom: 2rem;
    }

    /* --- AGREGA ESTO JUSTO AQUÍ PARA EL CHAT --- */
    [data-testid="stChatMessage"] p {
        color: #1a365d !important;
    }
    
    .stApp {
        color: #1a365d;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header"><h1>🧮 Conty: Gestión Administrativa 1704</h1></div>', unsafe_allow_html=True)

# LÓGICA DE MENSAJES Y TOKENIZACIÓN
if "messages" not in st.session_state:
    st.session_state.messages = []

# PROMPT DEL SISTEMA (Configuración de comportamiento)
SYSTEM_PROMPT = f"""Eres CONTY, asistente de Andy la coordinadora del área de sociales y humanidades del instituto juventud. Tu base de datos es TEXTUALMENTE esta: {SYLLABUS_1704}.
REGLAS CRÍTICAS:
1. Responde siempre de forma meticulosa y proactiva a Andy.
2. Usa un máximo de 4000 tokens.
3. Si el contenido que estás generando es muy extenso o sientes que no has terminado de explicar un punto complejo, DEBES detenerte y preguntar textualmente: '¿Gustas que continúe con el siguiente apartado, Andy?'.
4. CIERRE: Finaliza con un comentario resiliente, un ejercicio de conceptos contables o un recordatorio de hidratación para Andy
5. Recuerda que no es una estudiante sino una coordinadora academica muy profesional y dedicada.
6. Si pide planear algun periodo preguntale cuantas horas posee, cuantas unidades y cuantas horas tiene destinadas para cada unidad"""

# CHAT INTERFACE
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Andy, escribe aquí tu consulta sobre el Plan 1704..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            client = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=st.secrets["GROQ_API_KEY"])
            
            # Petición con límite de 4000 tokens
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "system", "content": SYSTEM_PROMPT}] + st.session_state.messages,
                max_tokens=4000,
                temperature=0.4
            )
            
            full_response = response.choices[0].message.content
            st.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            st.error(f"Error en la auditoría del sistema, Andy: {e}")

# BOTÓN DE REINICIO
if st.sidebar.button("Borrar Balance (Reset)"):
    st.session_state.messages = []
    st.rerun()
