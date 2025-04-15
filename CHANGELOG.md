# Prueba de entrada Desarrollo de Software
Autor : Andres La Torre Vasquez

Usuario de github: Jun1el

link : https://github.com/Jun1el/Prueba_entrada_CC3S2
## Dia 1 
- Creamos la estructura del proyecto
- Crear archivos Dockerfile y docker-compose.yml con el contenido indicado.

**Nota:** Antes de crear branch develop hacer un commit en la rama main. 
- Inicializamos git y creamos una rama develop a partir de main y una rama feature/dia1 a partir de develop donde haremos los cambios del dia 1.
- Adicionalmente agregare un **README.md** para tener una mejor comprension del proyecto.
- Haremos un registro diario usando git diff y git blame para registrar el historial 
- Corregimos errores en la subida a Github agregando .gitignore asi como mejoramos la estructura del proyecto.
- Para la estructura agregamos 3 directorios (app,db y test) para un trabajo mas ordenado.

## Dia 2 

- Agregamos requirements.txt para mejorar la estructura y modificamos el dockerfile; asi como corregimos errores ede venv
- Agregamos la clase Questions y test bases de muestra 
- Comprobamos exitosamente los test 
- Agregamos caracteristicas propias a nuestra clase Questions y test 
- Comprobamos exitosamente los test.
- Modificamos el Readme.md por Changelog.md

## Dia 3

- Primero hicimos pruebas de conexion del docker compose exitosamente para lo cual agregamos un print a main para mostrar un mensaje sencillo
- Agregamos la clase Quiz y run_quiz adaptados a nuestro codigo exitosamente 
- Modificamos el CHANGELOG.md para declaras los avanzes del dia de hoy 

## Dia 4
- Primeramente definimos nuestro init.sql para crear la bd que aun no habiamos creado y logramos que exitosamente corriera en Docker.
- Asimismo modificamos run_quiz para que obtuviera los datos desde la bd 
- Hicimos correcciones de ligeros erroes en db.py y compose para un mejor funcionamiento ya que modularizamos el proyecto para tenerlo mas organizado y adaptable a cambios 
- Al mismo tiempo agregamos para que al final muestre las respuesta correctas e incorrectas al acabar el juego.
- Finalmente creamos pruebas unitarias sencillas para nuestra clase quiz 
- Modificamos el CHANGELOG para declarar los cambios del dia de hoy.

## Dia 5

- Agregamos el score del participante y puntaje de acuerdo a la dificultad de la pregunta
- Mejoramos la interfaz del juego mostrando el score final, y los puntos por pregunta obtenidos y agregamos test para Quiz.py
- Eliminamos __pycache__ del repositorio y actualizamos el .gitignore para no subir archivos innecesarios
- Mejoramos la documentacion del proyecto 

## Dia 6

- Se movio la carpeta de test a la carpeta de app para una mejor integracion de los test en docker y su funcionamiento correcto
- Creamos nuestro repositorio secreto SONAR_TOKEN para usar el scaneo de SONARCLOUD 
- Creamos nuestro ci.yml para el funcionamiento de github actions 
- Corregimos ciertos problemas de sonarqube en github actions desde la ramam de develop para no hacer merges innecesarios ya que hicimos muchos commits que al final usamos git reset para simplificar el historial y llegamos a arreglar todos los problemas de sonarqube
- Finalmente implementamos las pruebas de integracion de la bd con el programa