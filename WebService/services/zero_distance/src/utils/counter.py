class Counter:

    @classmethod
    def count_zeroes(cls, string):

        acc_list = list()
        acc = 0

        try:
            for each in string:

                if each == '0':
                    acc += 1
                    acc_list.append(acc)

                else:
                    acc = 0

            return max(acc_list)

        except ValueError:
            return 0

        except TypeError:
            return ''

