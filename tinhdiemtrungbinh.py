n = int(input())
a = list(input().split())
a_min = min(a)
a_max = max(a)
for item in a:
    if item == a_min or item == a_max:
        a.remove(item)
sum = 0.0
for item in a:
    sum += float(item)
print(round(sum/len(a),2))
