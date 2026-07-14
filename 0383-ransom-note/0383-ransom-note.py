class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Dono strings ke characters ki frequency count nikalo
        # Counter automatically {char: count} dict bana deta hai
        st1, st2 = Counter(ransomNote), Counter(magazine)

        # '&' operator do Counters ka INTERSECTION nikalta hai
        # matlab: har common char ki MINIMUM frequency le leta hai dono me se
        # agar ye intersection st1 (ransomNote) ke barabar hai,
        # matlab magazine me ransomNote ka har letter, jitni baar chahiye utni baar maujood hai
        if st1 & st2 == st1:
            return True
        
        return False