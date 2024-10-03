import pandas as pd

## Measures
def cm_to_meters(cm):
    return cm / 100

def cm_to_feet(cm):
    return cm / 30.48

def cm_to_inches(cm):
    return cm / 2.54

def convert_measures(input_file, output_file):
    try:
        df = pd.read_excel(input_file)
        # Convert
        df["Inches"] = df["Centimeters"].apply(cm_to_inches)
        df["Feet"] = df["Centimeters"].apply(cm_to_feet)
        df["Meters"] = df["Centimeters"].apply(cm_to_meters)
        
        df.to_excel(output_file, index=False)
        print(f"Measures converted and saved to {output_file}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main execution
if __name__ == "__main__":
    convert_measures("cm_measures.xlsx", "converted_measures.xlsx")
