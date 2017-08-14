import os


def find_packets():
    packets = []
    for root, dirs, files in os.walk('m:\\SP Information Database\\'):
        for file in files:
            if 'Packet' in file or 'packet' in file:
                packets.append(os.path.join(root, file))
                print("  * {} Packets ({})".format(len(packets), file))
    return packets


if __name__ == '__main__':
    packets = find_packets()
    print("Total Found {} Packets".format(len(packets)))

    print("  * Creating packet audit log...")
    packet_audit_log = open('found_packets_log.txt', 'w')
    for packet in packets:
        packet_audit_log.write("{}\n".format(packet))
    packet_audit_log.close()
