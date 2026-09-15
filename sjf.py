def sjf_non_preemptive(processes):
    """
    processes:
    [
        ("P1", arrival_time, burst_time),
        ("P2", arrival_time, burst_time),
        ...
    ]
    """

    processes = [
        {
            "name": name,
            "arrival": arrival,
            "burst": burst
        }
        for name, arrival, burst in processes
    ]

    time = 0
    completed = []
    remaining = processes.copy()

    while remaining:

        available = [
            p for p in remaining
            if p["arrival"] <= time
        ]

        if not available:
            time = min(p["arrival"] for p in remaining)
            continue

        current = min(
            available,
            key=lambda p: (p["burst"], p["arrival"])
        )

        start_time = time

        time += current["burst"]

        completion_time = time

        completed.append({
            "name": current["name"],
            "arrival": current["arrival"],
            "burst": current["burst"],
            "start": start_time,
            "completion": completion_time
        })

        remaining.remove(current)

    return completed


