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
            # print('in third if')
            # print(ct, "---- before -----")
            ct = ct+1
            # print(ct, "---- after -----")
            # print(new_string, 'before')
            # print(new_string.find(oc), 'index of th')
            new_string[:2]
            # print(new_string, "after slick")
            # if new_string[new_string.find(oc)-1] == 't':
            #      new_string[:new_string.find(oc)-1]
            #      print(new_string, "after remove of t")
            new_string = new_string.replace(oc,'', 1)
            # print(new_string, 'after')
            inner(new_string)
        return ct

    return inner(word)


# print(count_th('erthothdfadfafdTh'))
# print(count_th('abcthxyz'))
print(count_th('thhtthht'))


