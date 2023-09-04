import sys

# import pyparsing - available if you need it!
# import lark - available if you need it!


def match_digit(input_line):
    return any(char.isdigit() for char in input_line)


def match_alphanumeric(input_line):
    return any(char.isalnum() for char in input_line)


def match_positive_character_groups(input_line, pattern):
    chars_in_groups = "".join([group.split("]")[0] for group in pattern.split("[")])
    return any(char in input_line for char in chars_in_groups)


def match_pattern(input_line, pattern):
    if len(pattern) == 1:
        return pattern in input_line
    elif pattern == "\d":
        return match_digit(input_line)
    elif pattern == "\w":
        return match_alphanumeric(input_line)
    elif "[" in pattern and "]" in pattern:
        return match_positive_character_groups(input_line, pattern)
    else:
        raise RuntimeError(f"Unhandled pattern: {pattern}")


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
