import time
import psutil
from datetime import datetime
import os


def fmt_bytes(n):
    for unit in ('B','KB','MB','GB','TB'):
        if n < 1024:
            return f"{n:.2f} {unit}"
        n /= 1024
    return f"{n:.2f} PB"


def sample(interval=1.0):
    # загрузка CPU за интервал (процент суммарно)
    cpu_percent = psutil.cpu_percent(interval=interval)
    # загрузка CPU по логическим ядрам (немедленно, last interval)
    per_cpu = psutil.cpu_percent(interval=0, percpu=True)
    # память
    vm = psutil.virtual_memory()
    total = vm.total
    available = vm.available
    used = total - available
    used_percent = vm.percent

    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {
        "timestamp": ts,
        "cpu_percent": cpu_percent,
        "per_cpu": per_cpu,
        "mem_total": total,
        "mem_used": used,
        "mem_available": available,
        "mem_used_percent": used_percent,
    }


def print_sample(s):
    print(f"[{s['timestamp']}] CPU: {s['cpu_percent']:.1f}% (per-core: {', '.join(f'{p:.1f}%' for p in s['per_cpu'])})")
    print(f"  RAM: {s['mem_used_percent']:.1f}% — {fmt_bytes(s['mem_used'])} used / {fmt_bytes(s['mem_total'])} total\n")

def monitor(duration=30, interval=1.0):
    end = time.time() + duration
    while time.time() < end:
        s = sample(interval=interval)
        os.system('cls')
        print_sample(s)


if __name__ == "__main__":
    # пример: мониторить 60 секунд с выборкой каждую 2 секунды
    monitor(duration=60, interval=2.0)
