

class Validator:

    @classmethod
    def validate(cls, input_string):
        first_digit_weight_dict = dict()

        try:
            if [input_string[3], input_string[7], input_string[11]] != ['.', '.', '-']:
                return False
        except IndexError:
            pass

        formatted_string = cls.format_(input_string)
        print(formatted_string)

        if len(set(list(formatted_string))) == 1 or len(formatted_string) != 11:
            return False

        [first_digit_weight_dict.update({index: each}) for index, each in zip(range(10, 1, -1), formatted_string[:-2])]
        print(first_digit_weight_dict)

        first_digit_mul_list_sum = sum([k*int(v) for k, v in first_digit_weight_dict.items()])
        first_digit_div = divmod(first_digit_mul_list_sum, 11)

        first_digit_remaining = 11 - first_digit_div[1]

        if first_digit_remaining > 9:
            first_digit_remaining = 0

        if first_digit_remaining != int(formatted_string[-2]):
            print(f'{first_digit_remaining} != {int(formatted_string[-2])}')
            return False

        second_digit_weight_dict = dict()

        [second_digit_weight_dict.update({index: each}) for index, each in zip(range(11, 1, -1), formatted_string[:-1])]
        second_digit_mul_list_sum = sum([k*int(v) for k, v in second_digit_weight_dict.items()])
        second_digit_div = divmod(second_digit_mul_list_sum, 11)

        second_digit_remaining = 11 - second_digit_div[1]
        
        if second_digit_remaining > 9:
            second_digit_remaining = 0

        if second_digit_remaining != int(formatted_string[-1]):
            return False

        return True

    @classmethod
    def format_(cls, input_string):
        return ''.join([each for each in input_string if each not in ['.', '-']])

