import re

def process_instructions(instructions):
    enable_disable = "do()"
    total_part_one, total_part_two = 0, 0

    for instruction in instructions:
        if instruction in {"do()", "don't()"}:
            enable_disable = instruction
            continue
        nums = list(map(int, re.findall(r"\d{1,3}", instruction)))
        result = nums[0] * nums[1]
        total_part_one += result
        if enable_disable == "do()":
            total_part_two += result

    return total_part_one, total_part_two

with open("input.txt") as f:
    full_text = "".join(line.strip() for line in f)

instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", full_text)

total_part_one, total_part_two = process_instructions(instructions)
print(total_part_one)
print(total_part_two)
