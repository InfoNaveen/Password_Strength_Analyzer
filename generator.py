# wordlist_generator.py
import itertools
from datetime import datetime
import os  # <-- Import for path security

def generate_wordlist(keywords, start_year, end_year, output_file):
    """
    Generates a custom wordlist from keywords, names, dates, etc.,
    streaming directly to a file to save memory.
    """
    
    # --- VULNERABILITY FIX: Path Traversal ---
    try:
        # Get the "real" absolute path of the intended file
        target_path = os.path.realpath(output_file)
        # Get the "real" absolute path of the current directory
        current_dir = os.path.realpath(os.getcwd())
        
        # Check if the target path starts with the current directory path
        if not target_path.startswith(current_dir):
            print(f"Error: Invalid output path. File must be within the project directory.")
            return  # Exit the function
    except Exception as e:
        print(f"Error processing path: {e}")
        return
    # --- END OF FIX ---

    print(f"Generating wordlist based on: {keywords}")
    count = 0
    
    # --- PERFORMANCE FIX: Stream directly to file ---
    try:
        # Use the "safe" target_path variable
        with open(target_path, 'w') as f:
            base_words = set()
            for key in keywords:
                base_words.add(key.lower())
                base_words.add(key.upper())
                base_words.add(key.capitalize())
            
            # 1. Write base words first
            for word in base_words:
                f.write(word + '\n')
                count += 1
            
            # 2. Generate and write leetspeak words
            leet_map = {'a': '@', 'e': '3', 'i': '1', 'o': '0', 's': '$'}
            leet_words = set()
            for word in base_words:
                leet_word = word
                for char, leet in leet_map.items():
                    leet_word = leet_word.replace(char, leet)
                if leet_word != word:
                    f.write(leet_word + '\n')
                    count += 1
                    leet_words.add(leet_word) # Save for the next step
            
            base_words.update(leet_words)

            # 3. Define affixes
            affixes = [str(y) for y in range(start_year, end_year + 1)]
            affixes.extend(['123', '12345', '!', '@', '#'])

            # 4. Generate and write combined words
            for word in base_words:
                for affix in affixes:
                    f.write(word + affix + '\n')
                    f.write(affix + word + '\n')
                    count += 2
        
        print(f"\n✅ Success! Wordlist saved to '{output_file}'")
        print(f"Total passwords generated: {count}")

    except IOError as e:
        print(f"Error writing to file: {e}")
