def reverse_string(s):
    """Reverse a string"""
    return s[::-1]

def capitalize_words(s):
    """Capitalize each word in a string"""
    return ' '.join(word.capitalize() for word in s.split())

def count_vowels(s):
    """Count vowels in a string"""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

if __name__ == '__main__':
    print('String utilities ready\!')
    test_str = 'hello world'
    print(f'Original: {test_str}')
    print(f'Reversed: {reverse_string(test_str)}')
    print(f'Capitalized: {capitalize_words(test_str)}')
    print(f'Vowel count: {count_vowels(test_str)}')
