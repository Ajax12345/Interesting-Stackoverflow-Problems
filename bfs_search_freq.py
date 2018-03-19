class TreeNode:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data



from collections import deque, defaultdict
def bsf(tree):
  d = deque([tree])
  levels = defaultdict(list)
  count = 0
  seen = [tree.data]
  while seen:
     listing = []
     while d:
      val = d.popleft()
      if val:
         levels[count].append(val.data)
         listing.extend([val.right, val.left])
     count += 1 
     if not any(listing):
       break
     d.extend(listing)
  return levels

vals = [5, 4, 6, 7, 3, 1, 10]
t1 = TreeNode(vals[0])
for i in vals[1:]:
  t1.insert(i)

result = bsf(t1)

