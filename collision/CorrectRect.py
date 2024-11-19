def isCorrectRect(rec):
    for i in rec:
        if i[0][0] <= i[1][0] and i[0][1] <= i[1][1]:
            return True
        else:
            return False
