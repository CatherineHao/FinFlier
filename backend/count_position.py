def find_position(text, word):
    index = text.find(word)
    end_index = index + len(word) - 1 if index != -1 else -1
    return index, end_index

input_text = "In 2023, the sales proportion of NEVs that were subcompact and below declined to 30%, from 61% in 2017. During the same periods of comparison, the mix of compact and midsize-to-large NEVs increased to 70% from 39%, reflecting the upgrade trend in terms of vehicle size."
input_word = "70%"
start, end = find_position(input_text, input_word)
print("First occurrence of '{}' is at index: {} and end at {}".format(input_word, start, end))
