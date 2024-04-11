# BELL Tx's RND System

from updateTosheet import *
from load_spreadsheet_data import *
from dynamic_stratified_randomization import *

# Setting
json_file_path = "C:/Users/USER/Downloads/randomization-bsnuhwowfit-38b6027ffe37.json"  # Google Spreadsheet API
spreadsheet_url = "https://docs.google.com/spreadsheets/d/1n1Iv7IxpT30eomhJlwy0uUyUYV5Z-hL2XSs0woe2mdU/edit#gid=1153467789"    # Google Spreadsheet URL
sheetname = "배정의 사본"
max_group_size = 15     # Maximum number of assignments that can be allocated to any single group.
group_len = 3       # Total number of groups available for assignments

# Main execution
num, factor, patient_data = load_spreadsheet_data(json_file_path, spreadsheet_url,sheetname)  # Need to check the format of spreadsheet
print(num + '-'  + factor)     # Check the current factor

assigned_group = dynamic_stratified_randomization(patient_data, factor, max_group_size, group_len)
print(assigned_group)

# Automatically updating the Google Spreadsheet with results
updateTosheet(json_file_path, spreadsheet_url,sheetname, assigned_group, num)

