
#!/usr/bin/env python3
# OPT(i) = max(  OPT(i-2) + min(s1, ei), M[i-1][j-1] + min(sj, ei) for j in range(1, i)  )

def obtener_ganancia_maxima(esfuerzos, energias) -> int:
    memo = [[0] * len(esfuerzos) for _ in range(len(esfuerzos))]  # matriz nxn
    # memo = np.zeros((len(esfuerzos), len(esfuerzos)), dtype=int)  # matriz nxn

    memo[0][0] = min(esfuerzos[0], energias[0])  # caso base
    memo[1][0] = min(esfuerzos[1], energias[0])

    for i in range(1, len(esfuerzos)):

        if i != 1:
            memo[i][0] = max(memo[i-2]) + min(esfuerzos[i], energias[0])

        for j in range(1, i+1):
            memo[i][j] = memo[i-1][j-1] + min(esfuerzos[i], energias[j])

    max_memo = max(memo[-1])
    return max_memo, reconstruir_camino(max_memo, memo)

def reconstruir_camino(max_memo, memo) -> list[str]:
    # Utiliza la escalera producida en la busqueda del maximo, la cual al llegar a la "base": idx = 0,
    # Se añade un dia de descanso en caso de que corresponda, y sino uno de entrenamiento 
    # (caso en el que primer elemento es el que falta por considerar). 

    camino = []
    idx = memo[-1].index(max_memo)
    i = len(memo)-1
    while i >= 0: 
        while idx >= 0:
            camino.insert(0, 'Entreno')
            idx -= 1
            i-=1
            if i < 0:
                return camino
        camino.insert(0, 'Descanso')
        i -= 1
        idx = memo[i].index(max(memo[i]))
    return camino