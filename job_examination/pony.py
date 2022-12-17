def isInsidePolygon(pt, poly):
    c = False
    i = -1
    l = len(poly)
    j = l - 1
    while i < l - 1:
        i += 1
        print(i, poly[i], j, poly[j])
        if ((poly[i]["lat"] <= pt["lat"] and pt["lat"] < poly[j]["lat"]) or (
                poly[j]["lat"] <= pt["lat"] and pt["lat"] < poly[i]["lat"])):
            if (pt["lng"] < (poly[j]["lng"] - poly[i]["lng"]) * (pt["lat"] - poly[i]["lat"]) / (
                    poly[j]["lat"] - poly[i]["lat"]) + poly[i]["lng"]):
                c = not c
        j = i
    return c


if __name__ == '__main__':
    abc = [{'lat': 1, 'lng': 1}, {'lat': 1, 'lng': 4}, {'lat': 3, 'lng': 7}, {'lat': 4, 'lng': 4}, {'lat': 4, 'lng': 1}]
    print(isInsidePolygon({'lat': 2, 'lng': 5}, abc))
    t = int(input())
    for _ in range(t):
        x1, y1, x2, y2 = list(map(int, input().split()))
        x1, x2 = min(x1, x2), max(x1, x2)
        y = max(y1, y2)
        n = int(input())
        for _ in range(n):
            water = list(map(int, input().split()))
            abs = []
            for i in range(1, len(water), 2):
                abs.append({'lat': water[i], 'lng': water[i + 1]})
            print(isInsidePolygon({'lat': 2, 'lng': 5}, abc))

