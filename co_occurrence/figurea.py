import re
import matplotlib.pyplot as plt

def count_articles_and_calculate_ratio(file_path, patterns):
    total_lines = 0
    matching_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            total_lines += 1
            columns = line.split(',') 
            if any(re.search(pattern, column, re.IGNORECASE) for column in columns for pattern in patterns):
                matching_count += 1
    ratio = matching_count / (total_lines - 1) if total_lines > 1 else 0
    return ratio


patterns = [
    'complex-?\s*concentrated\s+alloy',
    'compositionally-?\s*complex\s+alloy',
    'high entropy alloy',
    'multi-?\s*component\s+alloy',
    'multi-?\s*principal\s+element\s+alloy'
]

periods_files = {
    '89-03': 'co_occurrence/extracted_2003_1989.txt',
    '04-09': 'co_occurrence/extracted_2009_2004.txt',
    '10-14': 'co_occurrence/extracted_2014_2010.txt',
    '15-18': 'co_occurrence/extracted_2018_2015.txt',
    '19-21': 'co_occurrence/extracted_2021_2019.txt',
    '22-23': 'co_occurrence/extracted_2022_2023.txt'
}

ratios = [count_articles_and_calculate_ratio(file_path, patterns) for file_path in periods_files.values()]

plt.figure(figsize=(10, 10))
plt.bar(periods_files.keys(), ratios, color='#5EC286')
plt.xlabel('Year', fontsize=20)
plt.ylabel('Ratio of Articles', fontsize=20)
plt.tick_params(axis='x', labelsize=20) 
plt.tick_params(axis='y', labelsize=20) 
# plt.title('Ratio of Articles by Year', fontsize=14)
# plt.xticks(rotation=45)
plt.show()