import xml.etree.ElementTree as et


class Reader():
    def __init__(self,path):
        print('this path '+path)
        self.path = path

    def Xml(self):
        doc = et.parse(self.path)
        configuracion = doc.getroot()
        listaCiudades = configuracion.find('listaCiudades')
        for ciudades in listaCiudades.findall('ciudad'):
            ciudad = ciudades.find('nombre')
            print(ciudad.text)
            print(ciudad.attrib.get('filas'))
            print(ciudad.attrib.get('columnas'))
            for fila in ciudades.findall('fila'):
                print(fila.text)

path = str(input('ingrese el archivo'))
lectura = Reader('../ArchivoPrueba.xml')
lectura.Xml()