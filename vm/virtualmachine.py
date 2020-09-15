from abc import ABC
from typing import List
from sys import maxsize


class VM(ABC):

    def __init__(self):
        self._stack: List[int] = []
        self._stack_size = 0
        self._MAX_STACK_SIZE = maxsize
        self._program_counter = 0
        self._byte_code = None

    def load(self, byte_code: bytearray):
        self._byte_code = byte_code
        return self

    def pop(self):
        raise NotImplementedError

    def push(self, value):
        raise NotImplementedError

    def peek(self):
        raise NotImplementedError

    def set_pc(self, value):
        self._program_counter = value

    def advance_pc(self, value):
        self._program_counter += value

    def get_bytecode_at_address(self, address, offset: int = 0):
        return self._byte_code[address + offset]

    def get_pc(self):
        return self._program_counter
