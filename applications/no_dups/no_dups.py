def no_dups(s):
    # split the string
    # iterate through and return only the ones if they dont already exist
    # python set does not maintain order

    s = s.split()

    ans = []
    for word in s:
        if word not in ans:
            ans.append(word)
    ans = ' '.join(ans)

    return ans


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))