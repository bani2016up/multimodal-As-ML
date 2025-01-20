

from collections.abc import Callable
import os
from typing import NoReturn
from functools import wraps


def check_decorator(cls):
    for name, method in cls.__dict__.items():
        if callable(method) and name not in ['check', '__init__']:
            setattr(cls, name, cls.check_wrapper(method))
    return cls

class Commands:
    def __init__(self, base_dir: str) -> None:
        self.base_dir = os.path.abspath(base_dir)
        self.dir = self.base_dir

    @staticmethod
    def check(dir: str, t_fun: Callable, *t_args, **t_kwargs) -> NoReturn | None:
        if not dir.startswith("/Users/daniilparfenov/Documents/software/multy-modal/multimodal-As-ML/lumina_worckspace"):
            raise ValueError("Cannot access directory outside of the allowed workspace")
        return t_fun(*t_args, **t_kwargs)

    @classmethod
    def check_wrapper(cls, method):
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            return cls.check(self.dir, method, self, *args, **kwargs)
        return wrapper

    def final_path(self, extend: str) -> str:
        return f"{self.dir}/{extend}"

    def ls(self) -> list[str]:
        return os.listdir(self.dir)

    def tree(self) -> str:
        return os.popen(f"tree {self.dir}").read()

    def mkdir(self, dir_name: str) -> None:
        new_dir = self.final_path(dir_name)
        os.mkdir(new_dir)

    def rmdir(self, dir_name: str) -> None:
        dir_to_remove = self.final_path(dir_name)
        os.rmdir(dir_to_remove)

    def touch(self, filename: str) -> None:
        file_path = self.final_path(filename)
        with open(file_path, "w") as f:
            pass

    def rm(self, file_path: str) -> None:
        os.remove(file_path)

    def edit(self, filename: str, content: str) -> None:
        file_path = self.final_path(filename)
        with open(file_path, "w") as f:
            f.write(content)

    def cat(self, filename: str) -> str:
        file_path = self.final_path(filename)
        with open(file_path, "r") as f:
            return f.read()

    def run(self, filename: str) -> None:
        file_path = self.final_path(filename)
        os.system(file_path)

    def cd(self, path: str) -> None:
        if path == "..":
            new_dir = os.path.dirname(self.dir)
        else:
            new_dir = os.path.abspath(self.final_path(path))

        if not new_dir.startswith(self.base_dir):
            raise ValueError("Cannot navigate outside of the base directory")

        self.dir = new_dir

if __name__ == "__main__":
    pc = Commands("/Users/daniilparfenov/Documents/software/multy-modal/multimodal-As-ML/lumina_worckspace")
    print(pc.ls())
