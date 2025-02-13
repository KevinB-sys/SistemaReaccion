from flask import Flask, request, jsonify, render_template

# Crea una instancia de Flask
app = Flask(__name__)

base_conocimiento = {
    "inicio":{
        "pregunta": "¿Qué deseas conocer?",
        "respuestas":{
            "Galaxias": "Galaxias",
            "Estrellas": "Estrellas",
            "Planetas": "Planetas",
            "Fenomenos_Cosmicos": "Fenomenos_Cosmicos",
            "Exploracion_espacial": "Exploracion_espacial"
        }
    },
    # Aqui para el desglose de la opcion 1 (Galaxias)
    "Galaxias": {
        "pregunta": "¿Que quieres saber sobre las galaxias?",
        "respuestas": {
            "Tipos_de_galaxias": "Tipos_de_galaxias",
            "Estructuras_internas": "Estructuras_internas",
            "Interacciones": "Interacciones"
        }
    },
    "Tipos_de_galaxias": {
        "pregunta": "¿Que tipo deseas conocer?",
        "respuestas": {
            "Elipticas": "Elipticas",
            "Espirales": "Espirales"
        }
    },
    "Estructuras_internas": {
        "pregunta": "¿Que estructura deseas conocer?",
        "respuestas": {
            "Nucleo_galactico": "Nucleo_galactico",
            "Brazos": "Brazos"
        }
    },
    "Interacciones": {
        "pregunta": "¿Que tipo de interaccion deseas conocer?",
        "respuestas": {
            "Fusiones": "Fusiones",
            "Colisiones": "Colisiones"
        }
    },
    # Respuestas finales de la opcion 1 (Galaxias)
    "Elipticas": {
        "respuesta_final": "Las galaxias elipticas son aquellas que tienen forma de elipse y son las mas comunes en el universo."
    },
    "Espirales": {
        "respuesta_final": "Las galaxias espirales son aquellas que tienen forma de espiral y son las mas comunes en el universo."
    },
    "Nucleo_galactico": {
        "respuesta_final": "El nucleo galactico es el centro de la galaxia, donde se encuentra un agujero negro supermasivo."
    },
    "Brazos":{
        "respuesta_final": "Los brazos son estructuras en forma de espiral que se extienden desde el núcleo galáctico hacia los bordes."
    },
    "Fusiones": {
        "respuesta_final": "Las fusiones son interacciones entre galaxias que pueden dar origen a nuevas galaxias."
    },
    "Colisiones": {
        "respuesta_final": "Las colisiones son interacciones entre galaxias que pueden dar origen a nuevas galaxias."
    },

    # Aqui desglose de la opcion 2 (Estrellas)
    "Estrellas": {
        "pregunta": "¿Que quieres saber sobre las estrellas? ",
        "respuestas": {
            "Ciclo_de_vida": "Ciclo_de_vida",
            "Tipos_de_estrellas": "Tipos_de_estrellas",
            "Impacto_en_el_entorno": "Impacto_en_el_entorno"
        }
    },
    "Ciclo_de_vida": {
        "pregunta": "¿Que etapa deseas conocer? ",
        "respuestas": {
            "Formacion": "Formacion",
            "Vida_media": "Vida_media"
        }
    },
    "Tipos_de_estrellas": {
        "pregunta": "¿Que tipo deseas conocer? ",
        "respuestas": {
            "Gigantes": "Gigantes",
            "Enanas": "Enanas"
        }
    },
    "Impacto_en_el_entorno": {
        "pregunta": "¿Que aspecto deseas conocer? ",
        "respuestas": {
            "Radiacion": "Radiacion",
            "Agujeros_negros": "Agujeros_negros"
        }
    },
    # Respuestas finales de la opcion 2 (Estrellas)
    "Formacion": {
        "respuesta_final": "Las estrellas se forman en nebulosas a partir del colapso gravitacional de gas y polvo."
    },
    "Vida_media": {
        "respuesta_final": "La vida media de una estrella depende de su masa: las más grandes viven menos tiempo que las pequeñas."
    },
    "Gigantes": {
        "respuesta_final": "Las estrellas gigantes son enormes y muy luminosas, pero tienen vidas relativamente cortas."
    },
    "Enanas": {
        "respuesta_final": "Las estrellas enanas son pequeñas y menos luminosas, pero pueden vivir miles de millones de años."
    },
    "Radiacion": {
        "respuesta_final": "La radiacion de las estrellas calienta y alimenta la formación de vida en los planetas cercanos."
    },
    "Agujeros_negros": {
        "respuesta_final": "Los agujeros negros son objetos formados por estrellas colapsadas, con una gravedad tan intensa que nada puede escapar."
    },

    # Aqui desglose de la opcion 3 (Planetas)
    "Planetas": {
        "pregunta": "¿Que quieres saber sobre los planetas? ",
        "respuestas": {
            "Tipos_de_planetas": "Tipos_de_planetas",
            "Caracteristicas": "Caracteristicas",
            "Exploracion_de_planetas": "Exploracion_de_planetas"
        }
    },
    "Tipos_de_planetas": {
        "pregunta": "¿Que tipo deseas conocer? ",
        "respuestas": {
            "Rocosos": "Rocosos",
            "Gaseosos": "Gaseosos"
        }
    },
    "Caracteristicas": {
        "pregunta": "¿Que característica deseas conocer?",
        "respuestas": {
            "Tamano": "Tamano",
            "Clima": "Clima"
        }
    },
    "Exploracion_de_planetas": {
        "pregunta": "¿Que método deseas conocer? ",
        "respuestas": {
            "Rovers": "Rovers",
            "Telescopios": "Telescopios"
        }
    },
    # Respuestas finales de la opcion 3 (Planetas)
    "Rocosos": {
        "respuesta_final": "Los planetas rocosos tienen superficies sólidas y son los más cercanos al sol."
    },
    "Gaseosos": {
        "respuesta_final": "Los planetas gaseosos están formados principalmente por gases y no tienen una superficie sólida."
    },
    "Tamano": {
        "respuesta_final": "El tamaño de los planetas varía enormemente, desde pequeños como Marte hasta gigantes como Júpiter."
    },
    "Clima": {
        "respuesta_final": "El clima de un planeta depende de su atmósfera, distancia al sol y otros factores."
    },
    "Rovers": {
        "respuesta_final": "Los rovers son vehículos robotizados que exploran la superficie de los planetas."
    },
    "Telescopios": {
        "respuesta_final": "Los telescopios permiten observar y estudiar planetas desde la Tierra o el espacio."
    },
    
    # Opción 4: Fenómenos Cósmicos
    "Fenomenos_Cosmicos": {
        "pregunta": "¿Qué fenómeno cósmico deseas explorar? ",
        "respuestas": {
            "Agujeros_negros": "Agujeros_negros",
            "Supernovas": "Supernovas",
            "Ondas_gravitacionales": "Ondas_gravitacionales"
        }
    },
    "Agujeros_negros": {
        "pregunta": "¿Qué aspecto de los agujeros negros deseas conocer?",
        "respuestas": {
            "Formacion_agujeros_negros": "Formacion_agujeros_negros",
            "Tipos_agujeros_negros": "Tipos_agujeros_negros"
        }
    },
    "Supernovas": {
        "pregunta": "¿Qué quieres saber sobre las supernovas?",
        "respuestas": {
            "Origen_supernovas": "Origen_supernovas",
            "Impacto_supernovas": "Impacto_supernovas"
        }
    },
    "Ondas_gravitacionales": {
        "pregunta": "¿Qué deseas aprender sobre las ondas gravitacionales? ",
        "respuestas": {
            "Descubrimiento_ondas": "Descubrimiento_ondas",
            "Aplicaciones_ondas": "Aplicaciones_ondas"
        }
    },
    # Respuestas finales de Fenómenos Cósmicos
    "Formacion_agujeros_negros": {
        "respuesta_final": "Los agujeros negros se forman cuando una estrella masiva colapsa al final de su vida."
    },
    "Tipos_agujeros_negros": {
        "respuesta_final": "Los agujeros negros se clasifican en tres tipos principales: estelares, supermasivos y de masa intermedia."
    },
    "Origen_supernovas": {
        "respuesta_final": "Las supernovas ocurren al final del ciclo de vida de una estrella masiva, liberando grandes cantidades de energía."
    },
    "Impacto_supernovas": {
        "respuesta_final": "Las supernovas enriquecen el universo con elementos pesados necesarios para la formación de nuevos sistemas planetarios."
    },
    "Descubrimiento_ondas": {
        "respuesta_final": "Las ondas gravitacionales fueron predichas por Einstein y detectadas por primera vez en 2015 por el experimento LIGO."
    },
    "Aplicaciones_ondas": {
        "respuesta_final": "Las ondas gravitacionales permiten a los científicos estudiar fenómenos cósmicos extremos como fusiones de agujeros negros."
    },

    # Opción 5: Exploración Espacial
    "Exploracion_espacial": {
        "pregunta": "¿Qué aspecto de la exploración espacial deseas investigar? ",
        "respuestas": {
            "Misiones_historicas": "Misiones_historicas",
            "Tecnologias_espaciales": "Tecnologias_espaciales",
            "Futuro_exploracion": "Futuro_exploracion"
        }
    },
    "Misiones_historicas": {
        "pregunta": "¿Qué misión histórica deseas conocer? ",
        "respuestas": {
            "Apolo_11": "Apolo_11",
            "Sputnik_1": "Sputnik_1"
        }
    },
    "Tecnologias_espaciales": {
        "pregunta": "¿Qué tecnología espacial deseas explorar? ",
        "respuestas": {
            "Cohetes": "Cohetes",
            "Satelites": "Satelites"
        }
    },
    "Futuro_exploracion": {
        "pregunta": "¿Qué aspecto del futuro de la exploración espacial deseas aprender? ",
        "respuestas": {
            "Colonizacion_Marte": "Colonizacion_Marte",
            "Viajes_interestelares": "Viajes_interestelares"
        }
    },
    # Respuestas finales de Exploración Espacial
    "Apolo_11": {
        "respuesta_final": "Apolo 11 fue la misión que llevó a los primeros humanos a la Luna en 1969."
    },
    "Sputnik_1": {
        "respuesta_final": "Sputnik 1 fue el primer satélite artificial lanzado por la Unión Soviética en 1957."
    },
    "Cohetes": {
        "respuesta_final": "Los cohetes son vehículos que utilizan propulsión para superar la gravedad terrestre y alcanzar el espacio."
    },
    "Satelites": {
        "respuesta_final": "Los satélites son objetos artificiales colocados en órbita para observación, comunicación y exploración."
    },
    "Colonizacion_Marte": {
        "respuesta_final": "La colonización de Marte es una meta futura para la humanidad, liderada por empresas como SpaceX y agencias como la NASA."
    },
    "Viajes_interestelares": {
        "respuesta_final": "Los viajes interestelares son un objetivo a largo plazo que requiere avances significativos en tecnología de propulsión."
    }
}

@app.route('/')
def index():
    # Página de inicio con la primera pregunta
    pregunta = base_conocimiento["inicio"]["pregunta"]
    opciones = base_conocimiento["inicio"]["respuestas"]
    return render_template('index.html', pregunta=pregunta, opciones=opciones)

@app.route('/pregunta', methods=['POST'])
def pregunta():
    data = request.get_json()  # Recibir datos como JSON
    opcion = data.get('opcion')  # Obtener la opción seleccionada
    print(f"Opción seleccionada: {opcion}")  # Línea de depuración

    if not opcion:
        return jsonify({"error": "No se envió ninguna opción"}), 400

    # Buscar la opción en la base de conocimiento utilizando la palabra
    nodo_actual = base_conocimiento.get(opcion)

    if not nodo_actual:
        return jsonify({"error": f"Opción no válida: {opcion}"}), 400

    if "pregunta" in nodo_actual:
        # Si el nodo tiene una pregunta y más respuestas
        return jsonify({
            "pregunta": nodo_actual["pregunta"],
            "respuestas": nodo_actual["respuestas"]
        })
    elif "respuesta_final" in nodo_actual:
        # Si el nodo contiene una respuesta final
        return jsonify({
            "respuesta_final": nodo_actual["respuesta_final"]
        })
    else:
        return jsonify({"error": "Nodo no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)