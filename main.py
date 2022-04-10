from time import sleep
from send_email import send_email, make_message
from watch_machine import Info, watch_machine, process_info


def when_idle(info: Info):
    subject, content = process_info(info)
    send_email(message=make_message(subject, content, "lprintf", "lprintf"))


if __name__ == "__main__":
    while True:
        if not watch_machine(when_idle=when_idle):
            print("No idle machine found, keep waiting...")
            sleep(60*10)
        else:
            break
        
