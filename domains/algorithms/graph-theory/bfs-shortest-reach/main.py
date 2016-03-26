import collections


WEIGHT = 6


class UndirectedGraph(object):
    def __init__(self):
        self.edges = collections.defaultdict(set)

    def connect(self, n1, n2):
        self.edges[n1].add(n2)
        self.edges[n2].add(n1)

    def dijsktra(self, initial):
        """
        Adapted from https://gist.github.com/econchick/4666413
        """
        visited = {initial: 0}
        path = {}
        nodes = set(self.edges.keys())
        while nodes: 
            min_node = None
            for node in nodes:
                if node in visited:
                    if min_node is None:
                        min_node = node
                    elif visited[node] < visited[min_node]:
                        min_node = node
            if min_node is None:
                break
            nodes.remove(min_node)
            current_weight = visited[min_node]
            for edge in self.edges[min_node]:
                weight = current_weight + WEIGHT
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    path[edge] = min_node
        return visited, path


if __name__ == '__main__':
    t = int(input())
    for t in range(t):
        n, m = [int(i) for i in input().strip().split(' ')]
        ug = UndirectedGraph()
        for i in range(m):
            n1, n2 = [int(j)-1 for j in input().strip().split(' ')]
            ug.connect(n1, n2)
        s = int(input())-1
        visited, _ = ug.dijsktra(s)
        result = []
        for i in range(n):
            if i == s:
                continue
            if i in visited:
                result.append(visited[i])
            else:
                result.append(-1)
        print(' '.join([str(r) for r in result]))
