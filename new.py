#1249. Minimum Remove to Make Valid Parentheses
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        total_open = 0
        bal = 0
        char_list = []
        result = []

        for i in s:
            if i == "(":
                total_open += 1
                bal += 1

            elif i == ")":
                if bal == 0:
                    continue
                bal -= 1

            char_list.append(i)

        open_to_keep = total_open - bal

        for i in char_list:
            if i == "(":
                open_to_keep -= 1
                if open_to_keep < 0:
                    continue
            result.append(i)

        return "".join(result)

--------------------------------------------------------




            




        
