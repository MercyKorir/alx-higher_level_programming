#!/usr/bin/python3
multiple_returns = __import__("8-multiple_returns").multiple_returns

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("{:d} {}".format(length, first))
