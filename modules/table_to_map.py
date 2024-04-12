# This file is table_to_map.py
import sys

def tableToMap(*args):
  if len(args) == 0: return None

  table = args[0]

  index_list: list[str] = ['A', 'B', 'C', 'D', 'E', 'F']

  graph: dict = {}
  key1: str = ""
  key2: str = ""
  value: int = 0

  for row in range(len(table)) :
    for col in range(len(table[index_list[row]])):
      key1 = "{0}".format(index_list[row])
      key2 = "{0}".format(index_list[col])
      if key1 == key2: continue
      if table[key1][key2] == '0': continue
      # if graph.get(key2, {}).get(key1): continue
      value = int(table[key1][key2])
      graph.setdefault(key1, {}).setdefault(key2, value)

  return graph

if __name__ == "__main__":
    tableToMap()