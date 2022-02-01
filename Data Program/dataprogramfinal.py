# school_data.py
# Nicola Savino, ENDG 233 F21
# A terminal-based application to process and plot data based on given user input and provided csv files.
# You may only import numpy, matplotlib, and math. 
# No other modules may be imported. Only built-in functions that support compound data structures, user entry, or casting may be used.
# Remember to include docstrings for any functions/classes, and comments throughout your code.

from os import name
import numpy as np
import matplotlib.pyplot as plt

# The following class is provided and should not be modified.
class School:
    """A class used to create a School object.

        Attributes:l;4
            name (str): String that represents the school's name
            code (int): Integer that represents the school's code
    """

    def __init__(self, name, code):
        self.name = name 
        self.code = code

    def print_all_stats(self):
        """A function that prints the name and code of the school instance.

        Parameters: None
        Return: None

        """
        print("School Name: {0}, School Code: {1}".format(self.name, self.code))


# Import data here
# Hint: Create a dictionary for all school names and codes
# Hint: Create a list of school codes to help with index look-up in arrays

#This dictionary stores school names and codes for user input
school_dict = {         '1224':	'Centennial High School',
                        '1679':	'Robert Thirsk School',
                        '9626':	'Louise Dean School',
                        '9806':	'Queen Elizabeth High School',
                        '9813':	'Forest Lawn High School',
                        '9815':	'Crescent Heights High School',
                        '9816':	'Western Canada High School',
                        '9823':	'Central Memorial High School',
                        '9825':	'James Fowler High School',
                        '9826':	'Ernest Manning High School',
                        '9829':	'William Aberhart High School',
                        '9830':	'National Sport School',
                        '9836':	'Henry Wise Wood High School',
                        '9847':	'Bowness High School',
                        '9850':	'Lord Beaverbrook High School',
                        '9856':	'Jack James High School',
                        '9857':	'Sir Winston Churchill High School',
                        '9858':	'Dr. E. P. Scarlett High School',
                        '9860':	'John G Diefenbaker High School',
                        '9865':	'Lester B. Pearson High School',
                     }

#creates list of keysfrom the previous dictionary for quick indexing
id_list = list(school_dict.keys())

#generates three distinct arrays from the provided CSV files, skipping the header of each column
sdt_2018 = np.genfromtxt('SchoolData_2018-2019.csv', delimiter = ',', skip_header = True)
sdt_2019 = np.genfromtxt('SchoolData_2019-2020.csv', delimiter = ',', skip_header = True)
sdt_2020 = np.genfromtxt('SchoolData_2020-2021.csv', delimiter = ',', skip_header = True)

#merged_array is the sum of the last 3 columns of the imported CSV files
merged_array = np.array((sdt_2018[:,[1,2,3]] + sdt_2019[:,[1,2,3]] + sdt_2020[:,[1,2,3]]))

# Add your code within the main function. A docstring is not required for this function.
def main():
    print("ENDG 233 School Enrollment Statistics\n")

    # Print array data here
    print('Array Data for 2018-2019:\n', sdt_2018)
    print('Array Data for 2019-2020:\n', sdt_2019)
    print('Array Data for 2020-2021:\n', sdt_2020)
    print('Mean of sum of last 3 columns of each array:\n', merged_array)
    # Add request for user input here
     
    def get_key(val):
        '''This Function gets the key of the school_dict dictionary

            Parameters: val -- This parameter is used to check if user input is equal to a value within the dictionary
            Returns: key -- This return value is the key of the dictionary
        '''
        for key, value in school_dict.items():
            if val == value:
                return key

    def take_user_input():
        ''' This function is called at the beggining of the program to check user input and test for validity
            and also assigns values to the attributes of the school_id object being instantiated

            Parameters: None
            Returns: school_id -- Object from School class that contains value for the user inputeed school name or code
        '''
        user_input = input("Please Enter School Name or ID: ")
        
        #This else-if block checks for 2 cases, one where user input is a key in the dictionary, and one where it is a value
        #if user input is a key(code) then the school id is user input and the name is the value of that key
        #if user input is a value(name) then the school name is user input and the code is the key of that value
        #if user input is not found within the dictionary, input is invalid and the function is called again recursively
        if user_input in school_dict.keys():
            school_id.code = user_input
            school_id.name = school_dict[(user_input)]
        elif user_input in school_dict.values():
            school_id.name = user_input
            school_id.code = get_key(user_input)
        else:
            print("You must enter a valid school name or code.")
            take_user_input()
        return school_id

    #instantiates a School object, assigning name and code as it's attributes
    school_id = School(name, code = 0)
    take_user_input()

    print("\n***Requested School Statistics***\n")

    # Print school name and code using the given class
    school_id.print_all_stats()
    # Add data processing and plotting here
    


    #row index is the index of the value in the id_list list that matches the school_id code attribute
    row_index = int(id_list.index(school_id.code))
 
    #the following block creates a mean enrollment value for each grade and a total enrollment value for the given school and prints those values
    g10_mean = int((merged_array[row_index][0]) // 3)
    g11_mean = int((merged_array[row_index][1]) // 3)
    g12_mean = int((merged_array[row_index][2]) // 3)
    total_enrollment = int(merged_array[row_index][2])
    print('Mean enrollment for Grade 10: {}\n''Mean enrollment for Grade 11: {}\n''Mean enrollment for Grade 12: {}\n'.format(g10_mean, g11_mean, g12_mean))
    print('Total number of students who graduated in the past three years: {}'.format(total_enrollment))

    #this list is created to set the x-axis of the plots
    grades = [10,11,12]
    #plots grade enrollment by year for each grade
    plt1 = plt.plot(grades, [sdt_2018[row_index][1], sdt_2018[row_index][2], sdt_2018[row_index][3]], 'ro', label = '2019 enrollment')
    plt.plot(grades, [sdt_2019[row_index][1], sdt_2019[row_index][2], sdt_2019[row_index][3]], 'go', label = '2020 enrollment')
    plt.plot(grades, [sdt_2020[row_index][1], sdt_2020[row_index][2], sdt_2020[row_index][3]], 'bo', label = '2021 enrollment')
    plt.title('Grade Enrollment by Year')
    plt.ylabel('Enrollment')
    plt.xlabel('Grade')
    plt.xticks(grades)
    plt.legend(loc = 'upper left')
    plt.show()

    #This list is created set to the x-axis
    #the following 3 blocks plots yearly enrollment by grade, using 3 different subplots for each grade
    years = [2019, 2020, 2021]
    plt.title('Enrollment by Grade')
    plt.subplot(3, 1, 1)
    plt.plot(years, [sdt_2018[row_index][1], sdt_2019[row_index][1], sdt_2020[row_index][1]], 'y--', label = 'Grade 10')
    plt.xticks(years)
    plt.legend(loc = 'upper right')
    
    plt.subplot(3, 1, 2)
    plt.plot(years, [sdt_2018[row_index][2], sdt_2019[row_index][2], sdt_2020[row_index][2]], 'm--', label = 'Grade 10')
    plt.xticks(years)
    plt.legend(loc = 'upper right')

    plt.subplot(3, 1, 3)
    plt.plot(years, [sdt_2018[row_index][3], sdt_2019[row_index][3], sdt_2020[row_index][3]], 'c--', label = 'Grade 10')
    plt.xticks(years)
    plt.legend(loc = 'upper right')

    plt.show()
# Do not modify the code below
if __name__ == '__main__':
    main()

