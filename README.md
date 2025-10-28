# 🔐 Password Strength Analyzer & Smart Wordlist Generator

> ⚡ A Python-powered cybersecurity tool built in a 4-hour sprint — analyze password strength with zxcvbn and craft custom attack-ready wordlists from target-specific keywords.

![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)


Example : https://drive.google.com/file/d/1NXUNFl6zPW9uf4TAbn73YBQ_Mzjvzzxe/view?usp=drivesdk

A compact, dual-purpose command-line utility for password auditing and security research. It analyzes password strength and generates highly customized wordlists for ethical hacking and penetration testing.

---

## 🧠 Features

* **Password Analyzer (analyze):**
    * Rates passwords on a score of 0 (Very Weak) to 4 (Very Strong).
    * Provides estimated crack times for both online and offline attack models.
    * Gives actionable warnings and suggestions from zxcvbn.

* **Wordlist Generator (generate):**
    * Takes personal keywords (names, pets, dates) as input.
    * Generates permutations with uppercase, lowercase, and leetspeak.
    * Appends/prepends number ranges (like years) and common symbols.
    * Exports a clean .txt wordlist for tools like Hashcat or John the Ripper.

* *Secure & Efficient:*
    * *Path Traversal Protection:* Sanitizes all file outputs to prevent writing outside the project directory.
    * *Memory Safe:* Streams generated wordlists directly to disk, allowing for massive lists to be created without crashing from RAM exhaustion.

---

## ⚙ Installation

```bash
# 1. Clone the repository
git clone [https://github.com/InfoNaveen/Password_Strength_Analyzer.git](https://github.com/InfoNaveen/Password_Strength_Analyzer.git)
cd Password_Strength_Analyzer

# 2. Install dependencies from requirements.txt
pip install -r requirements.txt


🚀 Usage
The tool is run from the command line using main.py and has two commands: analyze and generate.
1. Analyze a Password
Use the analyze command with the required --password flag.
python3 main.py analyze --password "Password123!"

Example Output:
--- Password Analysis ---
Password: *************
Strength Score: 3/4 (Strong)
Time to crack (offline, fast hash): 4 months
Time to crack (online, throttle): 5 centuries

Suggestions:
- Add another word or two. Uncommon words are better.
--- End of Analysis ---

2. Generate a Wordlist
Use the generate command with the required --keywords flag.
# Example: Generate a list from keywords "Naveen", "Buddy", "1999"
python3 main.py generate --keywords "Naveen" "Buddy" "1999"

# Example: Specify an output file and a different year range
python3 main.py generate --keywords "Naveen" "Buddy" --start-year 2000 --end-year 2024 --output naveen_list.txt

Example Output:
Generating wordlist based on: ['Naveen', 'Buddy', '1999']

✅ Success! Wordlist saved to 'wordlist.txt'
Total passwords generated: 746

(Total count may vary based on generation logic)
📂 Project Structure
Password_Strength_Analyzer/
├── main.py                 # Main CLI entrypoint (using argparse)
├── password_analyzer.py    # Contains analyze_password() logic
├── wordlist_generator.py   # Contains generate_wordlist() logic
├── requirements.txt        # Project dependencies (zxcvbn)
└── README.md

🧑‍💻 Tech Stack
 * Python 3.x
 * zxcvbn: For industry-standard password strength estimation.
 * argparse: For building the robust command-line interface.
 * os: For secure, cross-platform path handling.
 * datetime: For calculating the default current year.
📝 License
This project is licensed under the MIT License.
