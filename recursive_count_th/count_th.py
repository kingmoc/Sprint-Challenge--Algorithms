'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    ct = 0

    def inner(word):
        # print('RUN FUNCTION')
        oc = 'th'
        new_string = word
        nonlocal ct

        if oc not in word:
            return 0

        if new_string.find(oc) != -1:
            ct = ct+1
            new_string[:2]
            new_string = new_string.replace(oc,' ', 1)
            inner(new_string)
        return ct

    return inner(word)


# print(count_th('erthothdfadfafdTh'))
# print(count_th('abcthxyz'))
# print(count_th('thhtthht'))


