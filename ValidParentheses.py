class Solution:
        
    def isValid(self, s: str) -> bool:
        """
        this is a stack problem.
        1. every open bracket closed by same type [...]
        2. opens are closed in correct order [{()}] good {[}  BAD
        3. every close has a corresponding open of same type ([{}]) GOOD {{]} BAD ] has no [

        Basically, a stack problem, we push opens onto stack, pop off stack when encountering closers. If closing but does not 
        match with top of stack, return false immediately, by rule 2 not in correct order
        then by end, if stack is still nonempty, return false, since invalid parentheses
        only when stack is empty do we return true
        so we have stack ...
        we iterate through s character by character, pushing onto and popping off stack

        we check at the end

        define: 
        stack: list
        for c in s:
            if opening character..
            push onto stack
            if closing character..
                pop off stack, but if they do not match (ex: {]), return false
        """

        # define our stack to track parentheses
        stack = []
        opening_chars = {'{', '[', '('}
        closing_chars = {'}', ']', ')'}

        # iterate through each character, catching if valid parentheses order based on stack rule
        for c in s:
            if c in opening_chars:
                stack.append(c) # push onto stack
            
            if c in closing_chars:
                if not stack: # edge case: closing character but no opening braces, we know its invalid
                    return False
                popped_parentheses = stack.pop()
                # logic to check if match
                if not (self.check_match(popped_parentheses, c)):
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False

    def check_match(self, first_char, second_char):
        if first_char == '{' and second_char == '}':
            return True
        elif first_char == '[' and second_char == ']':
            return True  
        elif first_char == '(' and second_char == ')':
            return True
        else:
            return False

if __name__ == "__main__":
    t = Solution()
    test = "{[()]}"
    print(t.isValid(test))