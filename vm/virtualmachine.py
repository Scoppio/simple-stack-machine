from abc import ABC
from typing import List, Optional
from sys import maxsize
import tarfile
from pathlib import Path


class VM(ABC):

    def __init__(self):
        self._stack: List[int] = []
        self._stack_size: int = 0
        self._MAX_STACK_SIZE: int = maxsize
        self._program_counter: int = 0
        self._byte_code: Optional[bytearray] = None
        self._data_block: Optional[bytes] = None

    def load(self, address: str):
        code = bytearray
        data = list()
        with tarfile.open(address) as tar:
            for member in tar.getmembers():
                member_name = Path(member.name).name
                ext = tar.extractfile(member.name)
                if member_name == 'code':
                    code = bytearray(ext.read())
                elif member_name == 'data':
                    data = ext.readlines()

        self._data_block: List[bytes] = data
        self._byte_code = code

        return self

    def pop(self):
        raise NotImplementedError

    def push(self, value):
        raise NotImplementedError

    def peek(self):
        raise NotImplementedError

    def get_data_at(self, address: int) -> bytes:
        return self._data_block[address]

    def set_pc(self, value):
        self._program_counter = value

    def advance_pc(self, value):
        self._program_counter += value

    def get_bytecode_at_address(self, address, offset: int = 0) -> int:
        return self._byte_code[address + offset]

    def get_pc(self):
        return self._program_counter
