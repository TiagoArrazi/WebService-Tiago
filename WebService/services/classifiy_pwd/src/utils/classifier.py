import string
import itertools


class Classifier:

    """
    RULES:
        - At least 8 characters
        - At least 1 lower case character
        - At least 1 upper case character
        - At least 1 number
        - At least 1 special character
        - No more than 2 consecutive characters
        - No sequential characters

    FROM 1 TO NONE VIOLATIONS WILL RESULT IN A STRONG PASSWORD (2)
    2 VIOLATIONS WILL RESULT IN A GOOD PASSWORD (1)
    3 OR MORE VIOLATIONS WILL AUTOMATICALLY RESULT IN A WEAK PASSWORD (0)

    """

    @classmethod
    def is_sequential(cls, pwd):
        seq = "{}{}{}".format(string.ascii_letters, string.digits, string.punctuation)
        positions = [seq.index(e) for e in pwd]
        acc = 0
        list_acc = list()

        for i, p in enumerate(positions):
            try:
                if p == positions[i + 1] - 1:
                    acc += 1
                else:
                    list_acc.append(acc)
                    acc = 0

            except IndexError:
                list_acc.append(acc)
                for seq in list_acc:
                    if seq:
                        return True
                return False

    @classmethod
    def is_consecutive(cls, pwd):
        consecs = [(char, len(list(group))) for char, group in itertools.groupby(pwd)]
        if max(each[1] for each in consecs) >= 3:
            return True
        return False

    @classmethod
    def classify(cls, pwd):
        upper_case = set(list(string.ascii_uppercase))
        lower_case = set(list(string.ascii_lowercase))
        digits = set(list(string.digits))
        symbols = set(list(string.punctuation))

        set_pwd = set(list(pwd))
        features = list()
        penalties = list()

        if len(pwd) < 8:
            features.append(len(pwd) - 8)
            print("[FATAL] Password shorter than 8 characters")
            return 0

        if not set_pwd.intersection(upper_case):
            penalties.append("[WARNING] Missing upper case characters")

        if not set_pwd.intersection(lower_case):
            penalties.append("[WARNING] Missing lower case characters")

        if not set_pwd.intersection(digits):
            penalties.append("[WARNING] Missing digits")

        if not set_pwd.intersection(symbols):
            penalties.append("[WARNING] Missing special characters")

        if cls.is_consecutive(pwd=pwd):
            penalties.append("[WARNING] 3 or more consecutive characters were found")

        if cls.is_sequential(pwd=pwd):
            penalties.append("[WARNING] Sequential characters were found")

        [print(p) for p in penalties]

        if len(penalties) < 2:
            print("[SUCCESS] Minimal to none rule violation, password acknowledged as STRONG")
            return 2

        elif 2 <= len(penalties) < 3:
            print("[SUCCESS] Moderate rule violation, password acknowledged as GOOD")
            return 1

        elif len(penalties) >= 3:
            print("[FAIL] Too many rules were violated, password acknowledged as WEAK")
            return 0
