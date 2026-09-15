def fcfs_scheduling(processes):
    """
    FCFS (First Come First Serve) CPU Scheduling

    Input:
        [
            ("P1", arrival_time, burst_time),
            ("P2", arrival_time, burst_time),
            ...
        ]

    Output:
        List of dictionaries containing:
        Process
        Arrival Time
        Burst Time
        Start Time
        Completion Time
        Turnaround Time
        Waiting Time
    """

    # Convert tuples into dictionaries
    processes = [
        {
            "name": name,
            "arrival": arrival,
            "burst": burst
        }
        for name, arrival, burst in processes
    ]

    # FCFS:
    # Process with smaller arrival time runs first.
    # If arrival times are equal, process name is used
    # as the tie-breaker.
    processes.sort(
        key=lambda p: (p["arrival"], p["name"])
    )

    time = 0
    completed = []

    for process in processes:

        # If CPU is idle, move time to process arrival
        if time < process["arrival"]:
            time = process["arrival"]

        # Process starts
        start_time = time

        # Execute process
        time += process["burst"]

        # Process finishes
        completion_time = time

        # Turnaround Time
        turnaround_time = (
            completion_time - process["arrival"]
        )

        # Waiting Time
        waiting_time = (
            turnaround_time - process["burst"]
        )

        # Store result
        completed.append({
            "name": process["name"],
            "pid": process["name"],
            "process": process["name"],

            "arrival": process["arrival"],
            "arrival_time": process["arrival"],

            "burst": process["burst"],
            "burst_time": process["burst"],

            "start": start_time,
            "start_time": start_time,

            "completion": completion_time,
            "completion_time": completion_time,

            "turnaround": turnaround_time,
            "turnaround_time": turnaround_time,

            "waiting": waiting_time,
            "waiting_time": waiting_time
        })

    return completed