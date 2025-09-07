"""Graph representations for five small exercises."""

NODE_DICT = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}
ORDER = ['a', 'b', 'c', 'd', 'e']


def part_1_graph():
    """
    Part 1: return a list of sets (length 5, order a,b,c,d,e).
    Each set contains the LABELS of the outbound neighbors.
    Edges (from the diagram, unweighted):
      a→b, a→e, b→c, c→d, c→e, d→b
    """
    edges = [
        ('a', 'b'), ('a', 'e'),
        ('b', 'c'),
        ('c', 'd'), ('c', 'e'),
        ('d', 'b'),
    ]

    adj = [set() for _ in ORDER]
    pos = {lbl: i for i, lbl in enumerate(ORDER)}
    for u, v in edges:
        adj[pos[u]].add(v)
    return adj


def part_2_graph():
    """
    Part 2: return a list of lists (length 5, order a,b,c,d,e).
    Each inner list contains the LABELS of the outbound neighbors (no weights).
    Edges (from the diagram, unweighted):
      a→a, a→b, a→e, b→c, c→a, c→e, c→d, e→d
    """
    edges = [
        ('a', 'a'), ('a', 'b'), ('a', 'e'),
        ('b', 'c'),
        ('c', 'a'), ('c', 'e'), ('c', 'd'),
        ('e', 'd'),
    ]

    pos = {lbl: i for i, lbl in enumerate(ORDER)}
    adj = [[] for _ in ORDER]
    for u, v in edges:
        adj[pos[u]].append(v)
    return adj


def part_3_graph():
    """
    Part 3: return a list of dicts (length 5, order a,b,c,d,e).
    Each dict maps LABEL -> weight for outbound neighbors.
    Weighted edges (from the diagram):
      a→a(8), a→b(1), c→a(2), b→c(3), a→e(4), c→e(4)
    """
    edges = [
        ('a', 'a', 8),
        ('a', 'b', 1),
        ('c', 'a', 2),
        ('b', 'c', 3),
        ('a', 'e', 4),
        ('c', 'e', 4),
    ]

    pos = {lbl: i for i, lbl in enumerate(ORDER)}
    adj = [dict() for _ in ORDER]
    for u, v, w in edges:
        adj[pos[u]][v] = w
    return adj


def part_4_graph():
    """
    Part 4: return a dict of sets mapping LABEL -> set of LABEL neighbors.
    Edges (unweighted, labels):
      a→a, a→b, a→e, b→c, c→a
    """
    edges = [
        ('a', 'a'), ('a', 'b'), ('a', 'e'),
        ('b', 'c'),
        ('c', 'a'),
    ]

    graph = {lbl: set() for lbl in ORDER}
    for u, v in edges:
        graph[u].add(v)
    return graph


def part_5_graph():
    """
    Part 5: return a dict of dicts mapping LABEL -> {LABEL: weight}.
    Weighted edges:
      a→b(5), e→a(6), b→e(3), e→b(2)
    """
    edges = [
        ('a', 'b', 5),
        ('e', 'a', 6),
        ('b', 'e', 3),
        ('e', 'b', 2),
    ]

    graph = {lbl: {} for lbl in ORDER}
    for u, v, w in edges:
        graph[u][v] = w
    return graph
