from lib.decorator import shell_command
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
    @staticmethod
    def ping(argip):
        stream = os.popen('ping -c 4 {}'.format(argip))
        output = stream.read()
        print(output)

    @shell_command
    def do_ping(self, arg):
        self.ping(arg)

