from lib.decorator import shell_command
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
    @shell_command
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



