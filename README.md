# Apuntes-Gafricacion-U1
## Unidad I – Introducción a la Graficación por Computadora

Este repositorio contiene la investigación documental correspondiente a la Unidad I de la materia Graficación por Computadora.

## Contenido

1. Historia y evolución de la graficación por computadora
2. Áreas de aplicación
3. Aspectos matemáticos de la graficación
4. Modelos del color: RGB, CMY, HSV y HSL
5. Representación y trazo de líneas y polígonos
6. Procesamiento de mapas de bits
7. Bibliografía en formato APA

También se incluyen prácticas realizadas:
- Animación de cámara en Blender (pasillo 3D)
- Dibujo de polígono en 2D
- Construcción geométrica de la Flor de la Vida
- Tutorial básico de iluminación en Blender

1.1 Historia y evolución de la graficación por computadora

Historia y evolución de la graficación por computadora

La graficación por computadora es el conjunto de técnicas que permiten generar imágenes digitales mediante el uso de algoritmos y hardware especializado.

Primeros desarrollos (1950–1960)

Los primeros sistemas gráficos aparecieron en laboratorios militares y universidades. Uno de los sistemas más importantes fue desarrollado en el MIT.

En 1963, Ivan Sutherland desarrolló Sketchpad, considerado el primer sistema de diseño asistido por computadora (CAD).

Durante esta etapa, las imágenes eran vectoriales y se mostraban en pantallas monocromáticas.

Década de 1980

Se popularizó el uso comercial de gráficos por computadora en:
- Videojuegos
- Cine
- Interfaces gráficas de usuario

Se desarrollaron tarjetas gráficas especializadas.

Década de 1990 – actualidad
- Renderizado 3D realista
- Animación digital avanzada
- Modelado tridimensional
- Uso de GPUs
- Realidad virtual y aumentada

Actualmente, herramientas como Blender permiten modelado, animación, iluminación y renderizado profesional.

1.2 Áreas de aplicación

Áreas de aplicación de la graficación por computadora

La graficación por computadora tiene múltiples aplicaciones:

1. Cine y animación
   
Producción de películas animadas y efectos especiales.

2. Videojuegos
   
Creación de entornos tridimensionales interactivos.

3. Arquitectura e ingeniería (CAD)
   
Diseño de planos y modelos estructurales.

4. Medicina
   
Reconstrucciones 3D de órganos y estudios tomográficos.

5. Realidad virtual y aumentada

Simulación de entornos inmersivos.

<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/adea6e99-eb69-4455-8618-f057077cb741" /> <img width="1172" height="660" alt="image" src="https://github.com/user-attachments/assets/55e4d7b1-8f84-4316-9aab-998658cc1831" /> <img width="1280" height="400" alt="image" src="https://github.com/user-attachments/assets/629c30f1-2e0a-468e-b945-8569110fdb50" />

1.3 Aspectos matemáticos de la graficación

La graficación por computadora se basa principalmente en:

Álgebra lineal
- Vectores
- Matrices
- Transformaciones lineales

Transformaciones básicas:
- Traslación
- Rotación
- Escalado

Geometría analítica

Uso del plano cartesiano para representar objetos.

Trigonometría

Cálculo de ángulos y rotaciones.

Cálculo diferencial

Modelado de curvas y superficies.

1.4 Modelos del color: RGB, CMY, HSV y HSL

Modelo RGB

<img width="1905" height="2000" alt="image" src="https://github.com/user-attachments/assets/f8814788-cd67-4651-af4b-dc65c3438d7a" />

Modelo aditivo basado en:
- Rojo
- Verde
- Azul

Se utiliza en pantallas digitales.

Modelo CMY

<img width="1000" height="1080" alt="image" src="https://github.com/user-attachments/assets/79e23469-52b5-444c-aa45-852ee99c147f" />

Modelo sustractivo:
- Cian
- Magenta
- Amarillo

Se usa en impresión.

Modelo HSV

<img width="613" height="401" alt="image" src="https://github.com/user-attachments/assets/596f8e82-57fa-45d2-82b0-b87a70e72708" />

- Hue (matiz)
- Saturación
- Valor

Modelo HSL

<img width="433" height="483" alt="image" src="https://github.com/user-attachments/assets/16fe6e62-7635-438e-91c6-1e6e6f4ca6ec" />

- Hue
- Saturación
- Luminosidad

Tutorial: Iluminación de un cubo en Blender

<img width="390" height="463" alt="image" src="https://github.com/user-attachments/assets/c9359e9c-9b2c-46a6-bc63-b996006b65c7" />

Pasos:
1. Abrir Blender.
2. Dejar el cubo por defecto.
3. Agregar una luz:
Shift + A → Light → Point.
4. Ajustar potencia en propiedades de luz.
5. Cambiar material:
   Material Properties → New.
6. Modificar:
- Base Color
- Roughness
- Metallic
7. Cambiar a modo Rendered para ver iluminación.

1.5 Representación y trazo de líneas y polígonos

La representación digital de líneas se realiza mediante algoritmos como:

- Algoritmo DDA
- Algoritmo de Bresenham

Los polígonos son figuras cerradas formadas por segmentos de línea.

1.5.1 Formatos de imagen

Principales formatos:
- PNG (sin pérdida)
- JPG (con pérdida)
- BMP
- GIF
- TIFF

Práctica: Dibujo de polígono en 2D

Descripción:

Se realizó el trazo de un polígono regular utilizando coordenadas cartesianas.

Se aplicó:

- Cálculo de vértices mediante trigonometría
- Uso de ángulos internos
- Conexión secuencial de puntos

Práctica: Flor de la Vida

<img width="474" height="817" alt="image" src="https://github.com/user-attachments/assets/02560be3-450e-4526-b347-cc260c76f76e" />

La Flor de la Vida es una figura geométrica formada por múltiples circunferencias superpuestas.

Para su construcción:

1. Se dibuja un círculo base.
2. Se coloca el centro del siguiente círculo en la circunferencia del primero.
3. Se repite el proceso formando una red hexagonal.

Conceptos aplicados:

- Geometría euclidiana
- Simetría
- Coordenadas cartesianas

1.6 Procesamiento de mapas de bits
Un mapa de bits es una imagen compuesta por píxeles organizados en una cuadrícula.

Cada píxel almacena información de color.

Conceptos importantes:

- Resolución
- Profundidad de color
- Compresión
- Filtros digitales
- Procesamiento digital de imágenes

Aplicaciones:

- Edición fotográfica
- Corrección de color
- Detección de bordes
- Reconocimiento de patrones

Bibliografía

Historia de la graficación por computadora. (n.d.). Slideshare. https://es.slideshare.net/slideshow/historia-de-la-graficacin-por-computadora/53956334

Antonio. (2016, June 19). Modelos de color (RGB, CMYK, HSV/HSL). Antonio Herrera. https://ahenav.wordpress.com/2014/04/09/modelos-de-color/

Foley, J. D., van Dam, A., Feiner, S. K., & Hughes, J. F. (1996). Computer Graphics: Principles and Practice. Addison-Wesley.

Hearn, D., & Baker, M. P. (2014). Computer Graphics with OpenGL. Pearson.

Shirley, P. (2018). Fundamentals of Computer Graphics. CRC Press.


