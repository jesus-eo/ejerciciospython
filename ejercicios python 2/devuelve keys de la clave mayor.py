'''oldest({
  "Emma": 71,
  "Jack": 45,
  "Amy": 15,
  "Ben": 29
}) ➞ "Emma"'''
def oldest(people):
   p = people.values()
   maximo = max(p)

   y = []
   for k, v in people.items():
      if v == maximo:
        y.append(k)
        return y



print(oldest({
  "Emma": 71,
  "Jack": 45,
  "Amy": 15,
  "Ben": 29
}))
