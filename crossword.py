def create_crossword_indices():
  tuple_list = []

  first_string = "OIMDIHEIAFNL"
  second_string = "CHJDBJMHPJKD"

  for i,fschar in enumerate(first_string):
    for j,sschar in enumerate(second_string):
      if sschar.upper() == fschar.upper():
        tuple_list.append((i,j))

  if not tuple_list:
    return None
  else:
    return tuple_list

create_crossword_indices()