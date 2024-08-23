from lib.decorator import shell_command, help_section
import socket
import time

class PlugInfo:
    def __init__(self, shell_instance):
        self.shell_instance = shell_instance

    @staticmethod
    def SNKInit():
        return {
            "name": "PortScanner",
            "vendor": "Werameli",
            "version": "Release 1.0",
            "description": "As it is, simple port scanner for SNK"
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

    @shell_command
    @help_section("Scan IP address for opened ports. Usage: portscan")
    def do_portscan(self, arg):
        self.startscan()

    @staticmethod
    def tcp_scan(ip, startPort, endPort):
        for port in range(startPort, endPort + 1):
            try:
                tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                if not tcp.connect_ex((ip, port)):
                    print('[+] %s:%d/TCP Open' % (ip, port))
                    tcp.close()
                    time.sleep(2)

            except socket.error:
                pass

    def scanHost(self, ip, startPort, endPort):
        print('[*] Starting TCP port scan on host %s' % ip)

        self.tcp_scan(ip, startPort, endPort)

        print('[=] TCP scan on host %s complete' % ip)

    def startscan(self):
        network = input("Input IP: ")
        startPort = int(input("Input start port (range start): "))
        endPort = int(input("Input end port (range end): "))

        self.scanHost(network, startPort, endPort)



