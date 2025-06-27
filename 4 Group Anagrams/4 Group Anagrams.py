from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}
        for string in strs:
            # Sort the string to get its canonical form eat -> aet
            sorted_string = "".join(sorted(string))

            # If sorted string not a key in dictionary, add it with empty list
            if sorted_string not in anagram_groups:
                anagram_groups[sorted_string] = []
            
            # Append the original string to the list associated with its sorted form
            anagram_groups[sorted_string].append(string)
        # Return the values of the dictionary, which are the lists of anagrams
        return list(anagram_groups.values())

solver = Solution()
input_strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = solver.groupAnagrams(input_strings)
print(result)