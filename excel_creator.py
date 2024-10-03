import pandas as pd

# Dataframe: Basic info with the pieces names, it will allow to develop the excel
def create_dataframe():
    furniture = []
    while True:
        name = input("Enter furniture name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        try:
            size = float(input("Enter size in centimeters: "))
            furniture.append({"Muebles:": name, "Centimeters": size}) 
        except ValueError:
            print("Please enter a valid number for size.")
    
    df = pd.DataFrame(furniture) ## The array is converted to dataframe
    return df


# Save the DataFrame in Excel file
def save_to_excel(df, filename):
    df.to_excel(filename, index=False)
    print(f"Data saved to {filename}.")

# Main execution
if __name__ == "__main__":
    df = create_dataframe()
    save_to_excel(df, "cm_measures.xlsx")
