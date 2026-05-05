def parse_ports(ports):
    splitted = ports.strip().split(",")
    ports_list = []
    for x in splitted:
        if int(x) >= 1 and int(x)<=65535:
            ports_list.append(int(x))
    return ports_list

