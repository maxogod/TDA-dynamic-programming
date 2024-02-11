#!/usr/bin/env python3

def obtener_esfuerzo_y_energia(filename):
    esfuerzo = []
    energia = []

    with open(filename, 'r') as file:
        length = int(file.readline())
        for _ in range(length):
            line = file.readline()
            esfuerzo.append(int(line))
        for _ in range(length):
            line = file.readline()
            energia.append(int(line))
    return esfuerzo, energia


def obtener_plan_entrenamiento(archivo):
    with open(archivo, 'r') as file:
        contenido = file.readlines()
    planes_por_cantidad_dias = {}
    for i in range(0, len(contenido), 4):
        nombre = contenido[i].strip()
        plan_entrenamiento = contenido[i+2].split(": ")[1].strip().split(", ")
        planes_por_cantidad_dias[nombre] = list(plan_entrenamiento)

    return planes_por_cantidad_dias
