## Descripción General

Este script en Python para Blender genera una figura tipo Flor de la Vida, creando un círculo central y varios círculos alrededor distribuidos uniformemente en 360 grados.

La lógica principal se basa en:

Uso de coordenadas polares

Funciones trigonométricas (cos y sin)

Un ciclo while

Un incremento angular llamado paso

Mientras más pequeño sea el valor de paso, más círculos se generan.

Explicación Paso a Paso

1. Importación de librerías

```
import bpy
import math
```

- bpy: Permite controlar Blender mediante código.
- math: Se utiliza para funciones matemáticas como cos(), sin() y radians().

2. Limpieza de la escena

```
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
```
Selecciona todos los objetos existentes en la escena y los elimina.

Esto garantiza que el script genere la figura desde cero sin interferencias.

3. Definición de variables

```
radio = 2
angulo_actual = 0
paso = 5
```

- radio: Tamaño de cada círculo.
- angulo_actual: Ángulo inicial desde donde comenzará el recorrido.
- paso: Cantidad de grados que aumenta el ángulo en cada iteración.

El valor de paso es clave para determinar cuántos círculos se generan.

4. Creación del círculo central
```
bpy.ops.mesh.primitive_circle_add(
    radius=radio,
    location=(0, 0, 0)
)
```

Se crea un círculo en el origen (0,0,0).

Este es el círculo base de la figura.

5. Lógica del ciclo while

```
while angulo_actual < 360:
```

El ciclo se ejecuta hasta completar los 360 grados, es decir, una vuelta completa alrededor del centro.

6. Conversión de grados a radianes
```
angulo_radianes = math.radians(angulo_actual)
```
Las funciones trigonométricas en Python trabajan en radianes, por eso es necesario convertir los grados antes de usar cos y sin.

7. Cálculo de coordenadas
```
x = radio * math.cos(angulo_radianes)
y = radio * math.sin(angulo_radianes)
```
Se usan las fórmulas de coordenadas polares:

- x = r cos(θ)
- y = r sin(θ)

Esto permite posicionar cada círculo exactamente a una distancia igual al radio, pero en diferentes ángulos.

Así se distribuyen uniformemente alrededor del centro.

7. Creación de nuevos círculos


```
bpy.ops.mesh.primitive_circle_add(
    radius=radio,
    location=(x, y, 0)
)
```


Se crea un nuevo círculo en la posición calculada.

8. Incremento del ángulo

```angulo_actual += paso
```

En cada iteración, el ángulo aumenta según el valor de paso.

Aquí es donde se controla la cantidad de círculos generados.

Relación entre el valor de "paso" y la cantidad de círculos

La cantidad aproximada de círculos creados es:

360 / paso

Ejemplos:

- paso = 30 → 12 círculos
- paso = 10 → 36 círculos
- paso = 5 → 72 círculos
- paso = 1 → 360 círculos

Mientras más pequeño sea el valor de paso:
- Más iteraciones realiza el ciclo
- Más posiciones se calculan
- Más círculos se generan
- La figura se vuelve más densa y compleja

Si el paso es grande, habrá pocos círculos y estarán más separados.

Si el paso es pequeño, habrá muchos círculos y la figura se verá más cerrada y detallada.

Lógica Matemática General

El programa:

1. Parte de un círculo central.
2. Recorre 360 grados.
3. Calcula posiciones usando funciones trigonométricas.
4. Genera círculos en cada posición.
5. Controla la densidad mediante el valor del paso.

Es un ejemplo claro del uso de programación estructurada, ciclos y matemáticas aplicadas a gráficos 3D.


<img width="1297" height="990" alt="image" src="https://github.com/user-attachments/assets/6845533c-74b3-4a39-9871-b4af66a7a491" />

<img width="1037" height="663" alt="image" src="https://github.com/user-attachments/assets/35aeee6b-f1f8-4376-9737-65af4431f202" />

<img width="1045" height="637" alt="image" src="https://github.com/user-attachments/assets/70596c22-8ca9-4720-984c-10b1644e2aae" />



