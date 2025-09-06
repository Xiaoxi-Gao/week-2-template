"""Graph representations for five small exercises.

This file contains five functions (part_1_graph ... part_5_graph),
each returning a different graph representation as required.
The node order is fixed: a, b, c, d, e.
"""

NODE_DICT = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}
ORDER = ['a', 'b', 'c', 'd', 'e']


def part_1_graph():
    """
    Part 1: Return a list of sets (length 5, order a,b,c,d,e).
    Each set contains the labels of outbound neighbors.
    Edges from the diagram (unweighted):
        a→b, a→e
        b→c
        c→d, c→e
        d→b
        e→∅
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
    Part 2: Return a list of lists (length 5, order a,b,c,d,e).
    Each inner list contains the labels of outbound neighbors.
    Edges from the diagram (unweighted):
        a→a, a→b, a→e
        b→c
        c→a, c→e, c→d
        d→∅
        e→d
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
    Part 3: Return a list of dicts (length 5, order a,b,c,d,e).
    Each dict maps neighbor label -> weight.
    Edges from the diagram (weighted):
        a→a(8), a→b(1), a→e(4)
        b→c(3)
        c→a(2), c→e(4)
        d→∅
        e→∅
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
    Part 4: Return a dict of sets mapping label -> set of neighbors.
    Edges from the diagram (unweighted):
        a→a, a→b, a→e
        b→c
        c→a
        d→∅
        e→∅
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
    Part 5: Return a dict of dicts mapping label -> {neighbor: weight}.
    Edges from the diagram (weighted):
        a→b(5)
        b→e(3)
        e→b(2), e→a(6)
        c→∅
        d→∅
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
