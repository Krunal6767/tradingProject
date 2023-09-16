import pandas as pd

def save_data_to_csv(data, output_file):
    try:
        # Save the data to a CSV file
        data.to_csv(output_file, index=False)
        print(f"Data saved to {output_file}")

    except Exception as e:
        print(f"Error saving data: {e}")

def load_data_from_csv(input_file):
    try:
        # Load data from a CSV file
        data = pd.read_csv(input_file)
        return data

    except Exception as e:
        print(f"Error loading data: {e}")
        return None

if __name__ == "__main__":
    # Example usage:
    # Save data to a CSV file
    data_to_save = pd.DataFrame({'Date': ['2023-01-01', '2023-01-02'],
                                 'Close': [100.0, 101.0]})
    save_data_to_csv(data_to_save, 'data/sample_data.csv')

    # Load data from a CSV file
    loaded_data = load_data_from_csv('data/sample_data.csv')
    if loaded_data is not None:
        print("Loaded data:")
        print(loaded_data)
