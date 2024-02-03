#!/usr/bin/env python3

import unittest
from algoritmo import obtener_ganancia_maxima


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

        self.assertEqual(res, ejecucion)

    def test_10_elem(self):
        file = '10.txt'
        res = 380

        esfuerzos, energias = obtener_esfuerzo_y_energia(file)
        ejecucion = obtener_ganancia_maxima(esfuerzos, energias)

        self.assertEqual(res, ejecucion)

    def test_10_elem_bis(self):
        file = '10_bis.txt'
        res = 523

        esfuerzos, energias = obtener_esfuerzo_y_energia(file)
        ejecucion = obtener_ganancia_maxima(esfuerzos, energias)

        self.assertEqual(res, ejecucion)

    def test_10_elem_todo_entreno(self):
        file = '10_todo_entreno.txt'
        res = 860

        esfuerzos, energias = obtener_esfuerzo_y_energia(file)
        ejecucion = obtener_ganancia_maxima(esfuerzos, energias)

        self.assertEqual(res, ejecucion)

    def test_50_elem(self):
        file = '50.txt'
        res = 1870

        esfuerzos, energias = obtener_esfuerzo_y_energia(file)
        ejecucion = obtener_ganancia_maxima(esfuerzos, energias)

        self.assertEqual(res, ejecucion)

    def test_50_elem_bis(self):
        file = '50_bis.txt'
        res = 2136

        esfuerzos, energias = obtener_esfuerzo_y_energia(file)
        ejecucion = obtener_ganancia_maxima(esfuerzos, energias)

        self.assertEqual(res, ejecucion)

    def test_100_elem(self):
        file = '100.txt'
        res = 5325

        esfuerzos, energias = obtener_esfuerzo_y_energia(file)
        ejecucion = obtener_ganancia_maxima(esfuerzos, energias)

        self.assertEqual(res, ejecucion)

    def test_500_elem(self):
        file = '500.txt'
        res = 27158

        esfuerzos, energias = obtener_esfuerzo_y_energia(file)
        ejecucion = obtener_ganancia_maxima(esfuerzos, energias)

        self.assertEqual(res, ejecucion)

    def test_1000_elem(self):
        file = '1000.txt'
        res = 54021

        esfuerzos, energias = obtener_esfuerzo_y_energia(file)
        ejecucion = obtener_ganancia_maxima(esfuerzos, energias)

        self.assertEqual(res, ejecucion)

    def test_5000_elem(self):
        file = '5000.txt'
        res = 279175

        esfuerzos, energias = obtener_esfuerzo_y_energia(file)
        ejecucion = obtener_ganancia_maxima(esfuerzos, energias)

        self.assertEqual(res, ejecucion)


if __name__ == '__main__':
    unittest.main()
