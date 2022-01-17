from vm import instruction_set, Instruction
from typing import List
import tarfile
import os
from pathlib import Path


def compile_script(file_path):
    """

    :param file_path: 
    :return:
    """
    with open(file_path, 'r') as f:
        data = f.read().split("\n")
    bytecode, datablock = compile_to_bytecode(data)

    parent_dir = Path(file_path).parent
    output_file = os.path.join(parent_dir, 'code')
    output_data_file = os.path.join(parent_dir, 'data')

    print("saving bytecode to file")
    with open(output_file, 'wb') as f:
        f.write(bytecode)

    with open(output_data_file, 'w') as f:
        f.writelines(datablock)

    final_file = file_path.replace(".lsc", ".byc")
    with tarfile.open(final_file, "w") as tar:
        tar.add(output_data_file)
        tar.add(output_file)

    os.remove(output_data_file)
    os.remove(output_file)


def compile_to_bytecode(data):

    print("first pass, cleaning file")
    data = remove_commentary(data)

    bytecode = bytearray()
    markers = dict()
    to_jump = dict()
    datablock = list()

    print("second pass, bytecode and jump markers")
    bytecode_and_jump_markers(bytecode, data, markers, to_jump, datablock)

    print("this pass, placing the correct jump markers on bytecode")
    jump_markers(bytecode, markers, to_jump)
    return bytecode, datablock


def jump_markers(bytecode, markers, to_jump):
    for n, code in enumerate(bytecode):
        if n in to_jump:
            bytecode[n - 1] = markers[to_jump[n]]


def bytecode_and_jump_markers(bytecode, data, markers, to_jump, datablock: List):
    pc = 0
    for line in data:
        try:
            line = line.split(" ")
            line = [a for a in filter(lambda x: x, line)]
            if line is None or not len(line):
                continue
            op = line[0]
        except (AttributeError, IndexError) as e:
            print(line)
            raise e

        if ":" in op:
            markers[op[:-1]] = pc
            continue
        else:
            pc += instruction_set[op][1]

        instruction = instruction_set[op]
        bytecode.append(instruction[0])
        if instruction[0] in (Instruction.JEQ, Instruction.JNQ):
            bytecode.append(0)
            to_jump[pc] = line[1]
        elif instruction[0] == Instruction.API_CALL:
            v = len(datablock)
            datablock.append(line[1])
            bytecode.append(v)

            bytecode.append(int(line[2]))

        elif instruction[1] > 1:
            for i in range(instruction[1] - 1):
                bytecode.append(int(line[i + 1]))


def remove_commentary(data):
    _datum = []
    for line in data:
        if line:
            if "#" in line:
                code = line.split("#")
                if len(code) == 2:
                    _datum.append(code[0])
            else:
                _datum.append(line)
    data = _datum
    return data


if __name__ == "__main__":
    compile_script("../scratch/my_bytecode_script.lsc")
    print("compilation done")
