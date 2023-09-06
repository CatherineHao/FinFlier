def find_position(text, word):
    index = text.find(word)
    end_index = index + len(word) - 1 if index != -1 else -1
    if index == -1:
        return None
    else:
        return [index, end_index]

input_text = "The highest sales proportion of compact-size NEVs since 2017 is 0.54 in 2019."
input_word = "0.54"
start, end = find_position(input_text, input_word)
# print("First occurrence of '{}' is at index: {} and end at {}".format(input_word, start, end))
