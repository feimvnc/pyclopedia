""" 
Gene string is combined by 4 characters, "ACGT".
Each string include a number followed by a character.
"1A2C2G1T" = "ACCGGT".

Given two gene strings, return number of same characters and total characters,
in format of "same characters" + "/" + "total characters"

Example:  
Input: 
Gene1: "2T3G"
Gene2: "3T2G"
Output: "4/5"
Explanation: "TTGGG" and "TTGGG" have total 4 same characters, total length is 5.
"""

class Solution:

    def geneSimilarity(self, Gene1: str, Gene2: str) -> str:
        gene1 = self.splitString(Gene1)
        gene2 = self.splitString(Gene2)
        # print(gene1, gene2)  #  ->[[2, 'T'], [3, 'G']] [[3, 'T'], [2, 'G']]

        index1 = 0    # two pointers 
        index2 = 0 
        tot = 0    # total count 
        same = 0  
        while index1 < len(gene1) and index2 < len(gene2):
            if gene1[index1][0] < gene2[index2][0]:
                tot += gene1[index1][0]
                if gene1[index1][1] == gene2[index2][1]:
                    same += gene1[index1][0]
                gene2[index2][0] -= gene1[index1][0]
                index1 += 1
            else:
                tot += gene2[index2][0]
                if gene1[index1][1] == gene2[index2][1]:
                    same += gene2[index2][0]
                gene1[index2][0] -= gene2[index1][0]
                index2 += 1 

        return str(same) + "/" + str(tot)

    def splitString(self, s):
        result = []  
        now = 0 
        for i in range(len(s)):
            if '0' <= s[i] <= '9':  # get number string 
                now = now * 10 + ord(s[i]) - ord('0')
            else:
                result.append([now, s[i]])
                now = 0 
        return result 


Gene1 = "2T3G"
Gene2 = "3T2G"
print(Solution().geneSimilarity(Gene1, Gene2))   # -> 4/5