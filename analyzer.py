# password_analyzer.py
from zxcvbn import zxcvbn

def analyze_password(password):
    """
    Analyzes the strength of a given password using zxcvbn.
    """
    results = zxcvbn(password)
    
    # Extract key information
    score = results['score']
    strength = {
        0: "Very Weak  weakest",
        1: "Weak",
        2: "Fair",
        3: "Strong",
        4: "Very Strong 🔒"
    }
    
    print(f"--- Password Analysis ---")
    print(f"Password: {'*' * len(password)}")
    print(f"Strength Score: {score}/4 ({strength.get(score)})")
    print(f"Time to crack (offline, fast hash): {results['crack_times_display']['offline_fast_hashing_1e10_per_second']}")
    print(f"Time to crack (online, throttle): {results['crack_times_display']['online_throttling_100_per_hour']}")
    
    if results['feedback']['warning']:
        print(f"\nWarning: {results['feedback']['warning']}")
    
    if results['feedback']['suggestions']:
        print("Suggestions:")
        for suggestion in results['feedback']['suggestions']:
            print(f"- {suggestion}")
    
    print("--- End of Analysis ---")
