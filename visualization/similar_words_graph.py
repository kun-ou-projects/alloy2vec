import matplotlib.pyplot as plt
import pandas as pd

file_path = 'visualization/updated_gas_pipeline (1).xlsx' 
df = pd.read_excel(file_path)

default_color = '#5EC286'

country_column_exists = 'Country' in df.columns

if country_column_exists:
    country_colors = {
        'US': '#1f77b4', 
        'Germany': '#ff7f0e', 
        'Japan': '#2ca02c', 
        'China': '#FF0000', 
        'UK': '#9467bd',  
        'Russia/USSR': '#001B57',  
        'US and Europe': '#A67D3D', 
        'Europe': '#bcbd22',  
        'MPEA': '#FF1CAE',  
        'non-MPEA' : '#1f77b4' 
    }
else:
    country_colors = {}

appeared_countries = set()

x_values, y_values, labels, label_positions, point_colors = [], [], [], [], []

for i, period in enumerate(df['Year Period'].unique()):
    period_data = df[df['Year Period'] == period]

    for _, row in period_data.iterrows():
        if row['Materials'] == 'N/A':
            continue
        x_values.append(i)
        y_values.append(row['Distance'])
        labels.append(row['Materials'])
        if country_column_exists:
            appeared_countries.add(row['Country'])
            point_colors.append(country_colors.get(row['Country'], default_color)) 
        else:
            point_colors.append(default_color)
        label_positions.append(row.get('label_position', 'right'))

plt.figure(figsize=(18, 10))
for x, y, label, position, color in zip(x_values, y_values, labels, label_positions, point_colors):
    ha = 'center'  
    va = 'center'  
    if position == 'bottom':
        va = 'top'
        y -= 0.002 
    elif position == 'top':
        va = 'bottom'
        y += 0.002  
    elif position == 'left':
        ha = 'right'
    elif position == 'right':
        ha = 'left'
    
    plt.scatter(x, y, color=color)
    plt.text(x, y, label, fontsize=16, ha=ha, va=va)


plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.xticks(range(len(df['Year Period'].unique().tolist())), df['Year Period'].unique().tolist()) #rotation=45
plt.xlim(-1, len(df['Year Period'].unique().tolist()))
plt.xlabel('Year', fontsize=20)
plt.ylabel('Cosine Distance', fontsize=20)
plt.ylim(0.465,0.635)

if country_column_exists:
    legend_handles = [plt.Line2D([0], [0], marker='o', color='w', label=country, 
                                 markersize=14, markerfacecolor=color) for country, color in country_colors.items() if country in appeared_countries]
    plt.legend(handles=legend_handles, loc='lower right', bbox_to_anchor=(1, 0.1), fontsize=18)
else:
    plt.scatter([], [], color=default_color, label='Default')
    plt.legend(title='Color Legend', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=16)

plt.tick_params(axis='x', labelsize=20)  
plt.tick_params(axis='y', labelsize=20)  

plt.tight_layout()
plt.show()
