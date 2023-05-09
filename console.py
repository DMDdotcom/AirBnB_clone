#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """ A class that defines the main console/ command line interprrreter"""
    prompt = "command_input "
    
    def do_author(self, line):
        """prints the author"""
        print("hello, this shell was written by damilola")

    def do_exit(self, line):
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()

