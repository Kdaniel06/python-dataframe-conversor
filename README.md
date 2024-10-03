# Measurement Converter

## Description
This project consists of two Python scripts: `excel_creator.py` and `conversor.py`. The `excel_creator.py` script allows users to input furniture names and their sizes in centimeters, creating an Excel file (`cm_measures.xlsx`). The `conversor.py` script reads this Excel file and converts the measurements from centimeters to inches, feet, and meters, saving the results in a new Excel file (`converted_measures.xlsx`).

## Features
- Input furniture names and sizes in centimeters.
- Convert measurements from centimeters to inches, feet, and meters.
- Save results in Excel format using the `pandas` library.

## Requirements
This project requires Python 3.7 or higher and the following libraries:
- pandas
- openpyxl

You can install the required libraries using the provided `requirements.txt`.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
    
## Usage
### Run the Excel Creator:

Execute the excel_creator.py script to create an Excel file with furniture names and sizes.
```bash
python excel_creator.py
```

### Run the Converter:

After creating the cm_measures.xlsx file, run the conversor.py script to convert the measurements and save them in a new Excel file.
```bash
python conversor.py
```

### Example
When prompted, enter furniture names and their corresponding sizes in centimeters. Type 'done' when finished.
The program will generate an Excel file named cm_measures.xlsx in the same directory.
The converter will then read this file and create a new file named converted_measures.xlsx with the converted measurements.

## Author 
Daniel Cascante

## Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests.