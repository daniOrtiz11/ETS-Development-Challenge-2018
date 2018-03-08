# ETS-Development-Challenge-2018

## 1er Reto
### Lenguaje elegido: 
Python 3

### Comentario:
Al ser un archivo .py para ejecutarlo bastaría con hacerlo desde la linea de comandos teniendo instalado python 3.
En este caso se ha usado Spyder (incluido en el entorno Anaconda) para poder editar y probar el resultado lo más rápido posible.
La lectura de los datos se ha hecho de forma manual, directamente desde el código.
Idealmente se debería cargar desde fuera, introduciéndolos como entrada o con un archivo externo, pero al ser requerido sólo un único archivo me ha parecido la forma más coherente de hacerlo. 
No se han incluido comentarios en el código 

### Preguntas:
#### 1. ¿Qué algortimo se debe emplear para resolver este problema?
Vuelta atrás (Backtracking).
Más concretamente es una variación del famoso "Problema del viajante".

#### 3. ¿Cuál es el mejor camino para Frodo?
Orodruin
Minas Morgul
Minas Tirith
Edoras
Isengard
Nin-In-Eilf
Sarn Ford
Tuckburow
Hobbiton

## 2º Reto
### Lenguajes elegidos: 
Frontend: javascript + html
Backend: nodejs + express

Importante: la aplicación está incompleta, por falta de tiempo personal no ha sido posible llevar a cabo la idea total de lo pretendido.
Comentario:
Se decidió usar Express como infraestructura para montar la aplicación web con node.js
Todas las librerias instaladas están incluidas en el zip, a destacar "ejs" para permitir usar html en vez de jade.
Para arrancar la aplicación basta con tener instalado node y desde de la consola con ir a la carpeta de la aplicación "datademo" y ejecutar:
npm start
Se quedará en la consola, no cerrar, y se podrá ver corriendo la aplicación en el puerto 3000:
localhost:3000
En la parte front unicamente está desarrollado como extraer los datos del csv y formatearlos en json para poder usarlos.
La idea era usar Chart.js para mostrar esos datos. Hay que tener en cuenta el tamaño y las dificultades en la renderización de la pantalla.
Por tanto la idea era ir accediento a los datos a través de gráficos en forma de puntos (scatter) acotados hasta poder llegar al dato concreto requerido.
Pasos:
1º seleccionar el atributo (un punto por cada uno de diferente color) por el que se quiere buscar.
2º Se mostrarán varios puntos con distintos rangos de valores.
3º Ir bajando de niveles de puntos hasta llegar a un nivel en que los puntos representen tuplas concretas y ya mostrar toda la información.

