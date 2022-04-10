from typing import List


class smtp_config:
    sender_address = "lprintf@lprintf.com"
    relay_host_name = "smtp.lprintf.com"
    relay_host_port = 587
    relay_auth = True
    relay_auth_username = "lprintf@lprintf.com"
    relay_auth_password = "ABCDEFGHIJKLMN"

    receivers = ["lprintf@lprintf.com"]


class Machine:
    def __init__(self, name, check_cmd) -> None:
        self.name = name
        self.check_cmd = check_cmd

machine_list: List[Machine]=[
    Machine("P200_0", "ssh root@1.2.3.4 -p 1000 /opt/conda/bin/gpustat -cpu"),
    Machine("titanX", "ssh lyj@58.199.1.1 -p 8888 gpustat -cpu"),
]