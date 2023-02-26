import re


def load_inc_file(filename):
    """load the register and config word definitions from .inc file and build a dict"""

    with open(filename) as fp:
        reg = {}
        coms = {}
        for line in fp:
            # STATUS EQU  H'0003'
            if line.startswith(";-"):
                comment = ""
                comment_found = False
                for charac in line[2:]:
                    if charac == "-":
                        if comment_found:
                            break
                        continue
                    comment_found = True
                    comment += charac
                coms[len(reg)] = comment.strip()
            m = re.search("(?i)^(\S+)\s+EQU\s+H'(\S+)'", line.strip())
            if m:
                name, value = m.groups()
                reg[name] = int(value, 16)

    return reg, coms


registers, comments = load_inc_file("p10f320.inc")
with open("p10f320.py", "w") as fp:
    count = 0
    for name, value in registers.items():
        if comments.get(count) is not None:
            fp.write(f"\n# ============== {comments[count]} ==============\n\n")
        fp.write(f"{name} = const(0x{value:04x})\n")
        count += 1
