def normalized_array(input_array):
    minimum = input_array[0]
    maximum = input_array[0]

    for value in input_array:
        if value < minimum:
            minimum = value

        if value > maximum:
            maximum = value

    if maximum == minimum:
        new_array = input_array * 0
    else:
        new_array = (input_array - minimum) / (maximum - minimum)

    return new_array
