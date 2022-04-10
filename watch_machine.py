import os
import re
from typing import List
from config import Machine, machine_list

# Temperature, Utilization, Used/Total Memory
pattern_tcut = re.compile("\n(.*?)\|(\d+?)'C,(\d+?)%\|(\d+?)/(\d+?)MB\|")


def default_when_idle(**args):
    print(f"{args['gpu']}")


class Info:
    def __init__(
        self,
        name="Test",
        GPU="gpu0",
        temperature=66,
        utilization=100,
        used_memory=11905,
        total_memory=16280,
    ) -> None:
        self.name = name
        self.GPU = GPU
        self.temperature = temperature
        self.utilization = utilization
        self.used_memory = used_memory
        self.total_memory = total_memory


def process_info(info: Info):
    (
        name,
        gpu,
        temperature,
        utilization,
        used_memory,
        total_memory,
    ) = info.__dict__.values()
    subject = "Machine idle " + name
    info = f"GPU:{gpu}, temperature:{temperature}, utilization:{utilization}, used_memory:{used_memory}, total_memory:{total_memory}"
    print(f"{subject}:\n {info}")
    return subject, info


def watch_machine(
    machines: List[Machine] = machine_list,
    when_idle=process_info,
) -> bool:
    for machine in machines:
        status = os.popen(machine.check_cmd).read().replace(" ", "")
        print(status)
        GPU_status = pattern_tcut.findall(status)
        for gpu, temperature, utilization, used_memory, total_memory in GPU_status:
            # 判断其实也不该在本函数实现
            if int(utilization) < 10 or int(used_memory) / int(total_memory) < 0.1:
                # '''
                # Traceback (most recent call last):
                #     TypeError: default_when_idle() takes 0 positional arguments but 6 were given
                # '''
                # when_idle(
                #     name, gpu, temperature, utilization, used_memory, total_memory, info
                # )

                when_idle(
                    Info(
                        machine.name,
                        gpu,
                        temperature,
                        utilization,
                        used_memory,
                        total_memory,
                    )
                )
                return True
    return False


if __name__ == "__main__":
    default_when_idle(
        gpu="gpu",
        temperature=66,
        utilization=100,
        used_memory=11905,
        total_memory=16280,
    )  # Success
    watch_machine()
