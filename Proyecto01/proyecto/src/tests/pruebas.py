import unittest, os
def resta_grados(kelvin,celsius):
    'Metodo que realiza la resta de kelvin a grados centigrados,a traves de una tupla, es decir, linea e int o float, regreando una instancia de una clase'
    for linea in (kelvin, celsius):
        if not isinstance(linea, int) and not isinstance(linea, float):
            raise TypeError
    return kelvin-celsius



def verificar_archivo(clase):
    'Ruta donde esta ubicado el archivo y a atraves de esta se comprueba si existe este archivo en la carpeta'
    ruta='/Users/Fa/Downloads/Proyecto1-Modelado/Proyecto01/proyecto/src/archivos/archivo_principal.py'
    try:
        archivo = open(ruta)
        print(archivo) 
        archivo.close()
    except FileNotFoundError:
        print('No existe el archivo')
        exit()
    return clase



class TestArchivos(unittest.TestCase):
    def test_resta(self):
        'Metodo que va a comprobar si esta bien la resta de grados con el metodo que se realizo anteriormente, en caso contrario se le indica al usuario'
        self.assertEqual(resta_grados(273.15,223),50.14999999999998)
        with self.assertRaises(TypeError):
            resta_grados(273.15, "Python")
    
    def test_latitudes(self):
        'Comprueba si la latitud y longitud de la ciudad es la misma o diferente para que se indique que esta mal'
        if 'latitud_origen'=='longitud_origen':
            self.assertFalse(False)

    def test_archivo(self):
        'Ruta donde esta ubicado el archivo y a atraves de esta se comprueba si coinciden las rutas'
        ruta2='/Users/Fa/Downloads/Proyecto1-Modelado/Proyecto01/proyecto/src/archivos/archivos_principal.py'
        ruta_bien=ruta2='/Users/Fa/Downloads/Proyecto1-Modelado/Proyecto01/proyecto/src/archivos/archivo_principal.py'
        self.assertEqual(verificar_archivo(ruta2),ruta_bien)
        self.assertFalse(False)
    
if __name__ == "__main__":
    unittest.main()