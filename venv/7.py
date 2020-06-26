def find_longest_word(word_list):
    word_len=[]
    for i in word_list:
        word_len.append((len(i),i))
    word_len.sort()
    return word_len[-1][1]


print(find_longest_word(['Liverpool', 'is', 'the', 'champion']))