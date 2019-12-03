with open('input\\day_3.txt', 'r') as f:
    path1,path2 = f.read().strip().split('\n')
    path1,path2 = [x.split(',') for x in [path1,path2]]

dx = {'R': 1, 'L': -1, 'U': 0, 'D': 0}
dy = {'R': 0, 'L': 0, 'U': 1, 'D': -1}

def find_steps(directions):
    x,y,steps = 0, 0, 0
    points = set()
    step_count = {}
    for step in directions:
        d = step[:1]
        l = int(step[1:])
        for n in range(l):
            x += dx[d]
            y += dy[d]
            points.add((x,y))
            steps += 1
            step_count.setdefault((x,y), steps)
    return points, step_count

ans1, steps1 = find_steps(path1)
ans2, steps2 = find_steps(path2)
intersections = ans1 & ans2

distance = min(abs(x) + abs(y) for x, y in intersections)
t_steps = min(steps1[point] + steps2[point] for point in intersections)

print(distance)
print(t_steps)
