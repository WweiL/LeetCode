def reverse(s):
    #  Hi, nice to see you. 变为 you, see to nice Hi.
    # reverse the input string word-wise and maintain the position of commmas unchanged
    n = len(s)
    words = []
    tmp = ""
    ans = [""] * n
    pos = -1
    for i in range(n):
        if s[i].isalnum():
            tmp += s[i]
        else:
            if(tmp != ""):
                words.append(tmp)
                tmp = ""
                pos += 2
                ans[pos] = s[i]
            else:
                pos += 1
                ans[pos] = s[i]

    for i in range(n):
        if len(words) == 0:
            break
        if ans[i] != "":
            continue
        ans[i] = words.pop()
    return "".join(ans)
