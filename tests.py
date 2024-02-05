#!/usr/bin/env python3

import unittest
from algoritmo import obtener_ganancia_maxima

def obtener_plan_entrenamiento(archivo):
    with open(archivo, 'r') as file:
        contenido = file.readlines()
    planes_por_cantidad_dias = {}
    for i in range(0, len(contenido), 4):
        nombre = contenido[i].strip()  
        plan_entrenamiento = contenido[i+2].split(": ")[1].strip().split(", ")
        planes_por_cantidad_dias[nombre] = list(plan_entrenamiento)

    return planes_por_cantidad_dias

archivo = './archivos_prueba/Resultados Esperados.txt'
planes_por_archivo = obtener_plan_entrenamiento(archivo)

def obtener_esfuerzo_y_energia(filename):
    esfuerzo = []
    energia = []

    with open(f'archivos_prueba/{filename}', 'r') as file:
        length = int(file.readline())
        for _ in range(length):
            line = file.readline()
            esfuerzo.append(int(line))
        for _ in range(length):
            line = file.readline()
            energia.append(int(line))
    return esfuerzo, energia


class UnitTests(unittest.TestCase):
    def test_3_elem(self):
        file = '3.txt'
        res = 7

        esfuerzos, energias = obtener_esfuerzo_y_energia(file)
        ejecucion = obtener_ganancia_maxima(esfuerzos, energias)

        self.assertEqual(res, ejecucion[0])
        self.assertEqual(planes_por_archivo[file], ejecucion[1])


    def test_10_elem(self):
        file = '10.txt'
        res = 380

        esfuerzos, energias = obtener_esfuerzo_y_energia(file)
        ejecucion = obtener_ganancia_maxima(esfuerzos, energias)

        self.assertEqual(res, ejecucion[0])
        self.assertEqual(planes_por_archivo[file], ejecucion[1])

    def test_10_elem_bis(self):
        file = '10_bis.txt'
        res = 523

        esfuerzos, energias = obtener_esfuerzo_y_energia(file)
        ejecucion = obtener_ganancia_maxima(esfuerzos, energias)

        self.assertEqual(res, ejecucion[0])
        self.assertEqual(planes_por_archivo[file], ejecucion[1])

    def test_10_elem_todo_entreno(self):
        file = '10_todo_entreno.txt'
        res = 860

        esfuerzos, energias = obtener_esfuerzo_y_energia(file)
        ejecucion = obtener_ganancia_maxima(esfuerzos, energias)

        self.assertEqual(res, ejecucion[0])
        self.assertEqual(planes_por_archivo[file], ejecucion[1])
    def test_50_elem(self):
        file = '50.txt'
        res = 1870

        esfuerzos, energias = obtener_esfuerzo_y_energia(file)
        ejecucion = obtener_ganancia_maxima(esfuerzos, energias)

        self.assertEqual(res, ejecucion[0])
        self.assertEqual(planes_por_archivo[file], ejecucion[1])

    def test_50_elem_bis(self):
        file = '50_bis.txt'
        res = 2136

        esfuerzos, energias = obtener_esfuerzo_y_energia(file)
        ejecucion = obtener_ganancia_maxima(esfuerzos, energias)

        self.assertEqual(res, ejecucion[0])
        self.assertEqual(planes_por_archivo[file], ejecucion[1])

    def test_100_elem(self):
        file = '100.txt'
        res = 5325

        esfuerzos, energias = obtener_esfuerzo_y_energia(file)
        ejecucion = obtener_ganancia_maxima(esfuerzos, energias)

        self.assertEqual(res, ejecucion[0])
        self.assertEqual(planes_por_archivo[file], ejecucion[1])


    def test_500_elem(self):
        file = '500.txt'
        res = 27158

        esfuerzos, energias = obtener_esfuerzo_y_energia(file)
        ejecucion = obtener_ganancia_maxima(esfuerzos, energias)

        self.assertEqual(planes_por_archivo[file], ejecucion[1])
        self.assertEqual(res, ejecucion[0])

    def test_1000_elem(self):
        file = '1000.txt'
        res = 54021

        esfuerzos, energias = obtener_esfuerzo_y_energia(file)
        ejecucion = obtener_ganancia_maxima(esfuerzos, energias)

        self.assertEqual(planes_por_archivo[file], ejecucion[1])
        self.assertEqual(res, ejecucion[0])

    def test_5000_elem(self):
        file = '5000.txt'
        res = 279175

        esfuerzos, energias = obtener_esfuerzo_y_energia(file)
        ejecucion = obtener_ganancia_maxima(esfuerzos, energias)
        
        self.assertEqual(res, ejecucion[0])
        self.assertEqual(planes_por_archivo[file], ejecucion[1])



if __name__ == '__main__':

    unittest.main()



