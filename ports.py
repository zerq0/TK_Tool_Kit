def parse_ports(ports):
    splitted = ports.strip().split(",")
    ports_list = set()
    for x in splitted:
        x = x.strip()
        if x == "" or x == " ":
            raise ValueError("Invalid port input")
        if "-" in x:
            start, end = x.split("-")
            start = int(start)
            end = int(end)
            if end < start:
                raise ValueError ("Port out of range")
            if start >= 1 and end <= 65535 and end >=1 and start <=65535:
                ports_list.update(range(start, end+1))
        else:
            port = int(x)
            if port >=1 and port <= 65535:
                ports_list.add(port)
            else:
                raise ValueError("Port out of range")
    return sorted(ports_list)
    