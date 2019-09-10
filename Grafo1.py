# -*- coding: utf-8 -*- 
"""
    Partes de un grafo: 
    a) Nodos: Vértices, vertex 
    b) Arcos (flechas): Aristas, edge

    La correspondencia es por orden alfabético (ascendente)

    El vértice A, tiene aristas: B, C
    El vértice B, tiene aristas: C, D
    El vértice C, no tiene aristas 
    El vértice D, no tiene aristas 
    *   Para representarlo en JSON, cada vértice será un índice y cada arista será un elemento de vértices de dicho índice dentro de un arreglo 

    *   Una de las caracteristicas de un grafo dirigido, es que es posible producir ciclos(loops) pero también salidas naturales al grafo 

    *    Una de las caracteristicas de los grafos no dirigidos es que se debe establecer un vértice inicial y final 
    *    El objetivo es buscar conexiones(rutas) entre vértices 
    *    El propósito de esas conexiones es conocer la ruta más corta. 

    Las aristas que  conectan vértices pueden tener un "Peso". El pesi es una ponderación entre múltiples caracteristicas (definidas por el escenario del grafo: carreteras, routers, satélites) de la arista. 

    El propósito del tema es producir tablas de peso para elegir la mejor ruta ej: la ruta más corta, la ruta de mayor peso, la ruta cuyo peso es igual a 1, etc... 

    Temas de Tercer Parcial: 
        - Grafos 
        -Rendimiento --> Ordenamiento 
        -Cifrado 
"""
#GRAFO DIRIGIDO 
graph1 = {
     "A": ["B", "C"], 
     "B": ["C", "D"], 
     "C": ["E"], 
     "D": [], 
     "E": ["A"]
}

#GRAFO NO DIRIGIDO, TIENE PESO POR SALTOS
graph2 = {
    "A": ["B", "C", "E"],
    "B": ["A", "C", "D"], 
    "C": ["A", "B", "E"], 
    "D": ["B"], 
    "E": ["A", "C"]
}
