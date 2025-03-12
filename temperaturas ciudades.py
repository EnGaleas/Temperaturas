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

# Calcular el promedio de temperaturas para cada ciudad y semana
ciudades = ["Ciudad 1", "Ciudad 2", "Ciudad 3"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")