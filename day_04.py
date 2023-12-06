

def parse_line_return_two_lists(input_string):

    input_string = input_string.strip('\n')
    input_string = input_string.split(": ")[1]

    input_string_list = input_string.split(" | ")

    left_list = input_string_list[0].split(" ")
    right_list = input_string_list[1].split(" ")

    num_matches = 0

    for number in right_list:
        if number in left_list:
            if number != '':
                num_matches += 1


    return num_matches







def do_task_1(file_name):
    file = open(file_name, 'r')
    Lines = file.readlines()

    sum = 0

    for line in Lines:
        num_matches = parse_line_return_two_lists(line)
        if num_matches == 0:
            line_value = 0
        else:
            line_value =  2 ** (num_matches - 1)
        sum += line_value

    return sum


def do_task_2(file_name):
    file = open(file_name, 'r')
    Lines = file.readlines()

    num_cards_won = 1
    current_card = -1

    card_list = [1] * len(Lines)

    """while num_cards_won:
        num_cards_won -= 1
        current_card += 1

        if current_card+1 > len(Lines):
            break
        line_value = parse_line_return_two_lists(Lines[current_card])

        num_cards_won += line_value"""

    for i in range(len(Lines)):
        line = Lines[i]
        cards_won = parse_line_return_two_lists(line)
        for j in range(1, cards_won+1):
            card_list[i+j] += card_list[i]

    return sum(card_list)

