def isCorrectRect(rec):
    if rec[0][0] <= rec[1][0] and rec[0][1] <= rec[1][1]:
        return True
    else:
        return False
