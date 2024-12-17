



def do_task_1(file_name):
    import re

    return_value = 0

    with open(file_name, 'r') as file:
        for line in file:

            # Regular expression to match the correct pattern
            pattern = r"mul\(\d+,\d+\)"

            # Find all matches
            matches = re.findall(pattern, line)

            for entry in matches:
                # Regular expression to extract all numbers
                pattern = r"\d+"

                # Find all numbers in the string
                numbers = re.findall(pattern, entry)
                return_value += int(numbers[0])*int(numbers[1])




    return return_value


def do_task_2(file_name):
    import re

    return_value = 0
    do = True

    with open(file_name, 'r') as file:
        for line in file:

            # List of patterns to search for in order
            patterns = [r"mul\(\d+,\d+\)", r"don't\(\)", r"do\(\)"]


            # Combine the patterns into a single regex
            combined_pattern = "|".join(patterns)

            # Find all matches in the string in order
            matches = re.findall(combined_pattern, line)

            for entry in matches:

                if entry == "don't()":
                    do = False

                elif entry == "do()":
                    do = True

                else:
                    if do:
                        # Regular expression to extract all numbers
                        pattern = r"\d+"

                        # Find all numbers in the string
                        numbers = re.findall(pattern, entry)
                        return_value += int(numbers[0]) * int(numbers[1])

    return return_value
