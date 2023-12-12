def is_vowel(ch):
    return ch in ['A', 'E', 'I', 'O', 'U']

def can_reach_codetown(town):
    CODETOWN = "CODETOWN"
    
    for i in range(len(town)):
        # If characters have different vowel-consonant nature, transformation is not possible
        if is_vowel(town[i]) != is_vowel(CODETOWN[i]):
            return False
    
    return True

if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        town = input()
        
        if can_reach_codetown(town):
            print("YES")
        else:
            print("NO")
