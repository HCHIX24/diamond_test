import pandas as pd

# Path to the diamond data CSV
file_path = 'diamonds.csv'

def print_menu():
    """Print the menu options for the user."""
    print("\nMenu:")
    print("1. Display available columns")
    print("2. Find the most expensive diamond")
    print("3. Calculate average price of diamonds")
    print("4. Count diamonds with 'Ideal' cut")
    print("5. Count unique colors and list color options")
    print("6. Calculate median carat of diamonds with 'Premium' cut")
    print("7. Calculate mean carat for each type of cut")
    print("8. Calculate mean price for each color")
    print("0. Exit")

def load_diamond_data(filename):
    """Load the diamond CSV data into a pandas DataFrame."""
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return pd.DataFrame()

def biggest_price(df, column_name):
    """Find the row with the most expensive diamond in the DataFrame."""
    max_price = df[column_name].max()
    return df[df[column_name] == max_price]

def average_price(df, column_name):
    """Calculate the average price of diamonds in the DataFrame."""
    return df[column_name].mean()

def count_ideal_cuts(df, cut_column_name):
    """Count how many diamonds have the 'Ideal' cut."""
    return df[cut_column_name].value_counts().get('Ideal', 0)

def count_premium_cuts(df, cut_column_name):
    """Count how many diamonds have the 'Premium' cut."""
    return df[cut_column_name].value_counts().get('Premium', 0)

def count_colors(df, color_column_name):
    """Count how many unique colors there are and list the color options."""
    return df[color_column_name].nunique(), df[color_column_name].unique()

def median_carat(df, cut_type):
    """Calculate the median carat of diamonds with the specified cut type."""
    filtered_df = df[df['cut'] == cut_type]
    return filtered_df['carat'].median()

def mean_carat_by_cut(df, cut_column_name):
    """Calculate the mean carat for each type of cut."""
    return df.groupby(cut_column_name)['carat'].mean()

def mean_price_by_color(df, color_column_name):
    """Calculate the mean price for each color type."""
    return df.groupby(color_column_name)['price'].mean()

def display_columns(df):
    """Display available columns in the DataFrame."""
    return df.columns.tolist()

def main():
    diamond_data = load_diamond_data(file_path)
    
    if diamond_data.empty:
        return
    
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print("\nColumns in diamond dataset:", display_columns(diamond_data))
        
        elif choice == '2':
            most_expensive = biggest_price(diamond_data, 'price')
            print("\nMost expensive diamond:")
            print(most_expensive)
        
        elif choice == '3':
            avg_price = average_price(diamond_data, 'price')
            print(f"Average price: {avg_price:.2f}")
        
        elif choice == '4':
            ideal_count = count_ideal_cuts(diamond_data, 'cut')
            print(f"Number of diamonds with 'Ideal' cut: {ideal_count}")
        
        elif choice == '5':
            num_colors, color_options = count_colors(diamond_data, 'color')
            print(f"\nNumber of unique colors: {num_colors}")
            print("Color options:", color_options)
        
        elif choice == '6':
            median_premium_carat = median_carat(diamond_data, 'Premium')
            print(f"Median carat for 'Premium' cut: {median_premium_carat:.2f}")
        
        elif choice == '7':
            mean_carat_by_cut_result = mean_carat_by_cut(diamond_data, 'cut')
            print("\nMean carat by cut type:")
            print(mean_carat_by_cut_result)
        
        elif choice == '8':
            mean_price_by_color_result = mean_price_by_color(diamond_data, 'color')
            print("\nMean price by color:")
            print(mean_price_by_color_result)
        
        elif choice == '0':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
