from enum import Enum
from vm import VM
from typing import Dict


def _nop(*args, **kwargs):
    ...


def _add(sm: VM):
    b, a = sm.pop(), sm.pop()
    sm.push(a + b)


def _div(sm: VM):
    b, a = sm.pop(), sm.pop()
    sm.push(int(a / b))


def _mul(sm: VM):
    b, a = sm.pop(), sm.pop()
    sm.push(a * b)


def _sub(sm: VM):
    b, a = sm.pop(), sm.pop()
    sm.push(a + b)


def _var(sm: VM):
    sm.push(sm.get_bytecode_at_address(address=sm.get_pc(), offset=1))


def _and(sm: VM):
    b, a = sm.pop(), sm.pop()
    sm.push(a & b)


def _or(sm: VM):
    b, a = sm.pop(), sm.pop()
    sm.push(a | b)


def _xor(sm: VM):
    b, a = sm.pop(), sm.pop()
    sm.push(a ^ b)


def _jeq(sm: VM):
    if sm.peek() == 0:
        sm.set_pc(sm.get_bytecode_at_address(address=sm.get_pc(), offset=1) - 2)


def _jnq(sm: VM):
    if sm.peek() != 0:
        sm.set_pc(sm.get_bytecode_at_address(address=sm.get_pc(), offset=1) - 2)


def _api_1(sm: VM):
    print(sm.peek())


class Instruction(Enum):
    """
    Instruction

    The instruction is divided in 3 parts, first is the mnemonic, second part is the bytecode value for that
    instruction, the third value is the number of steps required to execute the instruction.
    Example:
        NOP = (0x00, 1, _nop)
        No operation: Mnemonic NOP, code is 0, the number of steps the program counter will take is 1.
        VAR = (0x05, 2, _var)
        Variable: Mnemonic VAR, code is 5, the number of steps the program counter will take is 2.
    """
    NOP = (0x00, 1, _nop)
    ADD = (0x01, 1, _add)
    SUB = (0x02, 1, _sub)
    DIV = (0x03, 1, _div)
    MUL = (0x04, 1, _mul)
    VAR = (0x05, 2, _var)
    API_1 = (0X06, 1, _api_1)
    AND = (0x07, 1, _and)
    XOR = (0x08, 1, _xor)
    OR = (0x09, 1, _or)
    JEQ = (0x0A, 2, _jeq)
    JNQ = (0x0B, 2, _jnq)

    def __eq__(self, other):
        return self.value[0] == other

    def execute(self, sm: VM):
        self.value[2](sm)

    def get_bytecode(self):
        return self.value[0]

    def step_count(self):
        return self.value[1]


# Instruction map using the bytecode definition
byte_to_instruction: Dict[int, Instruction] = {d.value[0]: d for d in Instruction}

# Instruction execution map
instruction_execution = {d.value[0]: d.value[2] for d in Instruction}

# Instruction map using name definition
instruction_set = {d.name: d.value for d in Instruction}

# Instruction set for execution time
bytecode_set = {d.value[0]: d.value[1] for d in Instruction}
