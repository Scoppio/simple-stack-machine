from vm import StackMachine

if __name__ == "__main__":
    with open("../scratch/object_file.byc", 'rb') as f:
        byte_code = bytearray(f.read())

    machine = StackMachine()
    machine.load(byte_code)
    machine.run()
