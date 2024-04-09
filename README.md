# BELL Tx Clinical Trial Randomization Process

## Overview
BELL Tx is conducting a clinical trial focused on Cochlear Implant (CI) patients. To ensure the efficacy and reliability of our study, we employ a dynamic stratified randomization process. This approach is designed to evenly distribute patients across different groups based on specific hearing conditions and CI surgical factors.

## Stratification Factors
Patients are categorized and randomized into groups based on four key factors:
1. **Unilateral/Unilateral CI:** Unilateral hearing loss (normal hearing on the opposite side) + Unilateral CI surgery.
2. **Asymmetrical/Unilateral CI:** Asymmetrical hearing loss (hearing loss on the opposite side but not profound) + Unilateral CI surgery.
3. **Bilateral/Unilateral CI:** Bilateral profound hearing loss + Unilateral CI surgery.
4. **Bilateral/Bilateral CI:** Bilateral profound hearing loss + Bilateral CI surgeries.

## Randomization Objective
The primary goal of this stratification is to ensure that each group within the study receives an equal representation of the different patient categories. This balanced distribution is crucial for minimizing bias and enhancing the study's validity.

## Dynamic Recruitment
Our patient recruitment process is dynamic, meaning that patients are assigned to groups as they are enrolled in the study. This approach allows for continuous and flexible patient enrollment, which is essential for the diverse and evolving nature of our clinical trial.

## Technical Requirements
- **Integration with Google Spreadsheet API**: To facilitate the randomization process, our system is integrated with Google Spreadsheet. This allows for real-time data management and seamless patient assignment.
- **Automated Assignment**: The system automatically assigns new patients to the appropriate group based on the stratification factors. This automation ensures accuracy and efficiency in patient distribution.

## Essential Component
This repository includes the **'4f_Stratified RND_BELL.py'**, which is essential for performing the randomization process. It is designed to work in conjunction with the other three files included in this repository. To ensure the proper functionality and effectiveness of the randomization, it is crucial to use '4f_Stratified RND_BELL.py' file along with the other files as a comprehensive set.

Also, this code is designed to operate based on a Google Spreadsheet where the first row is composed of the columns **'ID', 'Factor', and 'Group'**. It is essential that the spreadsheet adheres to this format for the code to function correctly. Ensure that your Google Spreadsheet is structured with these specific column headers in the first row.



