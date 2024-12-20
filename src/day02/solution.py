from typing import Iterator

with open("input.txt", "r") as f:
    lines = f.readlines()

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
            elif direction == "up":
                return False
        else:
            if direction is None:
                direction = "up"
            elif direction == "down":
                return False
    return True

def part_01_solution(reports: list[str]) -> int:
    safe_reports = 0
    for report in reports:
        if report_is_safe(report):
            safe_reports += 1
    return safe_reports

def alt_reports(_report: str) -> Iterator[str]:
    levels = [int(x) for x in _report.split()]
    for i in range(len(levels)):
        yield " ".join([str(levels[j]) for j in range(len(levels)) if j != i])

def part_02_solution(reports: list[str]) -> int:
    safe_reports = 0
    for report in reports:
        if report_is_safe(report):
            safe_reports += 1
        elif any(report_is_safe(x) for x in alt_reports(report)):
            safe_reports += 1
    return safe_reports

print("Part 1 Answer:", part_01_solution(lines))
print("Part 2 Answer:", part_02_solution(lines))
