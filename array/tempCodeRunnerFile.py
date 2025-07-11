num = str(num)
    for i in num:
        if i not in rev:
            return False
    return True