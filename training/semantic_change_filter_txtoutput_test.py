from gensim.models import Word2Vec
import sys
import numpy as np
from gensim import matutils
import os
import csv

model_1989_2003 = Word2Vec.load("training/models/aligned_time_series_embeddings/aligned_1model_2003_1989")
model_2004_2009 = Word2Vec.load("training/models/aligned_time_series_embeddings/aligned_1model_2009_2004")
model_2010_2014 = Word2Vec.load("training/models/aligned_time_series_embeddings/aligned_1model_2014_2010")
model_2015_2018 = Word2Vec.load("training/models/aligned_time_series_embeddings/aligned_1model_2018_2015")
model_2019_2021 = Word2Vec.load("training/models/aligned_time_series_embeddings/aligned_1model_2021_2019")
model_2022_2023 = Word2Vec.load("training/models/aligned_time_series_embeddings/aligned_1model_2022_2023")


def read_keywords(file_paths):
    words_set = set()
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            for line in file:
                word = line.strip() 
                words_set.add(word)
    return list(words_set)

first_alloy_files = ['keywords/first_words/firstword_AA_family_all.txt',
                      'keywords/first_words/firstword_alloy.txt']
first_thermal_properties_file = ['keywords/first_words/firstword_thermal_properties.txt']
first_mechanical_properties_file = ['keywords/first_words/firstword_mechanical_properties.txt']
first_process_general_file = ['keywords/first_words/firstword_process_general.txt']
first_process_melt_ded_file = ['keywords/first_words/firstword_process_melt_ded.txt']
first_process_melt_general_file = ['keywords/first_words/firstword_process_melt_general.txt']
first_process_melt_pbf_file = ['keywords/first_words/firstword_process_melt_pbf.txt']
first_process_solid_binder_file = ['keywords/first_words/firstword_process_solid_binder.txt']
first_process_solid_cold_spray_file = ['keywords/first_words/firstword_process_solid_cold_spray.txt']
first_process_solid_extrusion_file = ['keywords/first_words/firstword_process_solid_extrusion.txt']
first_process_solid_field_assisted_file = ['keywords/first_words/firstword_process_solid_field_assisted.txt']
first_process_solid_friction_based_file = ['keywords/first_words/firstword_process_solid_friction_based.txt']
first_process_solid_general_file = ['keywords/first_words/firstword_process_solid_general.txt']

first_alloy_words = read_keywords(first_alloy_files)
first_thermal_properties_words = read_keywords(first_thermal_properties_file)
first_mechanical_properties_words = read_keywords(first_mechanical_properties_file)
first_process_general_words = read_keywords(first_process_general_file)
first_process_melt_ded_words = read_keywords(first_process_melt_ded_file)
first_process_melt_general_words = read_keywords(first_process_melt_general_file)
first_process_melt_pbf_words = read_keywords(first_process_melt_pbf_file)
first_process_solid_binder_words = read_keywords(first_process_solid_binder_file)
first_process_solid_cold_spray_words = read_keywords(first_process_solid_cold_spray_file)
first_process_solid_extrusion_words = read_keywords(first_process_solid_extrusion_file)
first_process_solid_field_assisted_words = read_keywords(first_process_solid_field_assisted_file)
first_process_solid_friction_based_words = read_keywords(first_process_solid_friction_based_file)
first_process_solid_general_words = read_keywords(first_process_solid_general_file)


other_alloy_files = ['keywords/other_words/similar_AA_family_all.txt',
                        'keywords/other_words/similar_alloy.txt']
other_thermal_properties_file = ['keywords/other_words/similar_thermal_properties.txt']
other_mechanical_properties_file = ['keywords/other_words/similar_mechanical_properties.txt']
other_process_general_file = ['keywords/other_words/similar_process_general.txt']
other_process_melt_ded_file = ['keywords/other_words/similar_process_melt_ded.txt']
other_process_melt_general_file = ['keywords/other_words/similar_process_melt_general.txt']
other_process_melt_pbf_file = ['keywords/other_words/similar_process_melt_pbf.txt']
other_process_solid_binder_file = ['keywords/other_words/similar_process_solid_binder.txt']
other_process_solid_cold_spray_file = ['keywords/other_words/similar_process_solid_cold_spray.txt']
other_process_solid_extrusion_file = ['keywords/other_words/similar_process_solid_extrusion.txt']
other_process_solid_field_assisted_file = ['keywords/other_words/similar_process_solid_field_assisted.txt']
other_process_solid_friction_based_file = ['keywords/other_words/similar_process_solid_friction_based.txt']
other_process_solid_general_file = ['keywords/other_words/similar_process_solid_general.txt']

other_alloy_words = read_keywords(other_alloy_files)
other_thermal_properties_words = read_keywords(other_thermal_properties_file)
other_mechanical_properties_words = read_keywords(other_mechanical_properties_file)
other_process_general_words = read_keywords(other_process_general_file)
other_process_melt_ded_words = read_keywords(other_process_melt_ded_file)
other_process_melt_general_words = read_keywords(other_process_melt_general_file)
other_process_melt_pbf_words = read_keywords(other_process_melt_pbf_file)
other_process_solid_binder_words = read_keywords(other_process_solid_binder_file)
other_process_solid_cold_spray_words = read_keywords(other_process_solid_cold_spray_file)
other_process_solid_extrusion_words = read_keywords(other_process_solid_extrusion_file)
other_process_solid_field_assisted_words = read_keywords(other_process_solid_field_assisted_file)
other_process_solid_friction_based_words = read_keywords(other_process_solid_friction_based_file)
other_process_solid_general_words = read_keywords(other_process_solid_general_file)


ELEMENTS = ["Li", "Be", "Na", "Mg", "Al", "K",
            "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga",
            "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb",
            "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
            "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po",
            "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es"]

ELEMENT_NAMES = ["Lithium", "Beryllium", "Sodium", "Magnesium", "Aluminium", "Potassium",
"Calcium", "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc", "Gallium",
"Rubidium", "Strontium", "Yttrium", "Zirconium", "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Indium", "Tin", "Antimony",
"Cesium", "Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium", "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium",
"Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium", "Osmium", "Iridium", "Platinum", "Gold", "Mercury", "Thallium", "Lead", "Bismuth", "Polonium",
"Radium", "Actinium", "Thorium", "Protactinium", "Uranium", "Neptunium", "Plutonium", "Americium", "Curium", "Berkelium", "Californium", "Einsteinium"]

def filter_words(top_context_words):
    metal = []
    thermal_property = []
    mechanical_property = []
    process_general = []
    process_melt_ded = []
    process_melt_general= []
    process_melt_pbf = []
    process_solid_binder = []
    process_solid_cold_spray = []
    process_solid_extrusion = []
    process_solid_field_assisted = []
    process_solid_friction_based = []
    process_solid_general = []
    unfiltered_item = []


    for item, similarity in top_context_words:
        # Find the item and its similarity in model_results
        similarity = next((sim for word, sim in top_context_words if word == item), None)
        #Below filter first words
        if any(element in item for element in ELEMENTS):
            metal.append((item, similarity))
        elif any(element in item for element in ELEMENT_NAMES):
            metal.append((item, similarity))
        # Step 3: Keep metal items that contain any word from alloy words (full match)
        elif item in first_alloy_words:
            metal.append((item, similarity))
        elif "alloy" in item:
            metal.append((item, similarity))
        elif "steel" in item:
            metal.append((item, similarity))
        elif any(word in item for word in first_process_general_words):
            process_general.append((item, similarity))
        elif any(word in item for word in first_process_melt_ded_words):
            process_melt_ded.append((item, similarity))
        elif any(word in item for word in first_process_melt_general_words):
            process_melt_general.append((item, similarity))
        elif any(word in item for word in first_process_melt_pbf_words):
            process_melt_pbf.append((item, similarity))
        elif item in first_process_solid_binder_words:
            process_solid_binder.append((item, similarity))
        elif any(word in item for word in first_process_solid_cold_spray_words):
            process_solid_cold_spray.append((item, similarity))
        elif any(word in item for word in first_process_solid_extrusion_words):
            process_solid_extrusion.append((item, similarity))
        elif any(word in item for word in first_process_solid_field_assisted_words):
            process_solid_field_assisted.append((item, similarity))
        elif any(word in item for word in first_process_solid_friction_based_words):
            process_solid_friction_based.append((item, similarity))
        elif any(word in item for word in first_process_solid_general_words):
            process_solid_general.append((item, similarity))
    
        # Step 5: Keep property items that contain properties keywords    
        elif item in first_thermal_properties_words:
            thermal_property.append((item, similarity))
        elif item in first_mechanical_properties_words:
            mechanical_property.append((item, similarity))

        #Below filter other words
        elif item in other_alloy_words:
            metal.append((item, similarity))
        elif item in other_process_general_words:
            process_general.append((item, similarity))
        elif item in other_process_melt_ded_words:
            process_melt_ded.append((item, similarity))
        elif item in other_process_melt_general_words:
            process_melt_general.append((item, similarity))
        elif  item in other_process_melt_pbf_words:
            process_melt_pbf.append((item, similarity))
        elif  item in other_process_solid_cold_spray_words:
            process_solid_cold_spray.append((item, similarity))
        elif  item in other_process_solid_extrusion_words:
            process_solid_extrusion.append((item, similarity))
        elif item in other_process_solid_field_assisted_words:
            process_solid_field_assisted.append((item, similarity))
        elif  item in other_process_solid_friction_based_words:
            process_solid_friction_based.append((item, similarity))
        elif item in other_process_solid_general_words:
            process_solid_general.append((item, similarity))
        elif item in other_mechanical_properties_words:
            mechanical_property.append((item, similarity))
        elif item in other_thermal_properties_words:
            thermal_property.append((item, similarity))          
        # Step 7: unfiltered items
        else:
            unfiltered_item.append((item, similarity))
    
    return {
        'metal': metal,
        'thermal_property': thermal_property,
        'mechanical_property': mechanical_property,
        'process_general': process_general,
        'process_melt_ded': process_melt_ded,
        'process_melt_general': process_melt_general,
        'process_melt_pbf': process_melt_pbf,
        'process_solid_binder': process_solid_binder,
        'process_solid_cold_spray': process_solid_cold_spray,
        'process_solid_extrusion': process_solid_extrusion,
        'process_solid_field_assisted': process_solid_field_assisted,
        'process_solid_friction_based': process_solid_friction_based,
        'process_solid_general': process_solid_general,
        'unfiltered_item': unfiltered_item
    }


models = [model_1989_2003, model_2004_2009, model_2010_2014, model_2015_2018, model_2019_2021, model_2022_2023]
time_periods = ['1989-2003','2004-2009','2010-2014','2015-2018','2019-2021','2022-2023']
keywords = ['high_entropY_alloys', 'multi-principal_element_alloy',
            'multi-component_alloy', 'complex_concentrated_alloy',
            'compositionally_complex_alloy']
output_dir = 'visualization'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

metal_distance_over_time = {}
for model, time in zip(models, time_periods):
    existing_keywords = [word for word in keywords if word in model.wv]
    if not existing_keywords:
        metal_distance_over_time[time] = [('N/A', 0)]
        continue

    try:
        top_context_words = model.wv.most_similar(positive=existing_keywords, topn=5000)
        categorized_words = filter_words(top_context_words)
        
        if 'metal' in categorized_words:
            metal_words = categorized_words['metal']
            metal_distance = [(word, 1 - similarity) for word, similarity in metal_words]
        else:
            metal_distance = [('N/A', 0)]
        
        metal_distance_over_time[time] = metal_distance
        
    except KeyError:
        metal_distance_over_time[time] = [('N/A', 0)]


key_word_str = "_and_".join(keywords)
file_name = os.path.join(output_dir, f"{key_word_str}_metal.csv") 

with open(file_name, 'w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    csv_writer.writerow(["Year Period", "Material Name", "Distance"])
    for time, properties in metal_distance_over_time.items():
        for word, distance in properties[:500]:
            csv_writer.writerow([time, word, distance])