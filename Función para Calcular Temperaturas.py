# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Días de la semana (7 días)
# Tercera dimensión: Semanas (4 semanas)
temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"day": "Lunes", "temp": 76},
            {"day": "Martes", "temp": 87},
            {"day": "Miércoles", "temp": 84},
            {"day": "Jueves", "temp": 76},
            {"day": "Viernes", "temp": 75},
            {"day": "Sábado", "temp": 89},
            {"day": "Domingo", "temp": 72}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 73},
            {"day": "Martes", "temp": 79},
            {"day": "Miércoles", "temp": 86},
            {"day": "Jueves", "temp": 88},
            {"day": "Viernes", "temp": 87},
            {"day": "Sábado", "temp": 90},
            {"day": "Domingo", "temp": 83}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 67},
            {"day": "Martes", "temp": 84},
            {"day": "Miércoles", "temp": 86},
            {"day": "Jueves", "temp": 88},
            {"day": "Viernes", "temp": 83},
            {"day": "Sábado", "temp": 86},
            {"day": "Domingo", "temp": 85}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 75},
            {"day": "Martes", "temp": 76},
            {"day": "Miércoles", "temp": 81},
            {"day": "Jueves", "temp": 79},
            {"day": "Viernes", "temp": 85},
            {"day": "Sábado", "temp": 86},
            {"day": "Domingo", "temp": 81}
        ]
    ],
    [   # Ciudad 2
        [   # Semana 1
            {"day": "Lunes", "temp": 66},
            {"day": "Martes", "temp": 64},
            {"day": "Miércoles", "temp": 78},
            {"day": "Jueves", "temp": 74},
            {"day": "Viernes", "temp": 73},
            {"day": "Sábado", "temp": 79},
            {"day": "Domingo", "temp": 75}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 63},
            {"day": "Martes", "temp": 76},
            {"day": "Miércoles", "temp": 70},
            {"day": "Jueves", "temp": 82},
            {"day": "Viernes", "temp": 85},
            {"day": "Sábado", "temp": 77},
            {"day": "Domingo", "temp": 91}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 81},
            {"day": "Martes", "temp": 85},
            {"day": "Miércoles", "temp": 88},
            {"day": "Jueves", "temp": 90},
            {"day": "Viernes", "temp": 82},
            {"day": "Sábado", "temp": 86},
            {"day": "Domingo", "temp": 70}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 69},
            {"day": "Martes", "temp": 67},
            {"day": "Miércoles", "temp": 69},
            {"day": "Jueves", "temp": 71},
            {"day": "Viernes", "temp": 84},
            {"day": "Sábado", "temp": 77},
            {"day": "Domingo", "temp": 80}
        ]
    ],
    [   # Ciudad 3
        [   # Semana 1
            {"day": "Lunes", "temp": 60},
            {"day": "Martes", "temp": 62},
            {"day": "Miércoles", "temp": 64},
            {"day": "Jueves", "temp": 61},
            {"day": "Viernes", "temp": 68},
            {"day": "Sábado", "temp": 65},
            {"day": "Domingo", "temp": 62}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 79},
            {"day": "Martes", "temp": 78},
            {"day": "Miércoles", "temp": 73},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 77},
            {"day": "Sábado", "temp": 74},
            {"day": "Domingo", "temp": 71}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 81},
            {"day": "Martes", "temp": 83},
            {"day": "Miércoles", "temp": 85},
            {"day": "Jueves", "temp": 82},
            {"day": "Viernes", "temp": 89},
            {"day": "Sábado", "temp": 86},
            {"day": "Domingo", "temp": 83}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 75},
            {"day": "Martes", "temp": 80},
            {"day": "Miércoles", "temp": 82},
            {"day": "Jueves", "temp": 79},
            {"day": "Viernes", "temp": 76},
            {"day": "Sábado", "temp": 73},
            {"day": "Domingo", "temp": 70}
        ]
    ]
]

def calcular_temperatura_promedio(datos_temperaturas):
    """
    Calcula la temperatura promedio de cada ciudad.

    :param datos_temperaturas: Diccionario donde las claves son los nombres de las ciudades
                               y los valores son listas con las temperaturas semanales.
    :return: Diccionario con la temperatura promedio de cada ciudad.
    """
    promedios = {}
    for ciudad, temperaturas in datos_temperaturas.items():
        total_dias = sum(len(semana) for semana in temperaturas)  # Cuenta los días registrados
        suma_total = sum(sum(semana) for semana in temperaturas)  # Suma todas las temperaturas
        promedios[ciudad] = suma_total / total_dias  # Calcula el promedio
    return promedios


# Datos de ejemplo: 3 ciudades, 4 semanas (cada semana con 7 días)
datos = {
    "Ciudad A": [[76, 87, 84, 76, 75, 89, 72], [73, 79, 86, 88, 87, 90, 83], [67, 84, 86, 88, 83, 86, 85], [75, 76, 81, 79, 85, 86, 81]],
    "Ciudad B": [[66, 64, 78, 74, 73, 79, 75], [63, 76, 70, 82, 85, 77, 91], [81, 85, 88, 90, 82, 86, 70], [69, 67, 69, 71, 84, 77, 80]],
    "Ciudad C": [[60, 62, 64, 61, 68, 65, 62], [79, 78, 73, 70, 77, 74, 71], [81, 83, 85, 82, 89, 86, 83], [75, 80, 82, 79, 76, 73, 70]]
}

# Llamar la función y mostrar los resultados
resultado = calcular_temperatura_promedio(datos)
print("Temperaturas promedio por ciudad:", resultado)