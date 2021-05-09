import nmap3 # type: ignore
from typing import Dict
import argparse


class Scanner(object):
   def __init__(self, /) -> None:
      hostname: str = self.get_arguments()
      result = self.scan(hostname)
      for line in result:
         print(str(result[line]) + "\n")


   def scan(self, host: str, /) -> Dict:
      nmap = nmap3.Nmap()
      return nmap.scan_top_ports(host)


   def get_arguments(self, /) -> str:
      parser = argparse.ArgumentParser()
      parser.add_argument("--host", help="Hostname from your victim.")
      options = parser.parse_args()
      if not options.host:
         options.host = str(input("[+] Hostname: "))
      return options.host


if __name__ == "__main__":
   s = Scanner()