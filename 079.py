SUBSEQS = ["319", "680", "180", "690", "129", "620", "762", "689", "762", "318", "368", "710", "720", "710", "629",
           "168", "160", "689", "716", "731", "736", "729", "316", "729", "729", "710", "769", "290", "719", "680",
           "318", "389", "162", "289", "162", "718", "729", "319", "790", "680", "890", "362", "319", "760", "316",
           "729", "380", "319", "728", "716"]


def compute():
    num = ""
    while True:
        t = ""
        isEmpty = True
        for i in range(len(SUBSEQS)):
            if t == "":
                if len(SUBSEQS[i]) > 0:
                    t = SUBSEQS[i][0]
            else:
                isEmpty = False
                if SUBSEQS[i].__contains__(t) and SUBSEQS[i][0] != t:
                    t = SUBSEQS[i][0]
        for i in range(len(SUBSEQS)):
            SUBSEQS[i] = SUBSEQS[i].replace(t, "")
        num += t
        if isEmpty:
            print(num)
            return


compute()
