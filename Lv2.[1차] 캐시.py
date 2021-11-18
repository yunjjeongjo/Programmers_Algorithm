def solution(cacheSize, cities):
    answer = 0
    cache = []

    for i in range(len(cities)):
        cities[i] = cities[i].lower()
    if cacheSize == 0:
        answer = 5 * len(cities)
    else:
        for i in range(len(cities)):

            if cities[i] in cache:
                cache.remove(cities[i])
                cache.append(cities[i])
                answer += 1
            else:
                if len(cache) >= cacheSize:
                    cache.pop(0)
                cache.append(cities[i])
                answer += 5
    print(cache)
    return answer