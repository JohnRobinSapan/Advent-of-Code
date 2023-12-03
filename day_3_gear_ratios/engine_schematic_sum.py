data = open("day_3_gear_ratios/data.txt")
sum = 0

SYMBOLS = ["@", "#", "$", "%", "&", "*", "-", "=", "+", "/"]
prev_line = ""
prev_char = ""
check_part = {}
list_parts = {}


f = open("day_3_gear_ratios/test_data.txt", "w")
passed_parts = {}
for idx, line in enumerate(data):
    cur_num = ""
    list_parts = dict(check_part)
    check_part = {}
    start_idx = -1
    end_idx = -1
    log = line
    for idx_char, char in enumerate(line):
        if char.isnumeric():
            if start_idx == -1:
                start_idx = idx_char
            cur_num += char
        elif cur_num:
            end_idx = idx_char
            # print(idx_char, char, start_idx, end_idx)
            list_parts.update(
                {cur_num: {"start": start_idx, "end": end_idx, "idx": idx}}
            )
            start_idx = -1
            cur_num = ""
        prev_char = char
    for part in list_parts:
        adj_prev = prev_line[
            list_parts[part]["start"] - 1
            if list_parts[part]["start"] != 0
            else 0 : list_parts[part]["end"] + 1
        ]
        adj_line = line[
            list_parts[part]["start"] - 1
            if list_parts[part]["start"] != 0
            else 0 : list_parts[part]["end"] + 1
        ]
        # print(adj_prev,part,part in adj_prev or part in adj_line)
        # print(adj_line,part,part in adj_prev or part in adj_line)
        if any(num in adj_prev or num in adj_line for num in SYMBOLS) and (
            part in adj_prev or part in adj_line
        ):
            # print(adj_prev)
            # print(adj_line)
            # print("Passed!!!!!", {part: list_parts.get(part)})
            passed_parts.update({part: list_parts.get(part)})
            sum += int(part)
        elif part in adj_prev or part in adj_line:
            # print(adj_prev)
            # print(adj_line)
            # print("Failed", {part: list_parts.get(part)})
            # Add part to check next line
            check_part.update({part: list_parts.get(part)})
        # else:
        #     print(adj_prev, part)
        #     print(adj_line, part)
    prev_line = line.strip()

# print(passed_parts)

data.seek(0)
for idx, line in enumerate(data):
    log = line
    for part in passed_parts:
        if idx == passed_parts[part]["idx"]:
            # print({part: passed_parts.get(part)})
            re = ""
            for _ in part:
                re += "."
            log = (
                log[: passed_parts[part]["start"]]
                + re
                + log[passed_parts[part]["end"] :]
            )
    f.write(log)

f.close()

print(sum)
data.close()
