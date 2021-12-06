import sys
N = int(sys.stdin.readline())
rgb = []
for _ in range(N):
    rgb.append(list(map(int, sys.stdin.readline().split())))


d = [0]*1001
d[0] = min(rgb[0])
color = [0]*1001

color[0] = rgb[0].index(d[0])


def get_color_min(rgb, idx):
    m = 1000
    for i in range(3):
        if i != idx:
            if rgb[i] < m:
                m = rgb[i]
                min_idx = i
    return min_idx


for i in range(1, N):
    min_idx = get_color_min(rgb[i], color[i-1])
    d[i] = d[i-1] + rgb[i][min_idx]
    color[i] = min_idx

print(d[:N])
print(d[N-1])
