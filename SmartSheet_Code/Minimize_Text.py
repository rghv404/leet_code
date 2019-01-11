import re

'''
Current problems and my suggetions:
* Simply minimizing the occurences of alphabets is not enough, the minimize
    function essentially has to act as a code/text Parser and with an exhautive
    list of non_identifiers. This can include comment identifiers -> /**/ and string
    indetifiers --> "" etc, anything within these identifiers can be skipped from bein reduced

* Additioanlly, In one pass we can reduce the letters and in second pass we can reduce the
    non_identifiers especially if they have a length greater than 2. For e.g
    statement time456ontime456 becomes time456on$0456 in first pass and
    something like time456on$0$$1 with $$1 representing the 1st non_identifier
    of it's kind. This will take care of large white space characters as well.
    The decode will happen bottom up, with non_identifiers decoded first
    following the alphabets/identifiers

* We should also check length of each replaced word so something as basic as I and other
    single letter identifiers are not replaced with a complicated versions of
    backrefernces

* Another approach to treat white space characters would be to encode them
    separately with something indicating their length for e.g.
    "Great Politics is               great politics." should become
    "Great Politics is$w15 $0 $1". Again this would be efficient only for white spaces
    more than 3 or 4 characters long.
    Encoding single white space characters may cause more harm in terms of storage
    space for long texts.

* Encode new lines similarly as /n.

* In general, we should not treat any thing more than lenght 2 as non identifiers and should infact
encode them as well.

'''


def minimize(input):
    non_identifiers = re.findall('[^a-zA-Z]+', input)
    text = re.sub('[^a-zA-Z]+', ' ', input)
    text = text.split()
    dict_ = {}
    res = ''
    for i, word in enumerate(text):

        if word in dict_:
            text[i] = '$' + str(dict_[word])
        else:
            dict_[word] = i

    # if the string does not begin with non_identifiers
    if len(text) >= len(non_identifiers):
        for k in range(len(text)):
            if k < len(non_identifiers):
                res += text[k] + non_identifiers[k]
            else:
                res += text[k]
    else:
        for k in range(len(non_identifiers)):
            if k < len(text):
                res += non_identifiers[k] + text[k]
            else:
                res += non_identifiers[k]
    return res
