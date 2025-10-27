🔐 Password Strength Analyzer & Smart Wordlist Generator

> ⚡ A Python-powered cybersecurity tool built in a 4-hour sprint — analyze password strength with zxcvbn and craft custom attack-ready wordlists from target-specific keywords.


🚀 Quick Links & Badges


✨ What it does

A compact dual-purpose utility for:

Password analysis (strength score 0–4, crack time estimates, warnings & suggestions).

Custom wordlist generation from user-provided keywords (names, pets, dates, nicknames) with permutations, leetspeak, numeric ranges, and symbol affixes — exported as .txt for use in tools like Hashcat, John the Ripper, or Hydra.





🧠 Features

🔎 Password Analyzer (analyze)

Score: 0 (Very Weak) → 4 (Very Strong).

Estimated crack times for both online and offline attack models.

Actionable warnings and suggestions to harden passwords.


🧰 Wordlist Generator (generate)

Input personal keywords (e.g., naveen, patil, football, 2004).

Generate permutations with:

Uppercase / lowercase variations

Leetspeak substitutions (a → @, e → 3, i → 1, o → 0, s → $)

Numeric suffixes/prefixes and year ranges (e.g., 1990–2025)

Common symbols appended/prepended (!, #, @, $)


Exports a clean .txt wordlist (one entry per line).





⚙ Installation

# clone repo
git clone https://[github.com/naveen-patil/password-strength-analyzer.git](https://github.com/InfoNaveen/Password_Strength_Analyzer.git)
cd Password_Strength_Analyzer

# install dependencies
pip install -r requirements.txt

> requirements.txt (example)



zxcvbn

(If your project uses a different zxcvbn package name, ensure the correct package is listed — e.g., zxcvbn-python.)




🚀 Usage

🧩 Analyze Password Strength

python main.py analyze

Follow the prompt to input a password. Output includes:

Strength score (0–4)

Crack time estimates

Warnings & suggestions


🧠 Generate Wordlist

python main.py generate

Follow prompts to enter keywords, numeric ranges, and symbols. Result is saved to wordlist_<timestamp>.txt in the project folder.




📂 Example Outputs

Wordlist sample

naveen
Naveen
n@veen
N@V33N2024
patil!99
patil#2004

Analysis sample

Password: Naveen@2024
Score: 3 (Strong)
Estimated Crack Time (Online): months
Estimated Crack Time (Offline): years
Suggestions: Add more length and unique symbols; avoid common patterns




🧾 Project Structure (suggested)

password-strength-analyzer/
├─ main.py              # CLI entrypoint (analyze / generate)
├─ analyzer.py          # zxcvbn wrapper & formatting helpers
├─ generator.py         # permutation & export logic
├─ requirements.txt
├─ README.md
└─ LICENSE




🧑‍💻 Tech Stack

Python 3.x

zxcvbn — password strength estimator

Standard libraries: itertools, random, datetime, argparse





✅ Use Cases

Ethical hacking / red teaming (wordlist tailoring)

Password hygiene training & demos

Security research into human-chosen passwords

Learning tool for students of cybersecurity





🌟 Future Enhancements

GUI (Streamlit / Tkinter) for easier use

Check passwords against breach databases (Have I Been Pwned API)

Hybrid dictionary + controlled brute force generation modes

Multi-language support and larger permutation templates





🤝 Contributing

Contributions welcome!

1. Fork it 🔱


2. Create a feature branch git checkout -b feat/awesome


3. Commit your changes git commit -m "feat: add awesome feature"


4. Push git push origin feat/awesome and open a PR






📝 License

This repository is licensed under the MIT License — use responsibly for ethical and educational purposes only.




🔗 Author & Contact (GitHub-ready)

Naveen Patil
GitHub: https://github.com/naveen-patil
Email: naveen.a.patil.best.123@gmail.com




📦 Clone & Get Started (one-liner)

git clone https://github.com/naveen-patil/Password_Strength_Analyzer.git && cd password_strength_analyzer && pip install -r requirements.txt




