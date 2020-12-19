from util import readfile
import re

DAY = 19


def solve_1(data):
    rule_map = {}
    start = 0
    for i, line in enumerate(data):
        if ":" in line:
            n, info = line.split(": ")
            info = info.replace('"', "")
            if "|" in info:
                l, r = [p.split(" ") for p in info.split(" | ")]
                rule_map[n] = [l, r]
            elif info in ("a", "b"):
                rule_map[n] = info
            else:
                rule_map[n] = info.split(" ")
        elif not line:
            start = i
            break

    memo = {}

    def prepare(r):
        nonlocal rule_map
        rule = rule_map[r]
        if isinstance(rule, str):
            return rule
        if len(rule) == 2 and isinstance(rule[0], list):
            x = []
            for rule_pair in rule:
                y = []
                if not isinstance(rule_pair, list):
                    rule_pair = [rule_pair]
                for _r in rule_pair:
                    memo[_r] = memo.get(_r) or prepare(_r)
                    y.append(memo[_r])
                x.append(f"({''.join(y)})")
            return f'({"|".join(v for v in x)})'
        else:
            return "".join(prepare(_r) for _r in rule)

    MESSAGE_REGEX = re.compile(f'^{prepare("0")}$')
    print(sum(int(MESSAGE_REGEX.match(msg) is not None) for msg in data[start:]))

    c = prepare("42")
    d = prepare("31")
    rule_map["8"] = f"({c})+"
    rule_map[
        "11"
    ] = f"({c}{d}|{c}{c}{d}{d}|{c}{c}{c}{d}{d}{d}|{c}{c}{c}{c}{d}{d}{d}{d})"  # lol
    pattern = f'^{prepare("0")}$'
    MESSAGE_REGEX = re.compile(pattern)
    print(sum(int(MESSAGE_REGEX.match(msg) is not None) for msg in data[start:]))


def solve_2(data):
    pass


if __name__ == "__main__":
    with open(f"{DAY}.in", "r") as f:
        data = [line.rstrip() for line in f]
        solve_1(data)
