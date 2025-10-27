# main.py
import argparse
from datetime import datetime
from password_analyzer import analyze_password
from wordlist_generator import generate_wordlist

def main():
    parser = argparse.ArgumentParser(description="Password Strength Analyzer and Custom Wordlist Generator")
    subparsers = parser.add_subparsers(dest='command', required=True, help='Available commands')

    # --- Analyze Sub-command ---
    analyze_parser = subparsers.add_parser('analyze', help='Analyze the strength of a single password')
    analyze_parser.add_argument('-p', '--password', type=str, required=True, help='The password to analyze')

    # --- Generate Sub-command ---
    gen_parser = subparsers.add_parser('generate', help='Generate a custom wordlist for attacks')
    gen_parser.add_argument('-k', '--keywords', nargs='+', required=True, help='List of keywords (e.g., name, pet, city, birth_year)')
    gen_parser.add_argument('-o', '--output', type=str, default='wordlist.txt', help='Output file name (default: wordlist.txt)')
    gen_parser.add_argument('--start-year', type=int, default=1990, help='Start year for number combinations (default: 1990)')
    gen_parser.add_argument('--end-year', type=int, default=datetime.now().year, help=f'End year for number combinations (default: current year, {datetime.now().year})')

    args = parser.parse_args()

    # --- Execute the command ---
    if args.command == 'analyze':
        analyze_password(args.password)
        
    elif args.command == 'generate':
        generate_wordlist(args.keywords, args.start_year, args.end_year, args.output)

if __name__ == "__main__":
    main()
