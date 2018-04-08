chars = ['a', 'b', 'c', 'd']
def get_combos(c):
  if len(c) == 1:
    yield c
  else:
     yield c
     for i in range(len(c)-1):
       yield from get_combos([c[d]+c[d+1] if d == i else c[d] if d < i else c[d+1] for d in range(len(c)-1)])

final_listing = list(get_combos(chars))
last_results = list(filter(lambda x:all(len(c) < 3 for c in x), [a for i, a in enumerate(final_listing) if a not in final_listing[:i]]))

#result
#[['a', 'b', 'c', 'd'], ['ab', 'c', 'd'], ['ab', 'cd'], ['a', 'bc', 'd'], ['a', 'b', 'cd']]
