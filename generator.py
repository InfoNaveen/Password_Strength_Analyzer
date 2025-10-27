# wordlist_generator.py
import itertools
from datetime import datetime

def generate_wordlist(keywords, start_year, end_year, output_file):
    """
    Generates a custom wordlist from keywords, names, dates, etc.
    """
    print(f"Generating wordlist based on: {keywords}")
    base_words = set()
    
    # 1. Add basic mutations (lower, upper, capitalize)
    for key in keywords:
        base_words.add(key.lower())
        base_words.add(key.upper())
        base_words.add(key.capitalize())

    # 2. Add leetspeak mutations
    leet_map = {'a': '@', 'e': '3', 'i': '1', 'o': '0', 's': '$'}
    leet_words = set()
    for word in base_words:
        leet_word = word
        for char, leet in leet_map.items():
            leet_word = leet_word.replace(char, leet)
        if leet_word != word:
            leet_words.add(leet_word)
    
    base_words.update(leet_words)
    
    # 3. Define affixes (years, common numbers)
    affixes = [str(y) for y in range(start_year, end_year + 1)]
    affixes.extend(['123', '12345', '!', '@', '#'])

    # 4. Combine words and affixes
    final_wordlist = set(base_words) # Start with the base words
    
    for word in base_words:
        for affix in affixes:
            final_wordlist.add(word + affix)
            final_wordlist.add(affix + word)

    # 5. Write to file
    try:
        with open(output_file, 'w') as f:
            for word in final_wordlist:
                f.write(word + '\n')
        print(f"\n✅ Success! Wordlist saved to '{output_file}'")
        print(f"Total unique passwords generated: {len(final_wordlist)}")
    except IOError as e:
        print(f"Error writing to file: {e}")
