from enum import Enum


class Instruction(Enum):
    """
    Instruction

    The instruction is divided in 3 parts, first is the mnemonic, second part is the bytecode value for that
    instruction, the third value is the number of steps required to execute the instruction.
    Example:
        NOP = (0x00, 1)
        No operation: Mnemonic NOP, code is 0, the number of steps the program counter will take is 1.
        VAR = (0x05, 2)
        Variable: Mnemonic VAR, code is 5, the number of steps the program counter will take is 2.
    """
    NOP = (0x00, 1)
    ADD = (0x01, 1)
    SUB = (0x02, 1)
    DIV = (0x03, 1)
    MUL = (0x04, 1)
    VAR = (0x05, 2)
    API_1 = (0X06, 1)
    AND = (0x07, 1)
    XOR = (0x08, 1)
    OR = (0x09, 1)
    JEQ = (0x0A, 2)
    JNQ = (0x0B, 2)

    def __eq__(self, other):
        return self.value[0] == other


instruction_set = {d.name: d.value for d in Instruction}
bytecode_set = {d.value[0]: d.value[1] for d in Instruction}
