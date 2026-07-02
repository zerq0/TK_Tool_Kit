def parse_ports(ports):
    splitted = ports.strip().split(",")
    ports_list = set()
    for x in splitted:
        x=x.strip()
        if x == "":
            raise ValueError("Invalid port input")
        if "-" in x:
            start, end = x.split("-")
            if int(end) < int(start):
                raise ValueError
            if int(start) >= 1 and int(end) <= 65535 and int (end) >=1 and int (start) <=65535:
                ports_list.update(range(int(start), int(end)+1))
        else:
            if int(x) >=1 and int(x) <= 65535:
                ports_list.add(int(x))

    return sorted(ports_list)
    