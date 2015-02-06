"""
Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.
 For example, the longest substring without repeating letters for "abcabcbb" is "abc",
which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
"""


class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        char_indices, max_len, last_repeat_offset = {}, 0, 0

        for i in range(len(s)):
            if s[i] in char_indices:
                if char_indices[s[i]] >= last_repeat_offset:
                    max_len = max(max_len, i - char_indices[s[i]])
                    max_len = max(max_len, i - last_repeat_offset)
                    last_repeat_offset = char_indices[s[i]] + 1

            char_indices[s[i]] = i

        return max(max_len, len(s) - last_repeat_offset)


    def lengthOfLongestSubstring_recur(self, s):
        if len(s) <= 1:
            return len(s)
        elif s[0] == s[1]:
            return max(1, self.lengthOfLongestSubstring_recur(s[1:]))
        else:
            sub_str = s[1:]
            no_repate_str = set(s[0])
            for i in range(len(sub_str)):
                if sub_str[i] not in no_repate_str:
                    no_repate_str.add(sub_str[i])
                else:
                    break

            return max(len(no_repate_str), self.lengthOfLongestSubstring_recur(s[1:]))


if __name__ == '__main__':
    s = """
Linux kernel management style, by Linus Torvalds1

openlife.cc

This is a short document describing the preferred (or made up, depending on who you ask) management style for the linux kernel. It's meant to mirror the CodingStyle document to some degree, and mainly written to avoid answering (*) the same (or similar) questions over and over again.


Management style is very personal and much harder to quantify than simple coding style rules, so this document may or may not have anything to do with reality. It started as a lark, but that doesn't mean that it might not actually be true. You'll have to decide for yourself.

Btw, when talking about "kernel manager", it's all about the technical lead persons, not the people who do traditional management inside companies. If you sign purchase orders or you have any clue about the budget of your group, you're almost certainly not a kernel manager. These suggestions may or may not apply to you.




    """
    print Solution().lengthOfLongestSubstring(s)












