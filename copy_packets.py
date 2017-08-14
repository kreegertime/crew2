import shutil
from multiprocessing import Pool


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def copy_packets(packets):
    for packet in packets:
        shutil.copy(packet, 'm:\\packets\\')
        print("  * Copied '{}')".format(packet))


def read_packets_file():
    content = []
    with open('found_packets_log.txt') as f:
        content = f.readlines()

    return [x.strip() for x in content]


if __name__ == '__main__':
    packets = read_packets_file()
    print("Total Found {} Packets".format(len(packets)))

    print("  * Starting copy...")
    buckets = 8
    packet_buckets = list(chunks(packets, buckets))
    pool = Pool(processes=buckets)
    pool.map(copy_packets, packet_buckets)

    print("Copied {} Packets".format(len(packets)))
