f = open('input.txt')
output = []
NUMS = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
for line in f: 
    first, last = None, None
    for i, c in enumerate(line): 
        if c.isdigit():
            if not first: 
                first = c
            last = c
        for num_index, word in enumerate(NUMS):
            if line[i : i + len(word)] == word:
                if not first: 
                    first = str(num_index + 1)
                last = str(num_index + 1)
    output.append(int(first + last))

print(sum(output))