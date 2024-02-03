
#!/usr/bin/env python3

# OPT(i) = max(  OPT(i-2) + min(s1, ei), M[i-1][j-1] + min(sj, ei) for j in range(1, i)  )
def obtener_ganancia_maxima(esfuerzos, energias) -> int:
    memo = [[0] * len(esfuerzos) for _ in range(len(esfuerzos))]  # matriz nxn

    memo[0][0] = min(esfuerzos[0], energias[0])  # caso base
    memo[1][0] = min(esfuerzos[1], energias[0])

    for i in range(1, len(esfuerzos)):

        if i != 1:
            memo[i][0] = max(memo[i-2]) + min(esfuerzos[i], energias[0])

        for j in range(1, i+1):
            memo[i][j] = memo[i-1][j-1] + min(esfuerzos[i], energias[j])

    return max(memo[-1])


def recontruir_camino(memo, esfuerzos, energias) -> list[str]:
    return []
