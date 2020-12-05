from util import readfile

DAY = 5

test = [
    "FBFBBFFRLR",
    "BFFFBBFRRR",
    "FFFBBBFRRR",
    "BBFFBBFRLL"
]

def solve_1(data):
    best, pairs = 0, []
    for ticket in data:
        rd, sd = ticket[:7], ticket[7:]
        l, r = 0, 127
        for c in rd:
            mid = (l + r) // 2
            if c == "F":
                r = mid
            else:
                l = mid
        row = r
        ll, rr = 0, 7
        for c in sd:
            mid = (ll + rr) // 2
            if c == "L":
                rr = mid
            else:
                ll = mid
        col = rr
        sid = row * 8 + col
        pairs.append((row, col))
        best = max(best, sid)
    return best, pairs

make_seat_id = lambda p: p[0] * 8 + p[1]

def solve_2(rc_pairs):
    rc_pairs.sort()
    first = rc_pairs[0]
    prev = (first[0], first[1], make_seat_id(first))
    for p in rc_pairs[1:]:
        sid = make_seat_id(p)
        pr, pc, ps = prev
        if pr == p[0] and sid > ps+1:
            return sid-1
        prev = (p[0], p[1], sid)


if __name__ == "__main__":
    with open(f"{DAY}.in", "r") as f:
        data = list(readfile(f, mapper = lambda x: x[0].rstrip()))
        best, pairs = solve_1(data)
        print(best)
        print(solve_2(pairs))