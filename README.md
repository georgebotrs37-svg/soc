🛡️ SSH Auth Log Analyzer (SOC Project)
A Python-based security tool designed to parse authentication logs, detect failed login attempts, and flag potential Brute Force attacks. This tool is part of a Security Operations Center (SOC) simulation project.
🚀 Features
Log Parsing: Uses Regular Expressions (Regex) to extract IP addresses from failed login entries.
Brute Force Detection: Automatically flags any IP address with 3 or more failed attempts as a potential threat.
Visual Alerts: Uses colorama for color-coded terminal output (Cyan for info, Red for alerts, Green for success).
Data Export: Saves the analysis results into a structured .csv file for further investigation.
🛠️ Requirements
Make sure you have Python installed. You will also need the following libraries:
code
Bash
pip install pandas colorama
📁 Project Structure
To ensure the script runs correctly, your folder should look like this:
code
Text
SOC/
├── analyzer.py       # The main Python script
├── auth.log          # The log file containing authentication data
└── reports/          # Folder where the report will be saved (created automatically)
    └── security_report.csv
📖 How to Use
Prepare the Log File: Create a file named auth.log in the same directory as the script.
Add Data: Paste your SSH logs (e.g., Failed password for root from 192.168.1.10...) into auth.log.
Run the Script:
code
Bash
python analyzer.py
Check Results:
View the live analysis in your terminal.
Open the generated report in reports/security_report.csv.
📊 Sample Output
Terminal:
=== Failed Login Attempts === (Shows IP list)
⚠ ALERT: Possible Brute Force from 192.168.1.10
CSV Report:
| IP Address | Failed Attempts |
| ------------- | --------------- |
| 192.168.1.10 | 4 |
| 10.0.0.5 | 1 |
📝 License
This project is for educational purposes. Feel free to use and modify it!
