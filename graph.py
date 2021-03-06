from union_find import UF 


class Graph(object):

    def __init__(self, count_v):
        self.adj = []
        self.edges = []
        for _ in range(count_v):
            self.adj.append([])

    def add_edge(self, u, v):
        self.adj[u].insert(0, v)
        self.adj[v].insert(0, u)

    def __repr__(self):
        s = ''
        for v in range(len(self.adj)):
            s += str(v) + ' : '
            for w in self.adj[v]:
                s += '{}, '.format(str(w))
            s += '\n'
        return s


class DiGraph(Graph):

    def add_edge(self, u, v):
        self.adj[u].insert(0, v)


class Edge(object):

    def __init__(self, v, w, weight=1):
        self.v = v
        self.w = w
        self.weight = weight

    def either(self):
        return self.v

    def other(self, v):
        return self.w if v == self.v else self.v

    def weight(self):
        return self.weight

    def __repr__(self):
        return '{}-{}-{}'.format(self.v, self.w, self.weight)


class DirectedEdge(object):

    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def from_p(self):
        return self.v

    def to(self):
        return self.w

    def __repr__(self):
        return '{}-{}-{}'.format(self.v, self.w, self.weight)

class EdgeWeightGraph(Graph):

    def add_edge(self, e):
        v = e.either()
        w = e.other(v)

        self.adj[v].insert(0, e)
        self.adj[w].insert(0, e)
        self.edges.append(e)


class DepthFirstPath(object):

    def __init__(self, graph, s):
        self.graph = graph
        self.s = s
        self.marked = [False] * len(self.graph.adj)
        self.edge_to = [-1] * len(self.graph.adj)
        self.edge_to[s] = s
        self.marked[s] = True
        self.dfs(s)

    def dfs(self, v):
        for w in self.graph.adj[v]:
            if not self.marked[w]:
                self.edge_to[w] = v
                self.marked[w] = True
                self.dfs(w)

    def path_to(self, v):
        if self.edge_to[v] < 0:
            return 'Cant reachable'
        path_stack = []
        path_stack.append(v)

        while True:
            w = self.edge_to[v]
            if w == self.s:
                path_stack.append(w)
                break
            path_stack.append(w)
            v = w

        while path_stack:
            w = path_stack.pop()
            print w, ' ',
        print '\n'


class BreathFirstPath(object):

    def __init__(self, g, s):
        self.s = s
        self.g = g
        self.marked = [False] * len(g.adj)
        self.edge_to = [-1] * len(g.adj)
        self.queue = []
        self.marked[s] = [True]
        self.edge_to[s] = s
        self.queue.append(s)
        self.bfs()

    def bfs(self):
        while self.queue:
            v = self.queue.pop(0)
            for w in self.g.adj[v]:
                if not self.marked[w]:
                    self.edge_to[w] = v
                    self.marked[w] = True
                    self.queue.append(w)

    def path_to(self, v):
        if self.edge_to[v] < 0:
            return 'Cant reachable'
        path_stack = []
        path_stack.append(v)

        while True:
            w = self.edge_to[v]
            if w == self.s:
                path_stack.append(w)
                break
            path_stack.append(w)
            v = w

        while path_stack:
            w = path_stack.pop()
            print w, ' ',
        print '\n'


class DiGraphDFS(object):

    def __init__(self, g, s):
        self.marked = [False] * len(g.adj)
        self.edge_to = [-1] * len(g.adj)
        self.g = g
        self.edge_to[s] = s
        self.marked[s] = True
        self.dfs(s)

    def dfs(self, v):
        for w in self.g.adj[v]:
            if not self.marked[w]:
                self.edge_to[w] = v
                self.marked[w] = True
                self.dfs(w)

class DirectedCycle(object):

    def __init__(self, g):
        self.marked = [False] * len(g.adj)
        self.edge_to = [-1] * len(g.adj)
        self.on_stack = [False] * len(g.adj) 
        self.cycle = []
        self.g = g

        for v in range(len(g.adj)):
            if not self.marked[v]:
                self.dfs(v)

    def dfs(self, v):
        # import pdb; pdb.set_trace()
        self.on_stack[v] = True
        self.marked[v] = True
        for w in self.g.adj[v]:
            if self.has_cycle():
                return
            elif not self.marked[w]:
                self.edge_to[w] = v
                self.dfs(w)
            elif self.on_stack[w]:
                x = v
                while x != w:
                    self.cycle.append(x)
                    x = self.edge_to[x]
                self.cycle.append(w)
        self.on_stack[v] = False


    def has_cycle(self):
        return self.cycle


class DirectedTop(object):

    def __init__(self, g):
        self.g = g
        self.marked = [False] * len(g.adj)
        self.pre = []

        for v in range(len(self.g.adj)):
            if not self.marked[v]:
                self.dfs(v)

    def dfs(self, v):
        self.marked[v] = True
        self.pre.append(v)
        for w in self.g.adj[v]:
            if not self.marked[w]:
                self.dfs(w)


class LazyPrimeMST(object):

    def __init__(self, g):
        self.g = g
        self.queue = []
        self.min_pq = []
        self.marked = [False] * len(g.adj)
        self.visit(0)

        while self.min_pq:
            e = self.min_pq.pop(0)
            v = e.either()
            w = e.other(v)

            if self.marked[v] and self.marked[w]:
                continue
            self.queue.append(e)
            if not self.marked[v]:
                self.visit(v)
            if not self.marked[w]:
                self.visit(w)

    def visit(self, v):
        self.marked[v] = True
        for e in self.g.adj[v]:
            if not self.marked[e.other(v)]:
                self.min_pq.append(e)
                self.min_pq.sort(key=lambda s: s.weight)


class PrimeMST(object):
    'not complete, need to be done future'

    def __init__(self, g):
        self.g = g
        self.edge_to = [-1] * len(self.g.adj)
        self.marked = [False] * len(self.adj)
        self.dist_to = [float('inf')] * len(self.g.adj)
        self.min_pq = {}

        self.dist_to[0] = 0
        self.min_pq.append([0, 0.0])
        while self.min_pq:
            self.visit(self.min_pq.pop(0)[0])

    def visit(self, v):
        self.marked[v] = True
        for e in self.g.adj[v]:
            w = e.other(v)
            if self.marked[w]:
                continue
            if e.weight() < dist_to[w]:
                self.edge_to[w] = e


class KruskaMST(object):

    def __init__(self, g):
        self.g = g
        self.mst = []
        self.min_pq = []
        self.uf = UF(len(self.g.adj))
        for e in self.g.edges:
            self.min_pq.append(e)
        self.min_pq.sort(key=lambda e: e.weight)

        while self.min_pq and len(self.msf) < len(self.g.adj) - 1:
            e = self.min_pq.pop(0)
            v = e.either()
            w = e.other(v)

            if self.uf.find(v) == self.uf.find(w):
                continue
            self.uf.union(v, w)
            self.mst.append(e)


class EdgeWeightedDigraph(EdgeWeightGraph):

    def add_edge(self, e):
        self.adj[e.from_p()].insert(0, e)
        self.edges.append(e)


class Dijkstra(object):

    def __init__(self, g, s):
        self.g = g
        self.s = s
        self.edge_to = [None] * len(self.g.adj)
        self.dist_to = [float('inf')] * len(self.g.adj)
        self.pq = []

        self.pq.append((s, 0))
        self.dist_to[0] = 0
        while self.pq:
            self.relax(self.pq.pop(0)[0])

    def relax(self, v):
        for e in self.g.adj[v]:
            w = e.to()
            if self.dist_to[w] > self.dist_to[v] + e.weight:
                self.dist_to[w] = self.dist_to[v] + e.weight
                self.edge_to[w] = e
                if w in [d[0] for d in self.pq]:
                    for i, j in enumerate(self.pq):
                        self.pq[i] = (j[0], self.dist_to[w])
                else:
                    self.pq.append((w, self.dist_to[w]))
                self.pq.sort(key=lambda a: a[1])


def test():
    g = Graph(6)
    with open('./tinyCG.txt') as fp:
        for l in fp:
            v, w = map(int, l.split(' '))
            self.dfs(s)
            g.add_edge(v, w)
    print g

    dfs = DepthFirstPath(g, 0)
    dfs.path_to(4)
    bfs = BreathFirstPath(g, 0)
    bfs.path_to(4)


def digraph_test():
    g = DiGraph(13)
    with open('./tinyDG.txt') as fp:
        for l in fp:
            v, w = map(int, l.split(' '))
            g.add_edge(v, w)
    print g
    dfs = DiGraphDFS(g, 0)
    print dfs.edge_to
    cycle_findder = DirectedCycle(g)
    print cycle_findder.edge_to
    print cycle_findder.cycle
    top = DirectedTop(g)
    print top.pre


def test_weight_graph():
    g = EdgeWeightGraph(8)
    with open('./tinyEWG.txt') as fp:
        for l in fp:
            v, w, weight = l.split(' ')
            e = Edge(int(v), int(w), float(weight))
            g.add_edge(e)

    print g
    mst = LazyPrimeMST(g)
    print mst.queue
    mst = KruskaMST(g)
    print mst.mst


def test_directed_weight_granph():
    g = EdgeWeightedDigraph(8)
    with open('./tinyEWD.txt') as fp:
        for l in fp:
            v, w, weight = l.split(' ')
            e = DirectedEdge(int(v), int(w), float(weight))
            g.add_edge(e)
    print g
    mst = Dijkstra(g, 0)
    print mst.edge_to


if __name__ == '__main__':
    test_directed_weight_granph()
