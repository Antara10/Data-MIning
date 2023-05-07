
transactions = [
    
    # Year, State, Quater, Visitors
    (2018, 'State A', 'Q1', 1000),
    (2018, 'State A', 'Q2', 1200),
    (2018, 'State A', 'Q3', 1500),
    (2018, 'State A', 'Q4', 1100),
    (2018, 'State B', 'Q1', 800),
    (2018, 'State B', 'Q2', 900),
    (2018, 'State B', 'Q3', 1000),
    (2018, 'State B', 'Q4', 950),
    (2018, 'State C', 'Q1', 700),
    (2018, 'State C', 'Q2', 850),
    (2018, 'State C', 'Q3', 900),
    (2018, 'State C', 'Q4', 1000),
    (2019, 'State A', 'Q1', 1100),
    (2019, 'State A', 'Q2', 1300),
    (2019, 'State A', 'Q3', 1600),
    (2019, 'State A', 'Q4', 1200),
    (2019, 'State B', 'Q1', 900),
    (2019, 'State B', 'Q2', 1000),
    (2019, 'State B', 'Q3', 1100),
    (2019, 'State B', 'Q4', 1050),
    (2019, 'State C', 'Q1', 750),
    (2019, 'State C', 'Q2', 900),
    (2019, 'State C', 'Q3', 950),
    (2019, 'State C', 'Q4', 1050),
    (2020, 'State A', 'Q1', 900),
    (2020, 'State A', 'Q2', 1100),
    (2020, 'State A', 'Q3', 1400),
    (2020, 'State A', 'Q4', 1000),
    (2020, 'State B', 'Q1', 850),
    (2020, 'State B', 'Q2', 950),
    (2020, 'State B', 'Q3', 1000),
    (2020, 'State B', 'Q4', 950),
    (2020, 'State C', 'Q1', 800),
    (2020, 'State C', 'Q2', 950),
    (2020, 'State C', 'Q3', 1000),
    (2020, 'State C', 'Q4', 1100),
    (2021, 'State A', 'Q1', 1000),
    (2021, 'State A', 'Q2', 1200),
    (2021, 'State A', 'Q3', 1500),
    (2021, 'State A', 'Q4', 1100),
    (2021, 'State B', 'Q1', 800),
    (2021, 'State B', 'Q2', 900),
    (2021, 'State B', 'Q3', 1000),
    (2021, 'State B', 'Q4', 950),
    (2021, 'State C', 'Q1', 700),
    (2021, 'State C', 'Q2', 850),
    (2021, 'State C', 'Q3', 900),
    (2021, 'State C', 'Q4', 1000),
    (2022, 'State A', 'Q1', 1100),
    (2022, 'State A', 'Q2', 1300),
    (2022, 'State A', 'Q3', 1600),
    (2022, 'State A', 'Q4', 1200),
    (2022, 'State B', 'Q1', 900),
    (2022, 'State B', 'Q2', 1000),
    (2022, 'State B', 'Q3', 1100),
    (2022, 'State B', 'Q4', 1050),
    (2022, 'State C', 'Q1', 750),
    (2022, 'State C', 'Q2', 900),
    (2022, 'State C', 'Q3', 950),
    (2022, 'State C', 'Q4', 1050),
    (2023, 'State A', 'Q1', 900),
    (2023, 'State A', 'Q2', 1100),
    (2023, 'State A', 'Q3', 1400),
    (2023, 'State A', 'Q4', 1000),
    (2023, 'State B', 'Q1', 850),
    (2023, 'State B', 'Q2', 950),
    (2023, 'State B', 'Q3', 1000),
    (2023, 'State B', 'Q4', 950),
    (2023, 'State C', 'Q1', 800),
    (2023, 'State C', 'Q2', 950),
    (2023, 'State C', 'Q3', 1000),
    (2023, 'State C', 'Q4', 1100)
    
    ]

# Create the datacube

def create_data_cube(data):
    data_cube = {}
    for entry in data:
        year,state,quater,visitors = entry
        
        if year not in data_cube:
            data_cube[year]={}
            
        if state not in data_cube[year]:
            data_cube[year][state]={}
            
        if quater not in data_cube[year][state]:
            data_cube[year][state][quater]=visitors
    return data_cube

# Save the data_cube
def save_data_cube(data_cube, filename):
    with open(filename, 'w') as file:
        file.write(str(data_cube))
        
data_cube = create_data_cube(transactions)

save_data_cube(data_cube, r"C:\Users\bipro\OneDrive\Documents\Data Mining\practical\practical\bipro.txt")

        
def slice_operation(data_cube, year, state, quater):
    sliced_cube = {}
    if year in data_cube:
        sliced_cube[year]={}
        if state in data_cube[year]:
            sliced_cube[year][state]={}
            if quater in data_cube[year][state]:
                
                sliced_cube[year][state][quater] = data_cube[year][state][quater]
        
            
    return sliced_cube

def load_data_cube(filename):
    
    with open(filename,'r') as file:
        data_cube = eval(file.read())
    return data_cube

Data_cube = load_data_cube(r"C:\Users\bipro\OneDrive\Documents\Data Mining\practical\practical\bipro.txt")

# Perform the slice operation based on user input
input_year = 2018
input_state = 'State A'
input_quater = 'Q1'

sliced_datacube = slice_operation(Data_cube, input_year, input_state, input_quater)
print("Sliced Cube: ",sliced_datacube)

def dice_operation(data_cube, year_range, state_list, quater_list):
    diced_cube = {}
    
    for year in year_range:
        if year in data_cube:
            diced_cube[year] = {}
            for state in state_list:
                if state in data_cube[year]:
                    diced_cube[year][state]={}
                    for quater in quater_list:
                        if quater in data_cube[year][state]:
                            diced_cube[year][state][quater]=data_cube[year][state][quater]
    return diced_cube

# Take the user input
input_year_range = 2018,2020
input_state_list = 'State A', 'State B'
input_quater_list = 'Q1', 'Q3'

diced_cube = dice_operation(data_cube, input_year_range, input_state_list, input_quater_list)

if diced_cube:
    print("DICE Result:")
    print(diced_cube)
else:
    print("No data found for the specified dimensions.")
