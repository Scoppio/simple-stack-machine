from typing import Union
from vm import byte_to_instruction, VM


class StackMachine(VM):

    def __init__(self):
        super().__init__()

    def push(self, value: Union[int, float]) -> None:
        assert self._stack_size < self._MAX_STACK_SIZE
        self._stack_size += 1
        self._stack.append(value)

    def pop(self) -> Union[int, float]:
        assert self._stack_size > 0
        self._stack_size -= 1
        value = self._stack.pop(self._stack_size)
        return value

    def peek(self) -> Union[int, float]:
        assert self._stack_size > 0
        value = self._stack[self._stack_size - 1]
        return value

    def run(self, byte_code: bytearray = None):
        if byte_code:
            self._byte_code = byte_code

        self.set_pc(0)
        while self._program_counter < len(self._byte_code):
            code = self.get_bytecode_at_address(self.get_pc())
            operation = byte_to_instruction[code]
            operation.execute(self)
            self.advance_pc(operation.step_count())
