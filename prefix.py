def is_vowel(c):
    return c in 'aeiou'

def count_balanced(arr):
    prefix = 0
    ans = 0
    mp = {0: 1}
    
    for s in arr:
        val = 0
        
        for c in s:
            if is_vowel(c):
                val += 1
            else:
                val -= 1
        
        prefix += val
        
        if prefix in mp:
            ans += mp[prefix]
        
        mp[prefix] = mp.get(prefix, 0) + 1
    
    return ans
if __name__ == "__main__":
    arr = ["aeio", "aa", "bc", "ot", "cdbd"]
    print("Balanced count:", count_balanced(arr))
