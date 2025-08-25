# Hostname Resolver in Python

This Python script allows users to input hostnames and resolves them to IP addresses. Users can then select a hostname to view its corresponding IP. This project demonstrates basic networking concepts and Python programming skills.

---

## Features
- Enter multiple hostnames to resolve
- Resolve hostnames to IP addresses using Python's `socket` module
- Look up specific host IPs by selecting the hostname index
- Handles invalid hostnames and incorrect input

---

## Tools / Technologies
- Python 3
- Standard Library (`socket` module)
- Command-line interface (CLI)

---

## How to Run
1. Clone or download the repository.
2. Open a terminal and navigate to the project folder.
3. Run the script:

4. Follow the on-screen prompts:
   - Enter hostnames one by one
   - Press **Enter** to finish
   - Enter the index of a hostname to see its IP
   - Press **Enter** again to quit

---

## Example Interaction
Enter a hostname or press enter to finish: google.com
Enter a hostname or press enter to finish: github.com
Enter a hostname or press enter to finish:

0: google.com
1: github.com

Enter the index of the hostname you want to look up (or press enter to quit): 0
google.com - 142.250.190.78


---

## Learning Outcomes
- Practiced Python functions, loops, and error handling
- Learned to use the `socket` module for networking tasks
- Gained experience with CLI user input and output formatting
