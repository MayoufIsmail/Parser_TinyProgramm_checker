class ProgramNode:
    def __init__(self, functions, main_function):
        self.functions = functions
        self.main_function = main_function

class FunctionNode:
    def __init__(self, return_type, identifier, parameters, body):
        self.return_type = return_type
        self.identifier = identifier
        self.parameters = parameters
        self.body = body

class ParameterNode:
    def __init__(self, type, identifier):
        self.type = type
        self.identifier = identifier

class DeclarationNode:
    def __init__(self, type, identifier, size=None):
        self.type = type
        self.identifier = identifier
        self.size = size

class AssignmentNode:
    def __init__(self, identifier, value):
        self.identifier = identifier
        self.value = value

class IfNode:
    def __init__(self, condition, true_block, false_block=None):
        self.condition = condition
        self.true_block = true_block
        self.false_block = false_block

class WhileNode:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class ReturnNode:
    def __init__(self, expression):
        self.expression = expression

class BinaryOperationNode:
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

class UnaryOperationNode:
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

class FunctionCallNode:
    def __init__(self, identifier, arguments):
        self.identifier = identifier
        self.arguments = arguments

class LiteralNode:
    def __init__(self, value, type):
        self.value = value
        self.type = type
