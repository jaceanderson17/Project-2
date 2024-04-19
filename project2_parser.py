# If you haven't read the P2 post in campuswire, read it before you continue.

# If you have working lexer of project 1, then you are good to go, you just
# need few modifications in the lexer. I believe you are better off, if you
# just extend it.

# If you don't have a working lexer for project 1, we have provide a skelton of 
# lexer. You need to complete the functions commented with tokenize.

# Lexer
class Lexer:
    def __init__(self, code):
        self.code = code
        self.position = 0

    # move the lexer position and identify next possible tokens.
    def get_token(self):
        if self.position >= len(self.code):
            return None
        else:
            token = self.code[self.position]
            while (self.position < len(self.code) and (self.code[self.position] == ' ' or self.code[self.position] == '\t' or self.code[self.position] == '\n')):
                self.position += 1

            if self.position >= len(self.code):
                return None
            token = self.code[self.position]
            if (token.isalpha()):
                self.position += 1
                if (token == 'i' and (self.position + 2) < len(self.code)):
                    helperString = self.code[(self.position): (self.position + 2)]
                    if (helperString == 'f '):
                        self.position += 2
                        return ['if', 'if_statement']
                    elif (helperString == 'nt' and self.code[(self.position) + 2] == ' '):
                        self.position += 2
                        return ['int', 'type']
                    else:
                        helperString = token
                        token = self.code[self.position]
                        while (token != ' ' and token != '\t' and token != '\n' and token != ')' and self.position + 1 < len(self.code)):
                            helperString += token
                            self.position += 1
                            token = self.code[self.position]
                        return [helperString, 'variable']
                elif (token == 't' and (self.position + 4) < len(self.code)):
                    helperString = self.code[(self.position): (self.position + 4)]
                    if (helperString == 'hen\n' or helperString == 'hen '):
                        self.position += 4
                        return ['then', 'then_statement']
                    else:
                        helperString = token
                        token = self.code[self.position]
                        while (token != ' ' and token != '\t' and token != '\n' and token != ')' and self.position + 1 < len(self.code)):
                            helperString += token
                            self.position += 1
                            token = self.code[self.position]
                        return [helperString, 'variable']
                elif (token == 'w' and (self.position + 5) < len(self.code)):
                    helperString = self.code[(self.position): (self.position + 5)]
                    if (helperString == 'hile '):
                        self.position += 5
                        return ['while', 'while_loop']
                    else:
                        helperString = token
                        token = self.code[self.position]
                        while (token != ' ' and token != '\t' and token != '\n' and token != ')' and self.position + 1 < len(self.code)):
                            helperString += token
                            self.position += 1
                            token = self.code[self.position]
                        return [helperString, 'variable']
                elif (token == 'd' and (self.position + 1) < len(self.code)):
                    helperString = self.code[(self.position): (self.position + 2)]
                    if (helperString == 'o\n' or helperString == 'o '):
                        self.position += 2
                        return ['do', 'do_statement']
                    else:
                        helperString = token
                        token = self.code[self.position]
                        while (token != ' ' and token != '\t' and token != '\n' and token != ')' and self.position + 1 < len(self.code)):
                            helperString += token
                            self.position += 1
                            token = self.code[self.position]
                        return [helperString, 'variable']
                elif (token == 'e' and (self.position + 3) < len(self.code)):
                    helperString = self.code[(self.position): (self.position + 4)]
                    if (helperString == 'lse '):
                        self.position += 4
                        return ['else', 'else_statement']
                    else:
                        helperString = token
                        token = self.code[self.position]
                        while (token != ' ' and token != '\t' and token != '\n' and token != ')' and self.position + 1 < len(self.code)):
                            helperString += token
                            self.position += 1
                            token = self.code[self.position]
                        return [helperString, 'variable']
                elif (token == 'f' and (self.position + 4) < len(self.code)):
                    helperString = self.code[(self.position): (self.position + 5)]
                    if (helperString == 'loat '):
                        self.position += 5
                        return ['float', 'type']
                    else:
                        helperString = token
                        token = self.code[self.position]
                        while (token != ' ' and token != '\t' and token != '\n' and token != ')' and self.position + 1 < len(self.code)):
                            helperString += token
                            self.position += 1
                            token = self.code[self.position]
                        return [helperString, 'variable']
                else:
                    helperString = token
                    token = self.code[self.position]
                    while token.isalpha() or token.isdigit():
                        helperString += token
                        self.position += 1
                        token = self.code[self.position]
                    return [helperString, 'variable']
            elif (token == '='):
                self.position += 1
                if (self.code[self.position] in ['>', '<', '=']):
                    token += self.code[self.position]
                    self.position += 1
                    return [token, 'comparison']
                return [token, 'expression']
            elif (token in ['+', '-', '*', '/']):
                self.position += 1
                return [token, 'arithmetic_operator']
            elif (token == '!'):
                token = '!='
                self.position += 2
                return [token, 'comparison']
            elif (token == '(' or token == ')'):
                self.position += 1
                return [token, 'parenthesis']
            elif (token == '{' or token == '}'):
                self.position += 1
                return [token, 'startOrEnd']
            elif (token == '>' or token == '<'):
                self.position += 1
                if (self.code[self.position] == '='):
                    token += self.code[self.position]
                    self.position += 1
                    return [token, 'comparison']
                return [token, 'comparison']
            elif (token.isalnum()):
                isDecimal = False
                self.position += 1
                helperString = token
                token = self.code[self.position]
                while token.isdigit() or token == '.':
                    helperString += token
                    if token == '.':
                        isDecimal = True
                    self.position += 1
                    token = self.code[self.position]
                if (isDecimal):
                    return [helperString, 'float_digit']
                else:
                    return [helperString, 'int_digit']
            return None

# Parse Tree Node definitions.
# Don't need to modify these definitions for the completion of project 2.

# But if you are interested in modifying these definitions for
# learning purposes. Then Don't whatever you want.

class Node:
    pass

class ProgramNode(Node):
    def __init__(self, statements):
        self.statements = statements

class DeclarationNode(Node):
    def __init__(self, identifier, expression, myType):
        self.identifier = identifier
        self.expression = expression
        self.type       = myType

class AssignmentNode(Node):
    def __init__(self, identifier, expression):
        self.identifier = identifier
        self.expression = expression

class IfStatementNode(Node):
    def __init__(self, condition, if_block, else_block):
        self.condition = condition
        self.if_block = if_block
        self.else_block = else_block

class WhileLoopNode(Node):
    def __init__(self, condition, loop_block):
        self.condition = condition
        self.loop_block = loop_block

class ConditionNode(Node):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

class ArithmeticExpressionNode(Node):
    def __init__(self, operator, left, right, myType):
        self.operator = operator
        self.left = left
        self.right = right
        self.type  = myType

class TermNode(Node):
    def __init__(self, operator, left, right, myType):
        self.operator = operator
        self.left = left
        self.right = right
        self.type  = myType

class FactorNode(Node):
    def __init__(self, value, myType):
        self.value = value
        self.type = myType




# final parser - student copy

# Skelton of Parser class.
# For project 1, we should have implemented parser that returns a string representation.
# For project 2:
  # 1. You have to build the Parse tree with the node definitions given to you. The core
  # logic of how to parse the lanague will not differ, but you to have create Tree node
  # whereever you are creating tuple in the project 1.
  # 2. Implement symbol table and scoping rules. 
  #   Hint: You can use stack to model the nested scopes and a dictionary to store identifiers
  #   and its type.

  # For those who are interested, you call print_parse_tree to view the text representation
  # of Parse Tree.


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = None
        self.advance()
        self.messages = []
        self.symbolTable = [[]]
        self.assignmentType = None
        self.declaration = False

    # function to parse the entire program
    def parse_program(self):
        # while self.current_token != None:
        #     print(self.current_token)
        #     self.advance()
        # return None
        return self.program()
        
            
        
    # move to the next token.
    def advance(self):
        self.current_token = self.lexer.get_token()

    # parse the one or multiple statements
    def program(self):
        tokens = ''
        while self.current_token != None:
            self.statement()
        print(self.messages)
        return self.messages
        
    
    # parse if, while, assignment statement.
    def statement(self):
        if self.current_token and self.current_token[1] == 'variable':
            self.declaration = False
            return self.assignment()
        elif self.current_token and self.current_token[1] == 'type':
            self.assignmentType = self.current_token[0]
            self.advance()
            self.declaration = True
            return self.assignment()
        elif self.current_token and self.current_token[1] == 'if_statement':
            return self.if_statement()
        elif self.current_token and self.current_token[1] == 'while_loop':
            return self.while_loop()
        return None


    # parse assignment statements
    def assignment(self):
        first = self.current_token
        if self.declaration:
            isAlreadyDeclared = self.isDeclaredInScope(first[0])
            if isAlreadyDeclared:
                self.messages.append(f'Variable {first[0]} has already been declared in the current scope')
        self.advance()
        if self.current_token and self.current_token[0] == '=':
            self.advance()
            returnNode = self.arithmetic_expression()
            if (self.declaration and self.assignmentType != returnNode.type):
                self.symbolTable[-1].append({first[0]: [self.assignmentType, None]})
                self.messages.append(f'Type Mismatch between {self.assignmentType} and {returnNode.type}')
            elif (self.declaration and self.assignmentType == returnNode.type):
                self.symbolTable[-1].append({first[0]: [self.assignmentType, self.assignmentType]})
            elif (self.declaration == False and self.getAssignType(first[0]) != returnNode.type):
                self.messages.append(f'Type Mismatch between {self.getAssignType(first[0])} and {returnNode.type}')
                self.updateSymbol(first[0], [first[1], None])
            returnNode = AssignmentNode(first[0], returnNode)
            return returnNode
            # return '(\'=\', \'' + first + '\', ' + self.arithmetic_expression() + ')'
        return None

    #parse arithmetic expressions
    def arithmetic_expression(self):
        returnStr = self.term()
        while self.current_token and self.current_token[1] == 'arithmetic_operator' and self.current_token[0] in ['+', '-']:
            plusMinus = self.current_token[0]
            self.advance()
            secondNum = self.term()
            returnStr = ArithmeticExpressionNode(plusMinus, returnStr, secondNum)
            # returnStr = '(' + plusMinus + ', ' + returnStr + ', ' + self.term() + ')'
        return returnStr

    def term(self):
        returnStr = self.factor()
        while self.current_token and self.current_token[1] == 'arithmetic_operator' and self.current_token[0] in ['*', '/']:
            multDiv = self.current_token[0]
            self.advance()
            returnStr2 = self.factor()
            if (returnStr.type == returnStr2.type):
                type = returnStr2.type
            else:
                self.messages.append(f'Type Mismatch between {returnStr.type} and {returnStr2.type}')
                type = None
            returnStr = TermNode(multDiv, returnStr, returnStr2, type)
            # returnStr = '(' + multDiv + ', ' + returnStr + ', ' + self.factor() + ')'
        return returnStr

    def factor(self):
        first = self.current_token
        if first is None:
            return None
        self.advance()
        if first[1] == 'int_digit':
            return FactorNode(first[0], 'int')
        elif first[1] == 'float_digit':
            return FactorNode(first[0], 'float')
        elif first[1] == 'variable':
            return FactorNode(first[0], self.getType(first[0]))
        elif first[0] == '(':
            exp = self.arithmetic_expression()
            if self.current_token and self.current_token[0] == ')':
                self.advance()
            return exp
        elif first[1] == 'comparison':
            return first[0]
        return None
    

    # parse if statement, you can handle then and else part here.
    # you also have to check for condition.
    def if_statement(self):
        self.advance()
        second = self.condition()
        if (self.current_token[0] == 'then'):
            self.advance()
        if (self.current_token[0] == '{'):
            self.symbolTable.append([])
            self.advance()
        third = []
        while (self.current_token[0] != '}'):
            third.append(self.statement())
        if (self.current_token[0] == '}'):
            self.advance()
            self.symbolTable.pop()
        if (self.current_token and self.current_token[0] == 'else'):
            self.advance()
            self.advance()
            self.symbolTable.append([])
            elseAddition = []
            while self.current_token[0] != '}':
                elseAddition.append(self.statement())
            self.symbolTable.pop()
            self.advance()
            return IfStatementNode(second, third, elseAddition)
        else:
            return IfStatementNode(second, third, None)

        # if self.current_token == None or self.current_token[0] != 'else':
        #     return '(\'if\', ' + second + ', ' + third + ')'
        # else:
        #     self.advance()
        #     if self.current_token == '{':
        #         self.advance()
        #     print(second, third)
        #     return '(\'if\', ' + second + ', ' + third + ', ' + self.statement() + ')'

    
    # implement while statment, check for condition
    # possibly make a call to statement?
    def while_loop(self):
        self.advance()
        second = self.condition()
        if self.current_token[0] == 'do':
            self.advance()
        if self.current_token[0] == '{':
            self.advance()
            self.symbolTable.append([])
        returnNode = WhileLoopNode(second, self.statement())
        if self.current_token[0] == '}':
            self.advance()
            self.symbolTable.pop()
        return returnNode
        # return '(\'while\', ' + second + ', [' +  self.statement() + '])'
    

    def condition(self):
        first = self.factor()
        second = self.factor()
        third = self.factor()
        return ConditionNode(first, second, third)
        # return '(' + second + ', ' + first  + ', ' + third + ')'
    
    def getType(self, variable):
        isDeclared = self.isDeclared(variable)
        if isDeclared:
            i = len(self.symbolTable) - 1
            while (i >= 0):
                for dict in self.symbolTable[i]:
                    if variable in dict:
                        return dict[variable][1]
                i -= 1
        return None
    
    def getAssignType(self, variable):
        isDeclared = self.isDeclared(variable)
        if isDeclared:
            i = len(self.symbolTable) - 1
            while (i >= 0):
                for dict in self.symbolTable[i]:
                    if variable in dict:
                        return dict[variable][0]
                i -= 1
        return None

    def isDeclared(self, variable):
        i = len(self.symbolTable) - 1
        while i >= 0:
            for dict in self.symbolTable[i]:
                if variable in dict:
                    return True
            i -= 1
        return False
    
    def isDeclaredInScope(self, variable):
        i = len(self.symbolTable) - 1
        currentTable = self.symbolTable[i]
        for dict in currentTable:
            if variable in dict:
                return True
        return False
    
    def updateSymbol(self, variable, update):
        i = len(self.symbolTable) - 1
        while (i >= 0):
            for dict in self.symbolTable[i]:
                if variable in dict:
                    dict[variable] = update
                    return
            i -= 1
        return



