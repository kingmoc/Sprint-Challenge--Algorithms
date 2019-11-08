'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
ct = 0
def count_th(word):
    # print('RUN FUNCTION')
    oc = 'th'
    new_string = word
    global ct

    if oc not in word:
        return 0
    if not word:
        return
    if new_string.find(oc) != -1:
        # print('in third if')
        # print(ct, "---- before -----")
        ct = ct+1
        # print(ct, "---- after -----")
        # print(new_string, 'before')
        new_string = new_string.replace(oc,'', 1)
        # print(new_string, 'after')
        count_th(new_string)

        # print(word.find(oc))
        # # word[word.find(oc):word.find(oc)+2]
        # x = word.replace(oc,'')
        # print(word, 'or')
        # print(x, 'new')
    return ct


# print(count_th('erthothdfadfafdTh'))
# print(count_th('abcthxyz'))


