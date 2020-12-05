from util import readfile

DAY = 5

test = ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]


def solve_1(data):
    best, sids = 0, []
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
        sids.append(sid)
        best = max(best, sid)
    return best, sids


make_seat_id = lambda p: p[0] * 8 + p[1]


def solve_2(sids):
    sids.sort()
    prev = sids[0]
    for sid in sids[1:]:
        if (sid - prev) > 1:
            return sid - 1
        prev = sid


if __name__ == "__main__":
    with open(f"{DAY}.in", "r") as f:
        data = list(readfile(f, mapper=lambda x: x[0].rstrip()))
        best, sids = solve_1(data)
        print(best)
        print(solve_2(sids))
