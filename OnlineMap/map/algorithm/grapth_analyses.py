from heapq import heapify, heappop, heappush


class Graph:
    #Формат создания графа смежности:
    #{source_location : {target_location : Edge(vertice_1, vertice_2, weigth)}} - 
    #сопоставляем двум связным вершинам вес

    def __init__(self, grapth : dict = {}):
        self.grapth = grapth

    def shortest_distance(self, begin): #Поиск кротчайшего пути между вершинами begin и end с помощью алгоритма Дейксрты
        # Инициализация всех значений всех вершин как бесконечность
        distances = {node : float("inf") for node in self.grapth}
        distances[begin] = 0
        paths = {node : [] for node in self.grapth}
        paths[begin].append(begin)

        # Инициализация приоритетной очереди
        pq = [(0, begin)]
        heapify(pq)

        # Создаём список для хранения посещённых вершин
        visited = set()

        while pq: # До тех пор пока приоритетная очередь не пуста
            current_distance, current_node = heappop(pq) # Берём вершину с минимальной дистанцией

            if current_node in visited:
                continue #Пропускаем уже посещённые вершины
            visited.add(current_node)

            for neighbour, weight in self.grapth[current_node].items():
                #Расчитываем растояние между текущей и соседней вершиной
                tentative_distance = current_distance + weight
                if tentative_distance < distances[neighbour]:
                    distances[neighbour] = tentative_distance
                    heappush(pq, (tentative_distance, neighbour))

        predecessors = {node: None for node in self.grapth}

        for node, distance in distances.items():
            for neighbor, weight in self.grapth[node].items():
                if distances[neighbor] == distance + weight:
                    predecessors[neighbor] = node
        
        return distances, predecessors
    
    def shortest_path(self, source, target):
        # Создание словаря предшествеников
        _, predecessors = self.shortest_distance(source)

        path = []
        current_node = target

        # Обратный путь от целевого узла с использованием предшественников
        while current_node:
            path.append(current_node)
            current_node = predecessors[current_node]

        # Изменяем путь
        path.reverse()

        return path