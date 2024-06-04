<h1>PRUEBA PILOTO EXAMEN MODULO 2</h1>

- Instrucciones:

**Sección 1) Configuración del Entorno de Desarrollo**

- **Configuración de una instancia EC2 en AWS con Amazon Linux.**
    
    Creas un cloud9 y una EC2 Abriendo los puertos correspondientes.
    

- **Instalación y configuración de herramientas de desarrollo en la instancia EC2, incluyendo Python, Git y despliega un entorno de desarrollo integrado (IDE) como Cloud9**
    
    Para verificar si tienes instalado python3:
    
    ```jsx
    python3 --version
    Python 3.9.16
    ```
    
    Para instalar git:
    
    ```jsx
    sudo yum install git -y
    git --version
    ```
    

- **Configuración de cortafuegos y seguridad en la instancia EC2 para proteger la aplicación, abriendo solamente los puertos necesarios**
    
    En este caso abrir el puerto 5000 al ser la app Flask.
    

**Sección 2) Desarrollo de la Aplicación Web**

- **Creación de una aplicación web simple utilizando el framework web Flask en Python.**
    
    Vamos a instalar `pip3` y luego Flask. Sigue estos pasos:
    
    ```jsx
    sudo yum install python3-pip -y
    pip3 --version
    ```
    
    Instala Flask:
    
    ```jsx
    sudo pip3 install flask
    ```
    

### Crear la aplicación Flask

1. **Crea un nuevo directorio para tu aplicación:**
    - Navega a tu espacio de trabajo y crea un nuevo directorio.

```jsx
mkdir flask_app
cd flask_app
```

1. **Crea un archivo `app.py` para tu aplicación Flask:**
- En el directorio `flask_app`, crea y abre el archivo `hello.py`.

```jsx
nano hello.py
```

Añade el siguiente código a `hello.py` para crear una aplicación Flask con una ruta y un formulario.

```jsx
                                                                                                                                                                  
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form1.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'<h1>Hello, {name}!</h1>'
    return render_template('form2.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

- **Implementación de funcionalidades básicas de la aplicación:**
    - Añade al menos una ruta
    
    [http://<tu-ip-publica-de-ec2>:5000/form]
    
    - Añade al menos un formulario
        
        Crea un directorio `templates` y agrega un archivo HTML para la ruta del formulario.
        
        ```jsx
        mkdir templates
        nano templates/form1.html
        ```
        
        ```jsx
                                       
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <h1>Welcome to My Flask App!</h1>
            <form method="POST" action="/form">
                Name: <input type="text" name="name">
                <input type="submit" value="Submit">
            </form>
        </body>
        </html>
        ```
        
        nano templates/form2.html
        
        Añade el siguiente contenido a `form2.html`:
        
        ```jsx
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Form</title>
        </head>
        <body>
            <h1>Ejemplo de prueba!</h1>
            <form method="POST">
                Name: <input type="text" name="name">
                <input type="submit" value="Submit">
            </form>
        </body>
        </html>
        
        ```
        

Usar este comando en el directorio donde tienes la aplicación:

```jsx
export FLASK_APP=hello.py
flask run --host=0.0.0.0 --port=5000
```

**Sección 3) Pruebas y Depuración**

- **Desarrollo de casos de prueba para verificar el funcionamiento correcto de la aplicación.**

Creas en la ruta de la app, el archivo `sudo nano test_hello.py`:

```jsx
import unittest
from hello import app

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        # Configura la aplicación de Flask en modo de pruebas
        app.testing = True
        self.app = app.test_client()
        print("Aplicación en modo de pruebas.")

    def test_ruta(self):
        # Prueba que la ruta raíz devuelve el contenido de form1.html
        response = self.app.get('/')
        print(f"test_ruta: codigo de status: {response.status_code}")
        if response.status_code == 200:
            print("test_ruta: La ruta raíz está accesible.")
        else:
            print("test_ruta: Error al acceder a la ruta raíz.")
        self.assertIn(b'<h1>Welcome to My Flask App!</h1>', response.data)
        print("test_ruta: Contenido verificado.")

    def test_ruta_get(self):
        # Prueba que la ruta '/form' devuelve el contenido de form2.html cuando se realiza una solicitud GET
        response = self.app.get('/form')
        print(f"test_ruta_get: status code: {response.status_code}")
        if response.status_code == 200:
            print("test_ruta_get: La ruta '/form' está accesible.")
        else:
            print("test_ruta_get: Error al acceder a la ruta '/form'.")
        self.assertIn(b'<title>Form</title>', response.data)
        print("test_ruta_get: Contenido verificado.")

    def test_ruta_post(self):
        # Prueba que la ruta '/form' devuelve el mensaje "Hello, {name}!" cuando se envía un formulario POST
        response = self.app.post('/form', data={'name': 'Ejemplo'})
        print(f"test_ruta_post: status code: {response.status_code}")
        if response.status_code == 200:
            print("test_ruta_post: La solicitud POST a '/form' fue exitosa.")
        else:
            print("test_ruta_post: Error al realizar la solicitud POST a '/form'.")

if __name__ == '__main__':
    print("Empezando pruebas unitarias.")
    unittest.main()

```

Y pruebas el test con este comando:
```jsx
python3 test_hello.py
```

**python3 test_hello.py**
<h2> Incorporación a Futuro con RDS: </h2>

<h3>Crear una base de datos RDS.</h3>
Una vez creada copiar el Punto de enlace, ejemplo: "database-1.c3v2jowp10tn.us-east-1.rds.amazonaws.com".

Instalaciones en la EC2 de Mysql:

•	Instalar mysql y php-mysql en la ec2, recuerda reiniciar el servicio de apache
```jsx
sudo wget https://dev.mysql.com/get/mysql80-community-release-el9-1.noarch.rpm
sudo dnf install mysql80-community-release-el9-1.noarch.rpm -y
sudo rpm --import https://repo.mysql.com/RPM-GPG-KEY-mysql-2023
sudo dnf install mysql-community-client -y
sudo dnf install mysql-community-server -y
```

•	Conectarte a la base de datos desde las ec2
```jsx
sudo systemctl start mysqld
sudo systemctl enable mysqld
sudo systemctl status mysqld
mysql -u admin -p -h database-1.c3v2jowp10tn.us-east-1.rds.amazonaws.com

```

Usar un archivo de configuracion que funcione parecido a este:

```jsx
**from flask import Flask,render_template, request
from flaskext.mysql import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'database-1.c3v2jowp10tn.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'eduardoadmin1234'
app.config['MYSQL_DB'] = 'database-1'
 
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('form1.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'<h1>Hello, {name}!</h1>'
    return render_template('form2.html')
 
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO info_table VALUES(%s,%s)''',(name,age))
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"
 
app.run(host='localhost', port=5000)**
```
Habria que modificar uno de los form1.html o form2.html para que relacione el formulario con la base de datos (CREATE DATABASE , CREATE TABLE , your_table_name (
     id INT AUTO_INCREMENT PRIMARY KEY,
     name VARCHAR(255),
     email VARCHAR(255),
     message TEXT
 );
 
Y tambien relacionar la conexión con el archivo de configuración anterior.

Y finalmente a traves de estos comandos:
```jsx
mysql> USE database-1
mysql> SELECT * FROM Tablaejemplo;
```

Comprobariamos en la EC2 si las tablas se han creado con los datos que hemos ingresado en los formularios.
