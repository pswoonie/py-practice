# This file is table_to_map.py

def tableToMap(*args):
  if len(args) == 0: return None

  table = args[0]

  index_list = ['A', 'B', 'C', 'D', 'E', 'F']

  dict_tb = {
    'AB':0,
    'AC':0,
    'AF':0,
    'BC':0,
    'BD':0,
    'CD':0,
    'CF':0,
    'DE':0,
    'EF':0
  }

  key = ""

  for row in range(len(table)) :
    for col in range(len(table[index_list[row]])):
      key: str = "{}{}".format(index_list[row], index_list[col])
      if key in dict_tb.keys():
        dict_tb[index_list[row]+index_list[col]] = table[index_list[row]][index_list[col]]

  return dict_tb

if __name__ == "__main__":
    tableToMap()