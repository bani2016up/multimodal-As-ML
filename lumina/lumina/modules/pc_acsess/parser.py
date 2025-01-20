import re
from typing import List, Tuple, Any, Callable
from functools import partial

class CommandParser:
    def __init__(self, pc_instance):
        self.pc = pc_instance
        self.commands = {
            'googleIt': self.google_it,
            'ls': self.pc.ls,
            'cd': self.pc.cd,
            'tree': self.pc.tree,
            'mkdir': self.pc.mkdir,
            'rmdir': self.pc.rmdir,
            'touch': self.pc.touch,
            'rm': self.pc.rm,
            'edit': self.pc.edit,
            'cat': self.pc.cat,
            'run': self.pc.run
        }

    def google_it(self, query: str) -> str:
        # This is a placeholder. You'll need to implement actual Google search functionality.
        return f"Googling: {query}"

    def parse_command(self, command: str) -> Tuple[Callable, List[Any]]:
        match = re.match(r'(\w+)(?:\s+\[(.*?)\])?(?:\s*->\s*.*)?$', command)
        if not match:
            raise ValueError(f"Invalid command format: {command}")

        cmd_name, args_str = match.groups()
        if cmd_name not in self.commands:
            raise ValueError(f"Unknown command: {cmd_name}")

        args = [arg.strip() for arg in args_str.split(',')] if args_str else []
        return self.commands[cmd_name], args

    def execute_command(self, command: str) -> Any:
        func, args = self.parse_command(command)
        return func(*args)

    def execute_commands(self, commands: List[str]) -> List[Any]:
        return [self.execute_command(cmd) for cmd in commands]

# Example usage:
if __name__ == "__main__":
    from lumina.modules.pc_acsess.main import PC

    base_dir = "/Users/daniilparfenov/Documents/software/multy-modal/multimodal-As-ML/lumina_worckspace"
    pc = PC(base_dir)
    parser = CommandParser(pc)

    # Test commands
    test_commands = [
        "ls",
        "mkdir [test_dir]",
        "cd [test_dir]",
        "touch [test_file.txt]",
        "edit [test_file.txt, Hello, World!]",
        "cat [test_file.txt]",
        "tree",
        "cd [..]",
        "rmdir [test_dir]",
        "googleIt [Python programming]"
    ]

    for cmd in test_commands:
        try:
            result = parser.execute_command(cmd)
            print(f"Command: {cmd}")
            print(f"Result: {result}")
            print()
        except Exception as e:
            print(f"Error executing '{cmd}': {str(e)}")
            print()
