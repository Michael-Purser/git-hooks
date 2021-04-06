#!/usr/bin/python3


from colorama import Fore, Style
from enum import IntFlag


class GitHookExitCode(IntFlag):
    Success = 0
    Failure = 1
    Aborted = 2


class GitHookLogger:
    _instance = None
    _name = None

    def __new__(cls, name):
        if cls._name is None:
            cls._instance = super(GitHookLogger, cls).__new__(cls)
            cls._name = name
        return cls._instance

    def info(self, message=""):
        print("[" + self._name + "] " + Fore.BLUE + "[INFO] " + Style.RESET_ALL + message)

    def fail(self, message=""):
        print("[" + self._name + "] " + Fore.RED + "[FAILED] " + Style.RESET_ALL + message)

    def success(self, message=""):
        print("[" + self._name + "] " + Fore.GREEN + "[SUCCESS] " + Style.RESET_ALL + message)
