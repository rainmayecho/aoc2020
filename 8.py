from util import readfile
import re

DAY = 8

LINE_REGEX = re.compile(r"(.*) ([\+-])(\d+)")

accumulator = 0
ip = 0


def acc(v):
    global accumulator
    global ip
    accumulator += v
    ip += 1


def jmp(offset):
    global ip
    ip += offset


def nop(*args):
    global ip
    ip += 1


F = {"acc": acc, "jmp": jmp, "nop": nop}


def solve_1(data):
    global ip
    global accumulator
    instructions = []
    for line in data:
        instr, sign, val = LINE_REGEX.findall(line)[0]
        val = int(val) * (1 if sign == "+" else -1)
        instructions.append((instr, val))

    seen, last = set(), None
    while True:
        instr, val = instructions[ip]
        if ip in seen:
            print(last)
            break
        seen.add(ip)
        F[instr](val)
        last = accumulator

    for i, (instr, val) in enumerate(instructions):
        ip, accumulator = 0, 0
        seen, last = set(), None
        if instr in ("jmp", "nop"):
            _instructions = list(instructions)
            _instructions[i] = (
                ("jmp", val) if instructions[i] == "nop" else ("nop", val)
            )

            while True:
                if ip >= len(_instructions):
                    return last
                instr, val = _instructions[ip]
                if ip in seen:
                    break
                seen.add(ip)
                F[instr](val)
                last = accumulator


if __name__ == "__main__":
    with open(f"{DAY}.in", "r") as f:
        data = [line.rstrip() for line in f]
        print(solve_1(data))
