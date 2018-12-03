class Search():
    def __init__(self):
        self.methods = ['dfs']

    def search(self, G, v, method='dfs'):
        assert method in self.methods, 'unknown method'
        assert v in G.nodes, 'vertex {} is not in graph'.format(v)

        self.marked = []
        self.count = 0

        if method == 'dfs':
            self.__dfs(G, v)

    def __dfs(self, G, v):
        adj = G.adjacency(v)
        if not adj:
            return
        for node in adj:
            if node not in self.marked:
                self.marked.append(node)
                self.count += 1
                self.__dfs(G, node)

class Partition():
    def __init__(self, G):
        self.G = G

    def connected_components(self):
        unmarked = self.G.nodes.copy()
        searcher = Search()
        components = []

        while unmarked:
            node = unmarked.pop()
            searcher.search(self.G, node)
            component = searcher.marked
            components.append(component)
            unmarked = unmarked - set(component)
        return components

