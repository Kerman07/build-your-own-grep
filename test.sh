#!/bin/bash

declare test_cases
test_cases=(
  "Pattern='ca?t' Input='cat' ExpectedExitCode=0"
  "Pattern='ca?t' Input='act' ExpectedExitCode=0"
  "Pattern='ca?t' Input='dog' ExpectedExitCode=1"
  "Pattern='ca?t' Input='cag' ExpectedExitCode=1"
  "Pattern='d' Input='dog' ExpectedExitCode=0"
  "Pattern='f' Input='dog' ExpectedExitCode=1"
  "Pattern='\\d' Input='123' ExpectedExitCode=0"
  "Pattern='\\d' Input='apple' ExpectedExitCode=1"
  "Pattern='\\w' Input='\$!?' ExpectedExitCode=1"
  "Pattern='\\w' Input='word' ExpectedExitCode=0"
  "Pattern='[abcd]' Input='a' ExpectedExitCode=0"
  "Pattern='[abcd]' Input='efgh' ExpectedExitCode=1"
  "Pattern='[abc][opq]p' Input='apple' ExpectedExitCode=0"
  "Pattern='[^xyz]' Input='apple' ExpectedExitCode=0"
  "Pattern='[^anb]' Input='banana' ExpectedExitCode=1"
  "Pattern='\\d apple' Input='sally has 3 apples' ExpectedExitCode=0"
  "Pattern='\\d apple' Input='sally has 1 orange' ExpectedExitCode=1"
  "Pattern='\\d\\d\\d apples' Input='sally has 124 apples' ExpectedExitCode=0"
  "Pattern='\\d\\\\d\\\\d apples' Input='sally has 12 apples' ExpectedExitCode=1"
  "Pattern='\\d \\w\\w\\ws' Input='sally has 3 dogs' ExpectedExitCode=0"
  "Pattern='\\d \\w\\w\\ws' Input='sally has 4 dogs' ExpectedExitCode=0"
  "Pattern='\\d \\w\\w\\ws' Input='sally has 1 dog' ExpectedExitCode=1"
  "Pattern='^log' Input='log' ExpectedExitCode=0"
  "Pattern='^log' Input='slog' ExpectedExitCode=1"
  "Pattern='^[abc]og' Input='dogcat' ExpectedExitCode=1"
  "Pattern='^[ojd]o\w' Input='dogcat' ExpectedExitCode=0"
  "Pattern='cat$' Input='cat' ExpectedExitCode=0"
  "Pattern='cat$' Input='cats' ExpectedExitCode=1"
  "Pattern='ca+t' Input='caaats' ExpectedExitCode=0"
  "Pattern='ca+t' Input='cat' ExpectedExitCode=0"
  "Pattern='ca+t' Input='act' ExpectedExitCode=1"
  "Pattern='ca?t' Input='cat' ExpectedExitCode=0"
  "Pattern='ca?t' Input='act' ExpectedExitCode=0"
  "Pattern='ca?t' Input='dog' ExpectedExitCode=1"
  "Pattern='ca?t' Input='cag' ExpectedExitCode=1"
  "Pattern='o[iug]ca?t+' Input='dogct' ExpectedExitCode=0"
  "Pattern='c.t' Input='cat' ExpectedExitCode=0"
  "Pattern='c.t' Input='cot' ExpectedExitCode=0"
  "Pattern='c.t' Input='car' ExpectedExitCode=1"
  "Pattern='o[dg].a?t+' Input='dogct' ExpectedExitCode=0"
)

# Initialize counters for passed and failed test cases
passed=0
failed=0

# Loop through the test cases
for i in "${!test_cases[@]}"; do
  eval "${test_cases[$i]}"
  
  # Run the grep command and capture its exit code
  result=$(echo "$Input" | ./your_grep.sh -E "$Pattern")
  exit_code=$?

  # Check if the exit code matches the expected exit code
  if [ $exit_code -eq $ExpectedExitCode ]; then
    passed=$((passed + 1))
  else
    echo "Test case failed: Pattern=\"$Pattern\", Input=\"$Input\", ExitCode=$exit_code, ExpectedExitCode=$ExpectedExitCode"
    failed=$((failed + 1))
  fi
done

# Print the summary
echo "$passed test cases passed"
