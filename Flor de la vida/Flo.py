# ==============================
# PRACTICA 1 - FLOR DE LA VIDA
# ==============================

# -------- PASO 1: IMPORTAR LIBRERIAS --------
import bpy
import math

# -------- PASO 2: LIMPIAR ESCENA --------
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# -------- PASO 3: DEFINICION DE VARIABLES --------
radio = 2                # Radio del círculo
angulo_actual = 0        # Ángulo inicial
paso = 80

             # Incremento en grados

# -------- PASO 4: CIRCULO CENTRAL --------
bpy.ops.mesh.primitive_circle_add(
    radius=radio,
    location=(0, 0, 0)
)

# -------- PASO 5: ESTRUCTURA WHILE --------
while angulo_actual < 360:

    # Convertir grados a radianes
    angulo_radianes = math.radians(angulo_actual)

    # Calcular coordenadas cartesianas
    x = radio * math.cos(angulo_radianes)
    y = radio * math.sin(angulo_radianes)

    # Crear círculo en nueva posición
    bpy.ops.mesh.primitive_circle_add(
        radius=radio,
        location=(x, y, 0)
    )

    # Incrementar ángulo
    angulo_actual += paso
