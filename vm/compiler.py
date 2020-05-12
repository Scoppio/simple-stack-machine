from vm import instruction_set, Instruction


def compile_script(file_path):
    """

    :param file_path: 
    :return:
    """
    bytecode = bytearray()
    with open(file_path, 'r') as f:
        data = f.read().split("\n")
    print("first pass, cleaning file")
    _datum = []
    for line in data:
        if line:
            if "#" in line:
                if len(code := line.split("#")) == 2:
                    _datum.append(code)
            else:
                _datum.append(line)
    data = _datum
    markers = {}
    to_jump = {}
    pc = 0
    print("second pass, bytecode and jump markers")
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
            for i in range(instruction_set[op][1]-1):
                bytecode.append(int(line[i+1]))

    print("this pass, placing the correct jump markers on bytecode")
    for n, code in enumerate(bytecode):
        if n in to_jump:
            bytecode[n-1] = markers[to_jump[n]]

    output_file = file_path.replace(".lsc", ".byc")

    print("saving bytecode to file")
    with open(output_file, 'wb') as f:
        f.write(bytecode)


if __name__ == "__main__":
    compile_script("../scratch/my_bytecode_script.lsc")
    print("compilation done")
