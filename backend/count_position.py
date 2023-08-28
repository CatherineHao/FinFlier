def find_position(text, word):
    index = text.find(word)
    end_index = index + len(word) - 1 if index != -1 else -1
    if index == -1:
        return None
    else:
        return [index, end_index]

input_text = "China's banks extended CNY 345.9 billion in new yuan loans in July 2023, the least since November of 2009 and well below market forecasts of CNY 800 billion. The value is also much lower than CNY 679 billion a year earlier and CNY 3.05 trillion in June, after a record CNY 15.73 trillion loans in the first half of the year. The reading adds to further evidence of a lacklustre economic recovery in China although July is usually a weak month for financing activities, with banks not in a rush to meet their lending targets at the beginning of the quarter."
input_word = "3.05"
start, end = find_position(input_text, input_word)
print("First occurrence of '{}' is at index: {} and end at {}".format(input_word, start, end))
