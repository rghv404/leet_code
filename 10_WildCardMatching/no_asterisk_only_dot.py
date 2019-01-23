
# recursive solution


def is_match(text, pattern):
    # we solve this first by recursion
    if not pattern:
        return not text
    first_match = bool(text) and pattern[0] in (text[0], '.')
    return first_match and is_match(text[1:], pattern[1:])

# iterative solution


def my_iter_sol(text, pattern):
    # i have no idea why i couldn't do this stupid as  question in the first
    # attempt
    if len(text) != len(pattern):
        return False
    for i, p in enumerate(pattern):
        if p not in (text[i], '.'):
            return False
    return True

# dynamic solution


def is_match_dynamic(text, pattern):


print(is_match(".adc", "aa..."))
print(my_iter_sol(".adc", "aad..."))
