from vm import instruction_set, Instruction


def compile_script(file_path):
    """

    :param file_path: 
    :return:
    """
    with open(file_path, 'r') as f:
        data = f.read().split("\n")
    bytecode = compile_to_bytecode(data)
    output_file = file_path.replace(".lsc", ".byc")
    print("saving bytecode to file")
    with open(output_file, 'wb') as f:
        f.write(bytecode)


def compile_to_bytecode(data):

    print("first pass, cleaning file")
    data = remove_commentary(data)

    bytecode = bytearray()
    markers = dict()
    to_jump = dict()

    print("second pass, bytecode and jump markers")
    bytecode_and_jump_markers(bytecode, data, markers, to_jump)

    print("this pass, placing the correct jump markers on bytecode")
    jump_markers(bytecode, markers, to_jump)
    return bytecode


def jump_markers(bytecode, markers, to_jump):
    for n, code in enumerate(bytecode):
        if n in to_jump:
            bytecode[n - 1] = markers[to_jump[n]]


def bytecode_and_jump_markers(bytecode, data, markers, to_jump):
    pc = 0
    for line in data:
        line = line.split(" ")
        line = [a for a in filter(lambda x: x, line)]
        op = line[0]
        if ":" in op:
            markers[op[:-1]] = pc
            continue
        else:
            pc += instruction_set[op][1]
        bytecode.append(instruction_set[op][0])
        if instruction_set[op][0] == Instruction.JEQ or instruction_set[op][0] == Instruction.JNQ:
            bytecode.append(0)
            to_jump[pc] = line[1]
        elif instruction_set[op][1] > 1:
            for i in range(instruction_set[op][1] - 1):
                bytecode.append(int(line[i + 1]))


def remove_commentary(data):
    _datum = []
    for line in data:
        if line:
            if "#" in line:
                if len(code := line.split("#")) == 2:
                    _datum.append(code)
            else:
                _datum.append(line)
    data = _datum
    return data


if __name__ == "__main__":
    compile_script("../scratch/my_bytecode_script.lsc")
    print("compilation done")
