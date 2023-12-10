import pandas as pd


1. def generate_car_matrix(df)->pd.DataFrame:
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    # Write your logic here #1
       def generate_car_matrix(dataset_path):
    df = pd.read_csv(dataset_path)

    # Pivot the DataFrame to create a matrix with id_1 as index, id_2 as columns, and car as values
    car_matrix = df.pivot(index='id_1', columns='id_2', values='car')
    car_matrix = car_matrix.fillna(0)

    for col in car_matrix.columns:
        car_matrix.at[col, col] = 0

    return car_matrix
dataset_path = '/content/dataset-1.csv'
result_matrix = generate_car_matrix(dataset_path)
print(result_matrix)
  

2. def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    # Write your logic here

def categorize_car_type(car): #2
    if car <= 15:
        return 'low'
    elif car <= 25:
        return 'medium'
    else:
        return 'high'

def get_type_count(df):
    # Add a new categorical column 'car_type' based on the custom function
    df['car_type'] = df['car'].apply(categorize_car_type)
    type_counts = df['car_type'].value_counts().to_dict()

    # Sort the dictionary alphabetically based on keys
    sorted_type_counts = dict(sorted(type_counts.items()))

    return sorted_type_counts


result = get_type_count(df)
print(result)

    


3. ##def get_bus_indexes(df)->list:
    """
   
    # Write your logic here #3
  
def get_bus_indexes(data_frame):  
    
    mean_bus = df['bus'].mean()
    bus_indices = df[df['bus'] > 2 * mean_bus].index.tolist()
    bus_indices.sort()

    return bus_indices
result = get_bus_indexes(df)
print(result)


    


4. #def filter_routes(df)->list:
    """
    def filter_routes(df):  #4
    filtered_df = df[df['truck'] > 7]

    if not filtered_df.empty:
        return sorted(filtered_df['route'].astype(int))
    else:
        return []
result = filter_routes(df)
print("Sorted list of routes:", result)


5. ##def multiply_matrix(matrix)->pd.DataFrame:
    def generate_car_matrix(dataset_path):
    df = pd.read_csv(dataset_path)
    car_matrix = df.pivot(index='id_1', columns='id_2', values='car')

    # Fill NaN values with 0
    car_matrix = car_matrix.fillna(0)

    for col in car_matrix.columns:
        car_matrix.at[col, col] = 0

    return car_matrix

def multiply_matrix(input_matrix):
    # Apply the specified logic to modify each value in the DataFrame
    modified_matrix = input_matrix.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)
    modified_matrix = modified_matrix.round(1)

    return modified_matrix

dataset_path = '/content/dataset-1.csv'
result_matrix = generate_car_matrix(dataset_path)

# Use the result_matrix as input to the multiply_matrix function
modified_result_matrix = multiply_matrix(result_matrix)
print(modified_result_matrix)


