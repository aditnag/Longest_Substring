class Solution(object):
    @staticmethod
    def longest_substring(s):

        left_pointer = 0
        right_pointer = 0
        d = {}
        ans = 0
        while right_pointer < len(s):
            if s[right_pointer] not in d or left_pointer > d[s[right_pointer]]:
                ans = max(ans, (right_pointer - left_pointer + 1))
                d[s[right_pointer]] = right_pointer
            else:
                left_pointer = d[s[right_pointer]] + 1
                ans = max(ans, (right_pointer - left_pointer + 1))
                right_pointer -= 1
            # print(ans)
            right_pointer += 1
        return ans


ob1 = Solution()
print(ob1.longest_substring("abcabcbb"))
print(ob1.longest_substring("bbbbb"))
print(ob1.longest_substring("pwwkew"))
print(ob1.longest_substring(""))

