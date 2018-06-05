from typing import NamedTuple
import re
class Token(NamedTuple):
   value:str
   type:str

class Parse:
  grammer = r'\w+|\)|\('
  types = [('alpha', '\w+'), ('Oparen', '\('), ('Cparen', '\)')]
  def __init__(self, parsed):
     self.parsed = iter(parsed)
     self.stack = []
     self.parse()
  def parse(self):
    start = next(self.parsed, None)
    if start and start.type != 'Cparen':
      if start.type == 'alpha':
         self.stack.append(start.value)
      elif start.type == 'Oparen':
         _p = Parse(self.parsed)
         self.parsed = _p.parsed
         self.stack.append(_p.stack)
      self.parse()
  def __len__(self):
     return sum(isinstance(i, str) for i in self.stack[-1])
  def __getitem__(self, func):
     return self.__class__.find_length(func, self.stack)
  @classmethod
  def find_length(cls, val, params):
     for i in range(len(params)-1):
        if params[i] == val:
          return sum(not isinstance(i, list) for i in params[i+1])
        if isinstance(params[i+1], list):
          return cls.find_length(val, params[i+1])
  @staticmethod
  def tokenize(d):
    return [Token(i, [a for a, b in Parse.types if re.findall(b, i)][0]) for i in re.findall(Parse.grammer, d)]

if __name__ == '__main__':
  s = ['a(b(c d) f)', 'e(a(h f))', 'b(c a(d(f) h(i j) l(2 k z)))']
  c = list(map(lambda x:Parse(Parse.tokenize(x)), s))
  print([i['a'] for i in c])
