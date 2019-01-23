'''
We use the frequency of characters in dictioanry and append all permuataion of
a word fro the frequnecy key
'''
import collections


def groupAnagrams(strs):
    dict_character_count = collections.defaultdict(list)
    for word in strs:
        count = [0] * 26
        for c in word:
            # update the character # to indicate that we have a certain of this
            # character in the current word
            count[ord(c) - ord('a')] += 1
        dict_character_count[tuple(count)].append(word)
    return list(dict_character_count.values())


print(groupAnagrams(["", "c", "c", "eat", "tea", "tan", "ate", "nat", "bat"]))
