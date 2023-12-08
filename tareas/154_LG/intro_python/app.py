def hello_world():
    print('Hello World')
    print(f'La variable __name__ tien el valor de {__name__}')
    
    
'''
__name__ es un keyword reservado de python, que se utiliza cuando ejecutas un script
o importas una libreria/script.
1. Si ejecutas el script "python app.py" entonces __name__ toma el valor de "__main__"
2. Si importas el script "import app" entonces __name__ toma el valor de "app", de esta
manera no se ejecutra el snippet que esta abajo, pues el condicional fallaria.
'''

if __name__ == '__main__':
    hello_world()
 