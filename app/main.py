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
    for char in input_line:
        pattern_left = pattern[pattern_ind:]
        if pattern_left.startswith("\d"):
            if match_digit(char):
                pattern_ind += 2
        elif pattern_left.startswith("\w"):
            if match_alphanumeric(char):
                pattern_ind += 2
        elif pattern_left.startswith("["):
            matched, length = match_character_groups(char, pattern_left[1:])
            if matched:
                pattern_ind += length
        elif match_character(char, pattern_left[0]):
            pattern_ind += 1
        else:
            return False
        if pattern_ind == pattern_end:
            return True


def match_pattern(input_line, pattern):
    start_ind, end_ind = len(input_line) - 1, -1
    if pattern.startswith("^"):
        start_ind = 0
        pattern = pattern[1:]
    for ind in range(start_ind, end_ind, -1):
        if try_match(input_line[ind:], pattern):
            return True
    return False


def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    if match_pattern(input_line, pattern):
        print(f"matched {pattern} in {input_line}")
        exit(0)
    else:
        exit(1)


if __name__ == "__main__":
    main()
