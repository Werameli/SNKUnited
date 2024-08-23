from lib.decorator import shell_command, help_section
import os

class PlugInfo:
    def __init__(self, shell_instance):
        self.shell_instance = shell_instance

    @staticmethod
    def SNKInit():
        return {
            "name": "Pinger",
            "vendor": "Werameli",
            "version": "Release 1.0",
            "description": "Simple 'ping' command analog in SNK"
        }


class ShellIntegrations:
    # help_texts = {}
    #
    # def __init__(self):
    #     for attr_name in dir(self):
    #         attr = getattr(self, attr_name)
    #         if callable(attr) and hasattr(attr, '_is_shell_command'):
    #             if hasattr(attr, '__help_text'):
    #                 self.__class__.help_texts[attr_name] = attr.__help_text
    #
    # def do_help(self, args):
    #     for command, description in self.__class__.help_texts.items():
    #         print(f"{command}: {description}")
    @staticmethod
    def ping(argip):
        stream = os.popen('ping -c 4 {}'.format(argip))
        output = stream.read()
        print(output)

    @shell_command
    @help_section("print test output. Usage: ping <host>")
    def do_ping(self, arg):
        self.ping(arg)

