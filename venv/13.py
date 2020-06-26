items = input("Input comma separated sequence of words")
words = [words for words in items.split(",")]
print(",".join(sorted(list(set(words)))))