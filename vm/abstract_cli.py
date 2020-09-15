import click
from vm.compiler import compile_script
from vm import StackMachine


@click.group()
def cli():
    ...


@cli.command("run")
@click.argument('bytecode_file', type=click.Path())
def run_bytecode_file(bytecode_file):
    """Run bytecode file"""
    with open(bytecode_file, "rb") as f:
        byte_code = bytearray(f.read())
    StackMachine().load(byte_code).run()


@cli.command("compile")
@click.argument('script_file', type=click.Path())
def compile_script(script_file):
    """Compile script"""
    compile_script(script_file)


if __name__ == "__main__":
    cli()
