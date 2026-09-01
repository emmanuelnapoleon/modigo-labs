def count_vowels(text):
    vowels = "aeiou"
    count = 0
    # TODO: loop through `text`, check each character (case-insensitively)
    # against `vowels`, and increment `count` when it matches
    for vowel in text:
        if vowel.lower() in vowels:
            count = count + 1 
    return count

print(count_vowels('Education'))