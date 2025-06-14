# Problem: https://leetcode.com/problems/sorting-the-sentence/submissions/1663619611/
# LC 1859. Sorting the Sentence
# Difficulty: Easy
# Approach: Hash Map

class Solution:
    def sortSentence(self, string: str) -> str:
        value = string.split()
        hashmap = {}
        for i in range(len(value)):
            hashmap[value[i][-1]] = value[i][:len(value[i])-1]    # {2 : is, 4: sentense, 1: This, 3: a}

        hashmap = dict(sorted(hashmap.items()))

        return " ".join(hashmap.values())
        

    

"""Time complexity : O(n)
Space complexity : O(n) + O(n)

Intutuion: To use hashmap and create and sort the keys in ascending order and
join them again  after sorting the dict based on the keys.


"""





        


