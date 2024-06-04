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
