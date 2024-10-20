# Hongyi-Duan-Complex-SQL-Project

[![SQL Run](https://github.com/nogibjj/Hongyi-Duan-Complex-SQL/actions/workflows/hello.yml/badge.svg)](https://github.com/nogibjj/Hongyi-Duan-Complex-SQL/actions/workflows/hello.yml)

```markdown
# Data Pipeline and Analysis Project

## Project Overview
This project implements a data pipeline for extracting, transforming, loading (ETL), and querying data from a CSV file (`Heroes_3.csv`). The goal is to efficiently handle data processing and analysis tasks. The project is organized into several Python scripts, each responsible for different components of the pipeline.

## Project Structure
The project contains the following files:

1. **`main.py`**: This script serves as the main entry point of the project. It orchestrates the entire pipeline by calling other scripts and functions.
   
2. **`extract.py`**: Handles the extraction of data from the `Heroes_3.csv` file. This script reads the CSV file into a usable format, typically a DataFrame, for further transformation and loading.

3. **`transform_load.py`**: This script is responsible for transforming the extracted data. The transformations could include filtering, cleaning, or modifying the data as needed. After transforming, it loads the processed data into a database or another file format for analysis.

4. **`query.py`**: Implements functions to query the transformed data. It includes various queries for analyzing or extracting insights from the dataset.

5. **`test_main.py`**: Contains test cases to verify the functionality of the scripts and ensure the pipeline runs as expected.

6. **`Heroes_3.csv`**: The dataset used in this project. It contains data related to heroes and associated statistics.

## Dependencies
To run the project, you will need the following libraries:
- `pandas`: For data manipulation and analysis.
- `numpy`: For numerical operations (if used in transformations).
- `pytest`: For running the test cases in `test_main.py`.

You can install these dependencies using pip:

```bash
pip install pandas numpy pytest
```

## How to Run the Project

1. **Extract Data**:
   To extract the data from `Heroes_3.csv`, run the `extract.py` script. This will load the dataset into memory and print a summary of the data.
   
   ```bash
   python extract.py
   ```

2. **Transform and Load Data**:
   After extracting the data, transform and load it by running the `transform_load.py` script. This will process the data and save the cleaned version in the appropriate format.

   ```bash
   python transform_load.py
   ```

3. **Query the Data**:
   Once the data is processed, you can run queries using the `query.py` script. Modify the script to input custom queries if needed.

   ```bash
   python query.py
   ```

4. **Run Tests**:
   To verify that everything is working as expected, run the test cases in `test_main.py`. It will test various functionalities of the pipeline.

   ```bash
   pytest test_main.py
   ```

## File Descriptions

- **`main.py`**: This script can be used to run the entire ETL pipeline at once. It calls the `extract.py`, `transform_load.py`, and `query.py` scripts sequentially.
  
- **`extract.py`**: Reads the data from the CSV file and loads it into a DataFrame. The file also includes helper functions to handle file I/O operations.

- **`transform_load.py`**: Transforms the extracted data according to the project’s needs. For example, it may clean missing values, normalize certain columns, or filter unnecessary data. After transforming the data, the script loads it into a new file or database.

- **`query.py`**: Contains predefined queries to run on the transformed dataset. You can also add custom queries to extract specific insights.

- **`test_main.py`**: Includes unit tests to ensure that the pipeline works as intended. Each function in the pipeline has corresponding test cases.

- **`Heroes_3.csv`**: The dataset containing information on various heroes, their statistics, and other related data.

## Customization
Feel free to modify the scripts to fit your specific use case. For example:
- Update the `transform_load.py` file to perform additional data cleaning or transformation steps.
- Add new queries to `query.py` to extract more insights from the dataset.
- Add more test cases in `test_main.py` to ensure the robustness of the pipeline.
