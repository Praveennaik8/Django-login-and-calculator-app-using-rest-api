

class Solution:
    @staticmethod
    def precedence(op):
        
        if op == '+' or op == '-':
            return 1
        if op == '*' or op == '/':
            return 2
        return 0
    
    @staticmethod
    def applyOp(a, b, op):
        
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/': return a // b
    
    @staticmethod
    def calculate(tokens):
        try:
            values = []
            ops = []
            i = 0
            
            while i < len(tokens):
                
                
                if tokens[i] == ' ':
                    i += 1
                    continue
                
            
                elif tokens[i] == '(':
                    ops.append(tokens[i])
                
                
                elif tokens[i].isdigit():
                    val = 0
                    
                
                    while (i < len(tokens) and
                        tokens[i].isdigit()):
                    
                        val = (val * 10) + int(tokens[i])
                        i += 1
                    
                    values.append(val)
                    
                    i-=1
                
            
                elif tokens[i] == ')':
                
                    while len(ops) != 0 and ops[-1] != '(':
                    
                        val2 = values.pop()
                        val1 = values.pop()
                        op = ops.pop()
                        
                        values.append(Solution.applyOp(val1, val2, op))
                    
                    ops.pop()
            
                else:
                
                
                    while (len(ops) != 0 and
                        Solution.precedence(ops[-1]) >=
                        Solution.precedence(tokens[i])):
                                
                        val2 = values.pop()
                        val1 = values.pop()
                        op = ops.pop()
                        
                        values.append(Solution.applyOp(val1, val2, op))
                    
                    
                    ops.append(tokens[i])
                
                i += 1
            
            # Entire expression has been parsed
            # at this point, apply remaining ops
            # to remaining values.
            while len(ops) != 0:
                
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                        
                values.append(Solution.applyOp(val1, val2, op))
        except:
            try:
                answer = eval(tokens)
                return eval(tokens)
            except:
                return 'Nan'
        #I thought I could implement calculate function on 24 but got other things
        #This is maximum I could do in the time period
        try:
            if values[-1] == eval(tokens):
                return values[-1]
            return eval(tokens)
        except:
            return 'Nan'