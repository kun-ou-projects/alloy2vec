import matplotlib.pyplot as plt
import re
from collections import defaultdict

time_periods = ['89-03', '04-09', '10-14', '15-18', '19-21', '22-23']
files = {
    '89-03': 'co_occurrence/extracted_2003_1989.txt',
    '04-09': 'co_occurrence/extracted_2009_2004.txt',
    '10-14': 'co_occurrence/extracted_2014_2010.txt',
    '15-18': 'co_occurrence/extracted_2018_2015.txt',
    '19-21': 'co_occurrence/extracted_2021_2019.txt',
    '22-23': 'co_occurrence/extracted_2022_2023.txt'
}

keywords = {
    'complex concentrated alloy': re.compile('complex-?\s*concentrated\s+alloy', re.IGNORECASE),
    'compositionally complex alloy': re.compile('compositionally-?\s*complex\s+alloy', re.IGNORECASE),
    'high entropy alloy': re.compile('high entropy alloy', re.IGNORECASE),
    'multi-component alloy': re.compile('multi-?\s*component\s+alloy', re.IGNORECASE),
    'multi-principal element alloy': re.compile('multi-?\s*principal\s+element\s+alloy', re.IGNORECASE),
}


counts = defaultdict(lambda: defaultdict(int))
total_lines_with_keywords = defaultdict(int)

for period, file_path in files.items():
    with open(file_path, 'r') as file:
        for line in file:
            found_keyword = False
            for keyword, pattern in keywords.items():
                if pattern.search(line):
                    counts[period][keyword] += 1
                    found_keyword = True
            if found_keyword:
                total_lines_with_keywords[period] += 1

relative_frequencies = defaultdict(lambda: defaultdict(float))
for period in time_periods:
    for keyword in keywords:
        if total_lines_with_keywords[period] > 0:
            relative_frequencies[period][keyword] = counts[period][keyword] / total_lines_with_keywords[period]

plt.figure(figsize=(10, 10))
colors = ['blue', 'green', 'red', 'cyan', 'magenta'] 
for i, (keyword, color) in enumerate(zip(keywords, colors)):
    frequencies = [relative_frequencies[period][keyword] for period in time_periods]
    plt.plot(time_periods, frequencies, label=keyword, color=color)  

plt.xlabel('Year', fontsize=20)
plt.ylabel('Relative Frequency', fontsize=20)
# plt.title('Relative Frequency of Keywords over Time', fontsize=14)
plt.legend(fontsize=18)
plt.tick_params(axis='x', labelsize=20)  
plt.tick_params(axis='y', labelsize=20) 
plt.tight_layout()
plt.show()