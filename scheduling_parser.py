import re


def _parse_processes(question):

    question = question.strip()

    # Find process names
    processes = re.findall(
        r"\bP\d+\b",
        question,
        re.IGNORECASE
    )

    # Remove duplicate process names while preserving order
    unique_processes = []
    for p in processes:
        p = p.upper()
        if p not in unique_processes:
            unique_processes.append(p)

    # Find arrival times.
    # AT must be followed by =, :, or whitespace.
    arrival_match = re.search(
        r"(?:arrival\s*time|arrival)\s*[=:]?\s*([0-9,\s]+)",
        question,
        re.IGNORECASE
    )

    if not arrival_match:
        arrival_match = re.search(
            r"\bAT\s*[=:]\s*([0-9,\s]+)",
            question,
            re.IGNORECASE
        )

    # Find burst times
    burst_match = re.search(
        r"(?:burst\s*time|burst)\s*[=:]?\s*([0-9,\s]+)",
        question,
        re.IGNORECASE
    )

    if not burst_match:
        burst_match = re.search(
            r"\bBT\s*[=:]\s*([0-9,\s]+)",
            question,
            re.IGNORECASE
        )

    if arrival_match and burst_match:

        arrivals = [
            int(x)
            for x in re.findall(
                r"\d+",
                arrival_match.group(1)
            )
        ]

        bursts = [
            int(x)
            for x in re.findall(
                r"\d+",
                burst_match.group(1)
            )
        ]

        if (
            len(unique_processes) == len(arrivals)
            and len(arrivals) == len(bursts)
        ):
            return [
                (
                    unique_processes[i],
                    arrivals[i],
                    bursts[i]
                )
                for i in range(len(unique_processes))
            ]

    # Individual format:
    # P1 AT=1 BT=2
    pattern = re.compile(
        r"(P\d+)"
        r".*?"
        r"(?:arrival\s*time|arrival|AT)"
        r"\s*[=:]\s*(\d+)"
        r".*?"
        r"(?:burst\s*time|burst|BT)"
        r"\s*[=:]\s*(\d+)",
        re.IGNORECASE
    )

    matches = pattern.findall(question)

    return [
        (
            name.upper(),
            int(arrival),
            int(burst)
        )
        for name, arrival, burst in matches
    ]


def parse_sjf_processes(question):
    return _parse_processes(question)


def parse_sjf_question(question):
    return _parse_processes(question)


def parse_fcfs_processes(question):
    return _parse_processes(question)


def parse_fcfs_question(question):
    return _parse_processes(question)


def parse_srtf_processes(question):
    return _parse_processes(question)


def parse_srtf_question(question):
    return _parse_processes(question)


def parse_rr_processes(question):
    return _parse_processes(question)


def parse_rr_question(question):

    processes = _parse_processes(question)

    quantum_pattern = re.compile(
        r"(?:time\s+quantum|quantum|q)"
        r"\s*[=:]?\s*(\d+)",
        re.IGNORECASE
    )

    match = quantum_pattern.search(question)

    if not match:
        return processes, None

    return processes, int(match.group(1))