<img width="200" alt="Logo friki de Ceros y Unos" src="https://guiferviz.com/cerosyunos/assets/logo.png">

# Ceros y Unos

Aquí podrás encontrar el código que aparece en los vídeos del canal de YouTube
**Ceros y Unos**.

Acompañando a cada algoritmo/problema hay una batería de *tests* para que puedas
comprobar que tus implementaciones son correctas.
Para no limitar a nadie ni discriminar a ningún lenguaje de programación,
todos los datos de entrada/salida del programa deberán de pasarse a través de
la entrada/salida estándar del sistema (a.k.a. `read`/`print`, `cin`/`cout`...).
La programación no se trata de andar discutiendo sobre cuál es el mejor
lenguaje de programación se trata de encontrar soluciones lógicas y sistemáticas
a los problemas que se nos presentan.
Así que sin más dilación, elige el lenguaje que más te guste y...
*¡feliz programación!*


## ¿Cómo empiezo?

### Clonar repositorio

El primer paso es clonar el repositorio de git que estás leyendo.
Si estás usando una línea de comandos con git instalado ejecuta:

```sh
git clone https://github.com/guiferviz/cerosyunos-code.git
```

También puedes descargarte un zip con todo el código desde la página de GitHub.
Debe haber algún botón llamado *Descargar ZIP* por algún sitio :)
De todas formas las instrucciones de este README están escritas pensando que
tienes acceso a una terminal que corre un sistema operativo de kernel Linux.
Si deseas instalar todas estas herramientas en Windows y sin usar la terminal
deberás de buscar alternativas a alguno de estos comandos.


### Instalar Python 3 y Pip

Tu misión será implementar el algoritmo pero, ¿quién se va a encargar de probar
que tu implementación es correcta?
Ahí es donde entra en juego el
[**Online Judge**](https://github.com/online-judge-tools/oj).
Esta herramienta ejecutará tu programa una vez por cada caso de prueba y
comprobará que la salida devuelta sea correcta.

Esta herramienta está creada en Python, por lo que hay que instalarlo.
Si usas alguna de las principales distribuciones de GNU Linux es bastante
probable que ya lo tengas instalado.
Estando en 2021, recomiendo instalar Python >= 3.7.

NOTA: Aunque el Online Judge requiera de Python para poder instalarse eso no
quiere decir que tengas que usar Python para implementar tus algoritmos.
Puedes usar **cualquier lenguaje**.

También es necesario contar con pip, el gestor de paquetes de Python.
En cualquier distribución basa en Ubuntu se puede instalar con:

```
sudo apt-get update
sudo apt-get install python3-pip
```


### Instalar dependencias de Python

Desde tu terminal navega al directorio en el que has clonado el código y
ejecuta lo siguiente:

```
pip install -r requirements.txt
```

Con esto se instalará el Online Judge y otras dependencias necesarias para
generar los tests.

Para comprobar que la instalación ha sido correcta puedes probar a ejecutar
`oj` y deberías obtener una salida que empieza como la siguiente:

```
$ oj
[INFO] online-judge-tools 11.2.0 (+ online-judge-api-client 10.8.0)
usage: oj [-h] [-v] [-c COOKIE] [--version] {download,d,dl,login,l,submit,s,test,t,generate-output,g/o,generate-input,g/i,test-reactive,t/r} ...

Tools for online judge services

.
.
.
```


### Instalar make

Para facilitar la generación y ejecución de tests se proporciona un `Makefile`
por cada ejercicio.
Es conveniente que tengas `make` instalado.
De nuevo, para instalarlo en una distribución GNU Linux basada en Ubuntu puedes
utilizar el siguiente comando:

```
sudo apt-get install make
```


### Ejecutar tests

Mueve tu terminal al directorio del primer ejemplo y lista los ficheros que hay
en él.

```
$ cd algoritmos/a000_max/
$ ls
generate.sh  generator.py  main.cpp  main.py  README.adoc  run.sh  solver.cpp  solver.py  tests
```

Aunque no todos los algoritmos/problemas tendrán exactamente la misma
estructura, si que serán bastante similares a este.

* En primer lugar tenemos un `README.md` que contiene el enunciado del problema.
Este fichero puede contener fórmulas LaTeX que no se renderizan en un README en
GitHub.
Si tienes algún visualizador de Markdown quizás te proporcione una mejor
experiencia de lectura.
* La carpeta `tests/` contiene los ficheros de entrada y salida de los tests.
* Los ficheros `solver.*` contienen la solución vista en el vídeo.
La extensión depende del lenguaje de programación.
En general cada problema está resuelto en un par de lenguajes.
* Los ficheros `main.*` son los que debes editar tú.
De nuevo, la extensión indica el lenguaje en cuestión.
La lectura de los datos de entrada está ya hecha, un comentario en el código
señala la función que debes completar.
* Un fichero `Makefile` con los siguientes targets:
  * `make tests`.
Algunos test están escritos a mano y otros son aleatorios.
El target `tests` utiliza `oj` y `generator.py` para crear ficheros de tests.
Editando este target puedes cambiar el número de test generados y la complejidad
de cada uno de ellos (el número de elementos de entrada, por ejemplo).
  * `make <extension>`.
Si quieres probar un fichero de Python debes ejecutar `make py`.
Este comando utiliza `oj` para ejecutar todos los tests.
Cuando uses otro lenguaje de programación que no esté ya definido en el
`Makefile` deberás crear tu propio target basándote en los existentes.
  * `make clean`.
Si lo necesitas, este comando borrará los tests generados automáticamente y
dejará solo aquellos creados manualmente.
También puedes usar este target para borrar los ficheros resultantes de una
compilación (si el lenguaje que estás usando es compilado :).

Ese es el funcionamiento básico, ¡con esto tienes diversión para rato!
Siéntete libre de jugar con los comandos y probar nuevas cosas.
Si encuentras algún error o quieres aportar una mejora no dudes en crear un
issue en este repositorio.
Una buena forma de aportar mejoras es incluir implementaciones en otros
lenguajes :)
