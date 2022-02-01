from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt
import math
import csv
from numpy.core.fromnumeric import size, sort, take
from numpy.lib.function_base import append
from numpy.lib.npyio import loadtxt
from numpy.typing import _128Bit

class data_import():
    def __init__(self):
        self.country_array = np.genfromtxt('Country_data.csv', delimiter=',', dtype=str, skip_header=True)
        self.pop_array = np.genfromtxt('Population_data.csv', delimiter=',', dtype=str, skip_header=True)
        self.species_array = np.genfromtxt('Threatened_Species.csv', delimiter=',', dtype=str, skip_header=True)
        
        self.region_list = np.unique(self.country_array[0:-1, 1])  #Creates an array of each unique value in the 'UN Region' column in Country_data.csv
        self.sub_region_list = []
        self.regional_species = []
        self.country_list = []
        for i in range(0, 194):
            self.country_list.append(self.pop_array[i][0])

class population_data():

    def __init__(self, country, mean_pop_change, change_in_pop_list, pop_per_sq_km):
        self.country = country
        self.mean_pop_change = mean_pop_change
        self.change_in_pop_list = change_in_pop_list
        self.pop_per_sq_km = pop_per_sq_km
    
    def print_stats(self):
        print("The mean population change each year in the country {0} from 2000-2020 was {1} people".format(self.country, self.mean_pop_change))
        if abs(min(self.change_in_pop_list)) > abs(max(self.change_in_pop_list)):
            print('The most the population changed in one year was a decrease of {}'.format(abs(min(self.change_in_pop_list))))
        elif abs(min(self.change_in_pop_list)) == abs(max(self.change_in_pop_list)):
            print('The most the population changed in one year was an increase/decrease of {}'.format(abs(min(self.change_in_pop_list))))
        else:
            print('The most the population changed in one year was an increase of {}'.format(abs(max(self.change_in_pop_list))))

    def create_and_print_plots(self):
        xlabels = ['00-01', '01-02', '02-03', '03-04', '04-05', '05-06', '06-07', 
                    '07-08', '08-09', '09-10', '10-11', '11-12', '12-13', '13-14', 
                    '14-15', '15-16', '16-17', '17-18', '18-19', '19-20']
        plt.subplot(2, 1, 1)
        plt.bar(xlabels, self.change_in_pop_list, color = 'g')
        plt.xticks(rotation = 45, fontsize = 6)
        plt.xlabel('Year')
        plt.ylabel('Population Change')
        plt.grid()
        plt.subplot(2, 1, 2)
        plt.plot((range(0, 21)), self.pop_per_sq_km, 'g.')
        plt.xticks(ticks = (range(0, 21)), labels = list(range(2000, 2021)), rotation = 45, fontsize = 6)
        plt.xlabel('Year')
        plt.ylabel('Population Per Square Km')
        plt.grid()
        plt.tight_layout()
        plt.show()

class data_manipulation():

    def __init__(self):
        self.init = ''
        
    def species_by_region(self):
        data_reader = data_import()
        
        user_region = ''
        user_region = take_region_input(data_reader.region_list, user_region)
        temp = np.where(data_reader.country_array[0:-1, 1] == user_region) #Creates an array that represents the index of each country within a region inside the main array
        region_countries = data_reader.country_array[temp]                  #Creates a new array that assigns the index values of the main array to this one
        region_index = region_countries[0:-1, 0]                            #Creates a one dimensional array that functions as the index for all available regions
        
        
        sub_regions = np.where(data_reader.country_array[:, 1] ==  user_region)
        
        sub_regions_in_region = data_reader.country_array[sub_regions]

        print('Your available sub-regions are {}'.format(np.unique(sub_regions_in_region[:, 2])))
        user_sub_region = take_sub_region_input(sub_regions_in_region)
        temp = np.where(data_reader.country_array[0:-1, 2] == user_sub_region) #Creates an array that represents the index of each country within a region inside the main array
        sub_region_countries = data_reader.country_array[temp]                  #Creates a new array that assigns the index values of the main array to this one
        sub_region_index = sub_region_countries[:, 0]
        
        

        regional_species = []
        for i in data_reader.species_array[:]:
            if i[0] in region_index:
                regional_species.append(i[1:5])

        sub_regional_species = []
        for i in data_reader.species_array[:]:
            if i[0] in sub_region_index:
                sub_regional_species.append(i[1:5])

        
        regional_species = np.array(regional_species).astype(np.int32)
        sub_regional_species = np.array(sub_regional_species).astype(np.int32)  #converts the regional species array into integer data type
        

        species_sum = np.sum(regional_species, axis=1, keepdims=True) #creates an 1 dimensional array that is the sum of each column along each row
        critically_endangered = np.max(species_sum)
        indexed_country = region_index[np.where(critically_endangered == critically_endangered)]
        indexed_country = str(indexed_country[0])
        
        
        total_species_sub_region_countries = np.sum(sub_regional_species, axis=1, keepdims=True)
        

        
        
        print("Within the {} region, the country with the highest amount of endangered species is '{}', with {} endangered species" .format(user_region, indexed_country, critically_endangered))

        ####Plotting Block
        y_data = []
        x_data = ['Plants', 'Fish', 'Birds', 'Mammals']
        colors = ['g', 'b', 'r', 'c', 'm']
        while len(y_data) != 4:
            y_data.append(np.mean(regional_species[ 0:-1, len(y_data)]))
        plt.bar(x_data, y_data, color=colors)
        plt.xticks(x_data)
        plot_title = 'Average Number of Endangered Species of {} region'.format(user_region)
        plt.title(plot_title)
        plt.xlabel('Organism Type')
        plt.ylabel('Average # of Endangered Species')
        plt.show()


        x_data = np.ndarray.tolist(sub_region_index)
        y_data = np.ndarray.tolist(total_species_sub_region_countries[:, 0])
        data_dict = {y_data[i]:x_data[i] for i in range(len(x_data))}
        data_dict = sorted(data_dict.items())
        x_data = [i[1] for i in data_dict]
        y_data = [i[0] for i in data_dict]
        
        plt.figure(figsize=(12,5))
        plt.bar(x_data, y_data, color='b')
        plt.xticks(rotation=90, size=8)
        plt.xlabel('Countries within sub-region')
        plt.ylabel('Number of endangered species')
        plt.title('Endangered species within the {} sub-region'.format(user_sub_region))
        plt.autoscale()
        plt.tight_layout()
        plt.show()
        ###End of Plotting Block
        

def take_user_input():
    user_input = input("1. Population Growth of a country\n2. Threatened species data\n Please Select 1 or 2: ")
    while user_input not in ['1', '2']:
        print('Input is invalid.')
        user_input = input("1. Population Growth of a country\n2. Threatened species data\n Please Select 1 or 2: ")    
    return user_input

def take_second_input(country_list):
    second_user_input = input('Please select a country from the list: ')    
    while second_user_input not in country_list:
        print('Input is invalid.')
        second_user_input = input('Please select a country from the list: ')
    return second_user_input    

def take_region_input(region_list, region_user_input):
    print('Your available regions are {}'.format(region_list))
    region_user_input = input("Please enter a region from the list above: ")
    if region_user_input not in region_list:
        print('Input is invalid')
        region_user_input = take_region_input(region_list, region_user_input)
    return region_user_input

def take_sub_region_input(sub_region_list):
    user_input = input("Please enter a sub-region from the list above: ")
    if user_input not in sub_region_list:
        print('Input is invalid')
        user_input = take_sub_region_input(sub_region_list)
    return user_input

def main():
    

    menu_selection = take_user_input()
    
    if menu_selection == '1':
        import_data = data_import()

        print('Your available countries are:\n{}'.format(import_data.country_list))
        second_user_input = take_second_input(import_data.country_list)
    
        pop_list = []
        for i in range(1, 22):
            pop_list.append(import_data.pop_array[import_data.country_list.index(second_user_input)][i])

        change_in_pop_list = []  
        for i in range(0, 20):
            change_in_pop_list.append(int(pop_list[i+1])-int(pop_list[i]))
            
        sq_km = import_data.country_array[import_data.country_list.index(second_user_input)][3]

        pop_per_sq_km = []
        for i in range(0, 21):
            pop_per_sq_km.append(int(pop_list[i]) / int(sq_km))

        _population_data = population_data(second_user_input, int(np.mean(change_in_pop_list)), change_in_pop_list, pop_per_sq_km)
        _population_data.print_stats()
        _population_data.create_and_print_plots()
    
    elif menu_selection == '2':
        data_math2 = data_manipulation()
        data_math2.species_by_region()


#Runs program
if __name__ == '__main__':
    main()
