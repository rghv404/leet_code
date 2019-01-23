'''
The solution works but time limit exceeds.
'''


def groupAnagrams(strs):
    res = []
    # boundary cases
    if len(strs) == 1:
        return [strs]
    # feed all words in dictionary so that we may skip words already visited
    dict_ = {}
    # handling empty strings
    empty_patterns = ["" for s in strs if s == ""]
    if len(empty_patterns) > 0:
        res.append(empty_patterns)

    for word in strs:
        if word == "":
            continue
        if word not in dict_:
            dict_[word] = 1
        else:
            dict_[word] += 1

    for word in strs:
        if word in dict_ and dict_[word] > 0:
            all_combs = permute(word)
            common_perms = get_common_elements(all_combs, strs)

            for perm in common_perms:
                dict_[perm] = True
            res.append(common_perms)

    return res


def get_common_elements(combs, strs):
    # this methoid of getting common works in O_N time
    return [word for word in combs if word in strs]


def permute(word):
    res = []
    if len(word) == 0:
        return ''
    if len(word) == 1:
        return word
    for i in range(len(word)):
        first = word[i]
        rem_words = word[:i] + word[i+1:]
        for c in permute(rem_words):
            res.append(first + c)
    return res


res = groupAnagrams(['', "c", "c", "eat", "tea", "tan", "ate", "nat", "bat", ''])
print(res)
