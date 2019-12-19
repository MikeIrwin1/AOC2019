from collections import defaultdict, deque

orbits = defaultdict(list)
edges = defaultdict(list)

with open('AoC/input/day_6.txt') as f:
    for row in f:
        body, obj = row.strip().split(')')
        orbits[body].append(obj)
        edges[body].append(obj)
        edges[obj].append(body)

def count_orbits(body):
    if body not in orbits:
        return 0
    bodies = orbits[body]
    return len(orbits[body]) + sum([count_orbits(body) for body in bodies])

def find_shortest_path(graph, start, end):
        dists = {start: 0}
        q = deque([start])
        seen = {start}
        while end not in dists:
            at = q.pop()
            dist = dists[at]
            for neighbour in graph[at]:
                if neighbour in seen:
                    continue
                seen.add(neighbour)
                dists[neighbour] = dist + 1
                q.append(neighbour)
        return dists[end]

print('Part 1: ', sum(count_orbits(body) for body in orbits.keys()))

you_body = [k for k, v in orbits.items() if 'YOU' in v].pop()
san_body = [k for k, v in orbits.items() if 'SAN' in v].pop()

print('Part 2:', find_shortest_path(edges, you_body, san_body))