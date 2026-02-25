# proyectoIntegrador
Generación de Carretera Curva con Animación en Blender


Este proyecto consiste en la generación procedural de una carretera curva utilizando Python dentro de Blender. El script crea automáticamente un escenario compuesto por paredes laterales, suelo segmentado y una cámara animada que recorre la trayectoria generada. El objetivo principal es aplicar conceptos matemáticos y de graficación por computadora para automatizar la construcción de un entorno tridimensional y su animación.

El desarrollo del escenario inicia con la limpieza completa de la escena, eliminando todos los objetos existentes para trabajar desde un entorno vacío. Posteriormente se crean materiales básicos para las paredes y el suelo, utilizando colores definidos en formato RGB. Estos materiales permiten diferenciar visualmente los elementos del escenario y mejorar la percepción de profundidad durante la animación.

La carretera se genera mediante un ciclo for que construye cada segmento de manera secuencial. En cada iteración se crean dos paredes (izquierda y derecha) y un plano que funciona como suelo. La posición de cada elemento se calcula utilizando una función seno, lo que permite generar una curvatura suave en el eje X mientras el escenario avanza en el eje Y. Esta técnica demuestra la aplicación directa de funciones trigonométricas dentro de la graficación por computadora para producir trayectorias dinámicas y naturales.

Matemáticamente, la curvatura se define mediante la expresión sin(i * 0.3) * 4, lo que produce un desplazamiento oscilatorio controlado. Gracias a esta fórmula, cada segmento se posiciona ligeramente desplazado respecto al anterior, generando la apariencia de una carretera ondulada. Este procedimiento es un ejemplo claro del uso de modelos matemáticos para controlar la geometría en entornos 3D.

Posteriormente, el script agrega una cámara y configura una animación de 150 cuadros (frames). En cada cuadro, la posición de la cámara se actualiza para avanzar sobre el eje Y mientras sigue la misma función seno utilizada para construir la carretera. De esta manera, la cámara recorre exactamente la trayectoria generada, creando un efecto de desplazamiento continuo. En cada frame se insertan keyframes de ubicación y rotación, lo que permite que Blender interpole automáticamente el movimiento.

El resultado final es una animación fluida donde la cámara avanza a lo largo de una carretera curva generada completamente por código. Este ejercicio integra conceptos fundamentales de graficación por computadora como transformaciones geométricas, modelado procedural, uso de materiales, animación por keyframes y aplicación de funciones matemáticas para la creación de formas dinámicas.
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/820ab3de-e6e8-4a2c-91dd-d482a579f0bd" />


Para ejecutar el script, es necesario abrir Blender (versión 3.x o superior), dirigirse a la pestaña de Scripting, crear un nuevo archivo, pegar el código y presionar “Run Script”. Posteriormente, al reproducir la línea de tiempo, se podrá observar la animación generada automáticamente.

Este proyecto demuestra cómo la programación puede utilizarse como herramienta poderosa dentro del modelado y la animación 3D, permitiendo automatizar procesos y aplicar fundamentos matemáticos en la construcción de entornos virtuales.

Cómo ejecutar

Abrir Blender 3.x o superior

Ir a la pestaña Scripting

Crear nuevo archivo

Pegar el código

Ejecutar con Run Script

Reproducir la animación con barra espaciadora

🛠️ Tecnologías utilizadas

Blender

Python

API bpy

Funciones matemáticas (math.sin, math.radians)
