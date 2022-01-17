from vm import StackMachine

if __name__ == "__main__":
    machine = StackMachine()
    machine.load("../scratch/my_bytecode_script.byc")
    machine.run()
