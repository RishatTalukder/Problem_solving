class Solution:
    def wordToMask(self, word: str) -> int:
        mask = 0
        for ch in word:
            mask |= 1 << (ord(ch) - ord('a'))
        return mask

    def wordCount(self, startWords, targetWords) -> int:
        start_set = set()
        
        # Step 1: Convert all startWords to bitmask and store
        for word in startWords:
            mask = self.wordToMask(word)
            start_set.add(mask)

        count = 0

        # Step 2: For each targetWord, remove each letter and check
        for word in targetWords:
            target_mask = self.wordToMask(word)
            for ch in word:
                bit = 1 << (ord(ch) - ord('a'))
                reduced_mask = target_mask ^ bit  # remove one bit
                if reduced_mask in start_set:
                    count += 1
                    break  # only count once per word

        return count
