from typing import List, Union

from order.command.command import Command
from order.command.undoable import Undoable


class CommandManager:
    """manage commands"""
    def __init__(self):
        self.__undo_commands: List[Union[Command, Undoable]] = list()

    def execute(self, command: Command):
        """execute the command"""
        result = command.execute()
        self.__undo_commands.append(command)
        return result

    def clear(self):
        """clear up all saved commands"""
        self.__undo_commands.clear()

    def undo(self, times: int = 1):
        """undo the previous [times] command(s)"""
        for i in range(times):
            command = self.__undo_commands.pop()
            command.undo()

    @property
    def undo_commands_size(self):
        """get number of undo commands"""
        return len(self.__undo_commands)
