from vm import Instruction, bytecode_set
from typing import List, Union


class StackMachine:
    _stack: List[int] = []
    _stack_size = 0
    _MAX_STACK_SIZE = 256

    def __init__(self):
        pass

    def _push(self, value: Union[int, float]) -> None:
        assert self._stack_size < self._MAX_STACK_SIZE
        self._stack_size += 1
        self._stack.append(value)

    def _pop(self) -> Union[int, float]:
        assert self._stack_size > 0
        self._stack_size -= 1
        value = self._stack.pop(self._stack_size)
        return value

    def _peek(self) -> Union[int, float]:
        assert self._stack_size > 0
        value = self._stack[self._stack_size-1]
        return value

    def run(self, byte_code: bytearray):
        _program_counter = 0
        while _program_counter < len(byte_code):
            op = byte_code[_program_counter]
            if op == Instruction.NOP:
                pass
            elif op == Instruction.ADD:
                b, a = self._pop(), self._pop()
                self._push(a + b)
            elif op == Instruction.DIV:
                b, a = self._pop(), self._pop()
                self._push(int(a / b))
            elif op == Instruction.MUL:
                b, a = self._pop(), self._pop()
                self._push(a * b)
            elif op == Instruction.SUB:
                b, a = self._pop(), self._pop()
                self._push(a + b)
            elif op == Instruction.VAR:
                self._push(byte_code[_program_counter + 1])
            elif op == Instruction.API_1:
                print(self._peek())
            elif op == Instruction.AND:
                b, a = self._pop(), self._pop()
                self._push(a & b)
            elif op == Instruction.OR:
                b, a = self._pop(), self._pop()
                self._push(a | b)
            elif op == Instruction.XOR:
                b, a = self._pop(), self._pop()
                self._push(a ^ b)
            elif op == Instruction.JEQ:
                if self._peek() == 0:
                    _program_counter = byte_code[_program_counter + 1] - 2
            elif op == Instruction.JNQ:
                if self._peek() != 0:
                    _program_counter = byte_code[_program_counter + 1] - 2
            _program_counter += bytecode_set[op]


if __name__ == "__main__":
    with open("object_file.byc", 'rb') as f:
        byte_code = bytearray(f.read())

    StackMachine().run(byte_code)
