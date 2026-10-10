
from datetime import datetime
from collections import Counter

filename = "server.log"

total_lines = 0
level_count = Counter()
errors_per_hour = Counter()
error_messages = Counter()

with open(filename, "r") as file:
    for line in file:
        line = line.strip()

        if not line:
            continue

        try:
            parts = line.split(" ", 2)

            timestamp = datetime.strptime(
                parts[0] + " " + parts[1],
                "%Y-%m-%d %H:%M:%S"
            )

            level = parts[2].split(" ", 1)[0]
            message = parts[2].split(" ", 1)[1]

            total_lines += 1
            level_count[level] += 1

            if level == "ERROR":
                errors_per_hour[timestamp.strftime("%Y-%m-%d %H:00")] += 1
                error_messages[message] += 1

        except (ValueError, IndexError):
            print("Skipping invalid log entry:", line)

with open("summary.txt", "w") as report:
    report.write("SERVER LOG REPORT\n")
    report.write("=================\n\n")

    report.write(f"Total lines: {total_lines}\n\n")

    report.write("Count by log level:\n")
    for level, count in sorted(level_count.items()):
        report.write(f"{level}: {count}\n")

    report.write("\nErrors per hour:\n")
    for hour, count in sorted(errors_per_hour.items()):
        report.write(f"{hour}: {count}\n")

    report.write("\nTop 5 frequent error messages:\n")
    for message, count in error_messages.most_common(5):
        report.write(f"{message}: {count}\n")

print("Report generated successfully: summary.txt")
