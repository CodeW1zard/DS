class Graph():
    '''
    Undirected Graph
    '''
    def __init__(self, G=None):
        if G:
            self.nodes = G.nodes
            self.adj = G.adj
        else:
            self.nodes = set()
            self.adj = {}

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.add(node)
            self.adj[node] = {}

    def add_edge(self, node1, node2, weight=1):
        if not node1 in self.nodes:
            self.add_node(node1)

        if not node2 in self.nodes:
            self.add_node(node2)

        self.adj[node1][node2] = weight
        self.adj[node2][node1] = weight

    def add_nodes_from(self, nodes):
        for node in nodes:
            self.add_node(node)

    def add_edges_from(self, edges):
        for edge in edges:
            if len(edge)==2:
                self.add_edge(edge[0], edge[1])
            elif len(edge)==3:
                self.add_edge(edge[0], edge[1], edge[2])
            else:
                raise ValueError('edges shape mismatch')

    def adjacency(self, node):
        self.__check_node(node)
        return self.adj[node]

    def degree(self, node):
        self.__check_node(node)
        return len(self.nodes[node])

    def remove_node(self, node):
        self.__check_node(node)
        for adj in self.adjacency(node):
            self.adj[adj].pop(node, None)
        self.adj.pop(node)

    def remove_edge(self, node1, node2):
        self.__check_node(node1)
        self.__check_node(node2)

        self.adj[node1].pop(node2, None)
        self.adj[node2].pop(node1, None)

    @property
    def max_degree(self):
        max_degree = 0
        for node in self.nodes:
            degree = self.degree(node)
            if degree > max_degree:
                max_degree = degree
        return max_degree

    @property
    def average_degree(self):
        V = self.number_of_nodes(self)
        if V:
            return self.number_of_edges(self)/V
        else:
            return 0

    def to_string(self):
        s = '%d verticies, %d edges \n '%(self.number_of_nodes, self.number_of_edges)
        for node in self.nodes:
            s += 'vertex {}: '.format(node)
            for e, w in self.adjacency(node).items():
                s += '{}, '.format(e)
            s += '\n '
        return s

    @property
    def number_of_nodes(self):
        return len(self.nodes)

    @property
    def number_of_edges(self):
        return sum([len(self.adjacency(node)) for node in self.nodes])

    @property
    def number_of_self_loops(self):
        return len([node for node in self.nodes if node in self.adjacency(node)])

    def __check_node(self, node):
        assert node in self.nodes, "node not exists"

