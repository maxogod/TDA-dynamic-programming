# Opt(i, j) = max( opt(i-1, j-1) + min(s_{j}, E[i]), opt(i-2, j-2) + min(s_1, E[i] ) )
def obtener_solucion(esfuerzos, energias):
    opt = [0] * (len(esfuerzos) + 1)
    opt[1] = min(energias[0], esfuerzos[0])
    j = 1

    for i in range(1, len(esfuerzos)):
        entreno = opt[i] + min(energias[j], esfuerzos[i])
        no_entreno = opt[i-1] + min(energias[0], esfuerzos[i])
        if entreno > no_entreno:
            opt[i+1] = entreno
        else:
            opt[i+1] = no_entreno
            j = 0

        j += 1

    return opt[-1]

esfuerzos = [36,2,78,19,59,76,65,64,33,41]
energias = [63,61,49,41,40,38,23,17,13,10]

print(obtener_solucion(esfuerzos, energias))