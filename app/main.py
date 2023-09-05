import sys

# import pyparsing - available if you need it!
# import lark - available if you need it!


def match_character(char, pattern):
    return char == pattern


def match_digit(char):
    return char.isdigit()


def match_alphanumeric(char):
    return char.isalnum()


def match_character_groups(input_char, pattern):
    group = pattern.split("]")[0]
    character_in_group = any(char == input_char for char in group.replace("^", ""))
    matched_length = [character_in_group, len(group) + 2]
    if group.startswith("^"):
        matched_length[0] = not matched_length[0]
    return matched_length


def try_match(input_line, pattern):
    pattern_ind, pattern_end = 0, len(pattern)
    line_ind, line_end = 0, len(input_line)

    while line_ind < line_end and pattern_ind < pattern_end:
        char = input_line[line_ind]
        pattern_left = pattern[pattern_ind:]

        if pattern_left.startswith("\d") and match_digit(char):
            pattern_ind += 2
        elif pattern_left.startswith("\w") and match_alphanumeric(char):
            pattern_ind += 2
        elif pattern_left.startswith("["):
            matched, length = match_character_groups(char, pattern_left[1:])
            if matched:
                pattern_ind += length
            else:
                return False
        elif pattern_ind < pattern_end - 1 and pattern[pattern_ind + 1] == "+":
            pattern_ind += 2
            matched = match_one_or_more_times(input_line[line_ind:], pattern_left[0])
            if matched >= 0:
                line_ind += matched
            else:
                return False
        elif pattern_ind < pattern_end - 1 and pattern[pattern_ind + 1] == "?":
            pattern_ind += 2
            line_ind += match_zero_or_one_times(input_line[line_ind:], pattern_left[0])
        elif match_character(char, pattern_left[0]):
            pattern_ind += 1
        else:
            return False
        line_ind += 1

    return pattern_ind == pattern_end


def match_zero_or_one_times(input_line, pattern):
    return 0 if input_line[0] == pattern else -1


def match_one_or_more_times(input_line, pattern):
    times = 0
    for char in input_line:
        if char == pattern:
            times += 1
        else:
            break
    return times - 1


def match_pattern(input_line, pattern):
    start_ind, end_ind = len(input_line) - 1, -1
    if pattern.startswith("^"):
        start_ind = 0
        pattern = pattern[1:]
    if pattern.endswith("$"):
        pattern = reverse_pattern(pattern)
        start_ind = 0
        input_line = input_line[::-1]
    for ind in range(start_ind, end_ind, -1):
        if try_match(input_line[ind:], pattern):
            return True
    return False


def reverse_pattern(pattern):
    return (
        pattern.replace("\\w", "w\\")
        .replace("\\d", "d\\")
        .replace("]", "*")
        .replace("[", "]")
        .replace("*", "[")[:-1][::-1]
    )


def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read().replace("\n", "")

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    # Uncomment this block to pass the first stage
    if match_pattern(input_line, pattern):
        print(f"matched {pattern} in {input_line}")
        exit(0)
    else:
        print(f"no match")
        exit(1)


if __name__ == "__main__":
    main()
