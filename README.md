# Automated Member Lottery

**Building AI course project**

## Summary
Create an AI-driven solution that automates the monthly member lottery for the union board. The lottery selects three winners from a list of 500 members, and the winners cannot win again until everyone else has won.

## Background

### Problem:
- The current lottery is manually handled with an Excel file, which can be time-consuming and prone to errors.
- Ensuring that winners cannot win again until everyone else has won is difficult to track manually.

### Motivation:
- Streamline and automate the lottery process to save time and minimize the risk of errors.
- Ensure fair prize distribution among members.

### Importance:
- Automation can free up time for other important tasks within the union.
- A fair and transparent lottery process is essential to maintain members' trust.

## Data sources and AI techniques

### Data Sources:
- Member data: An Excel file with 500 members containing their names and status (whether they have won or not).

### AI Techniques:
- Data Cleaning and Preprocessing
- Random Selection Algorithm
- Update Mechanism

## How is it used?

### Process:
1. **Data Ingestion**: Load the member data from the Excel file.
2. **Random Selection**: Use a random selection algorithm to choose three winners from the list of non-previous winners.
3. **Update Status**: Update the Excel file to mark the winners as having won.
4. **Generate Report**: Update the Word document template with the names of the winners and save it as a new file for the current month.

### Users:
- Union board administrators who manage the lottery process.

## Challenges

### Limitations:
- The algorithm cannot guarantee absolute fairness if the data is incorrect.
- Manual data entry may still introduce errors.

### Ethical Considerations:
- Ensure the algorithm's randomness to maintain trust in the lottery process.

## What next?

### Expansion:
- Include a feature to automatically send emails to the winners.
- Create a user interface for easier management of the lottery.

### Needs:
- Additional data to improve the algorithm's performance.
- Collaboration with union members to ensure data accuracy.

## Acknowledgments
- Building AI course from Reaktor Innovations and the University of Helsinki.
- Open source projects and AI tools like Python and Pandas for data handling.
