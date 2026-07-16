def normalized_array(input_array):
  minimum = input_array[0]
  maximum = input_array[0]

  for value in input_array:
    if value <  minimum:
          minimum = value
    if value >  maximum:
          maximum = value

    if maximum == minimum:
        new_array = []

        for value in input_array:
          new_array.append(0)

        return new_array

    new_array = []

    for value in input_array:
          norm = (value - minimum) / (maximum - minimum)
          new_array.append(norm)

    return new_array
