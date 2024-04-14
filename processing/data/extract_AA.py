import re
from tqdm import tqdm

pattern = re.compile(r'([^.!?]*AA\s+\d+[^.!?]*[.!?])')

with open('/data/original_all.txt', 'r') as source_file:
    lines = source_file.readlines()

with tqdm(total=len(lines), desc="Processing") as pbar, \
     open('/data/AA_numl.txt', 'w') as output_file:
    for line in lines:
        matches = pattern.findall(line)
        for match in matches:
            output_file.write(match.strip() + '\n')
        pbar.update(1)
