with open("input.txt", "r") as f:
    lines = f.readlines()

safe_reports = 0

def report_is_safe(_report: str) -> bool:
    levels = [int(x) for x in _report.split()]
    direction: str | None = None
    for i in range(1, len(levels)):
        delta = levels[i] - levels[i-1]
        if abs(delta) <= 0 or abs(delta) > 3:
            return False
        if delta < 0:
            if direction is None:
                direction = "down"
                continue
            if direction == "up":
                return False
            continue
        else:
            if direction is None:
                direction = "up"
                continue
            if direction == "down":
                return False
            continue
    return True


for report in lines:
    if report_is_safe(report):
        safe_reports += 1

print(safe_reports)
