def parse_ports(ports):
    splitted = ports.strip().split(",")
    ports_list = []
    for x in splitted:
        if x == "":
            print("invalid port input")
            exit
        if "-" in x:
            start, end = x.split("-")
            if end< start:
                temp = start
                start = end
                end = temp
            if int(start) >= 1 and int(end) <= 65535:
                ports_list.extend(range(int(start), int(end)+1))
        else:

    return sorted(ports_list)
    