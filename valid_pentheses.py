class Solution:
    def isValid(self, s: str) -> bool:
        closing_parentheses = []
        # loop through str
        for char in s:
            # if character is either (, [, {
            if char in '(, [, {':
                # add ) ] } to list
                if char == '(':
                    closing_parentheses.append(')')
                if char == '[':
                    closing_parentheses.append(']')
                if char == '{':
                    closing_parentheses.append('}')
            # if character is ) ] }
            if char in ') ] }':
                if char == ')':
                    try:
                        closing_parentheses.remove(')')
                    except ValueError:
                        pass
                if char == ']':
                    try:
                        closing_parentheses.remove(']')
                    except ValueError:
                        pass
                if char == '}':
                    try:
                        closing_parentheses.remove('}')
                    except ValueError:
                        pass
        # if list is empty, return True
        if len(closing_parentheses) == 0:
            return True
        else:
            return False