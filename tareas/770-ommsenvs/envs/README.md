# Pyenv

## Instrucciones para utilizar requirements.txt con .venv
1. Creación del ambiente virtual 
Para crear un ambiente virtual llamado .venv en el directorio actual:  
`python -m venv .venv`

2. Activar el ambiente virtual  
Dependiendo de tu sistema operativo, usa uno de los siguientes comandos:  
Linux/Mac  
`source .venv/bin/activate`  
Windows (cmd.exe):    
`.venv\Scripts\activate.bat`  

3. Instalar paquetes desde `requirements.txt`  
Si tienes un archivo requirements.txt en tu directorio actual (o un archivo equivalente), puedes instalar todas las dependencias especificadas en ese archivo con:  
`pip install -r requirements.txt`  

4. Guardar paquetes en requirements.txt
Si instalaste paquetes adicionales y quieres guardar esos paquetes y sus versiones en requirements.txt, puedes hacerlo con:  
`pip freeze > requirements.txt`  

5. Desactivar el ambiente virtual:  
Cuando hayas terminado de trabajar en tu ambiente virtual, puedes desactivarlo con:  
`deactivate`

# Conda
Estas instrucciones guiarán a los estudiantes en la creación y activación de un ambiente Conda utilizando un archivo `environment.yml.`

1. Creacion de ambiente de Conda
Para crear un ambiente con Conda basado en un archivo `environment.yml` presente en tu directorio actual:  
`conda env create -f environment.yml`  
El nombre del ambiente será el que se definió dentro del archivo environment.yml bajo la clave name. Nota que nuestro archivo no tiene este elemento, puedes agregarlo o buscar como pasarlo como comando de terminal.  

2. Activar el ambiente Conda:  
Para activar el ambiente que acabas de crear:  
`conda activate nombre_del_ambiente`  
Reemplaza nombre_del_ambiente con el nombre que definiste en el archivo environment.yml.   
Una vez activado, el nombre del ambiente aparecerá al inicio de la línea de comando.  

3. Desactivar el ambiente Conda:  
Cuando hayas terminado de trabajar en tu ambiente Conda, puedes desactivarlo con:  
`conda deactivate`  

4. Exportar el ambiente a un archivo environment.yml:  
Si realizaste cambios en el ambiente, como instalar paquetes adicionales, y quieres reflejar esos cambios en el archivo environment.yml, puedes hacerlo con:  
`conda env export > environment.yml`