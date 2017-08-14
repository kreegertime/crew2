import os
import shutil
from multiprocessing import Pool


def chunks(l, n):
	for i in range(0, len(l), n):
		yield l[i:i + n]


def copy_packets(packets):
	for packet in packets:
		shutil.copy(packet, 'm:\\packets\\')
		print("  * Copied '{}')".format(packet))


def find_packets():
	packets = []
	for root, dirs, files in os.walk('m:\\SP Information Database\\'):
		for file in files:
			if 'Packet' in file or 'packet' in file:
				packets.append(os.path.join(root, file))
				print("  * {} Packets ({})".format(len(packets), file))
	return packets


def read_packets_file():
	content = []	
	with open('found_packets_log.txt') as f:
		content = f.readlines()

	return [x.strip() for x in content] 


if __name__ == '__main__':
	#packets = find_packets()
	packets = read_packets_file()
	print("Total Found {} Packets".format(len(packets)))

	#print("  * Creating packet audit log...")
	#bat_file = open('found_packets_log.txt', 'w')
	#for packet in packets:
	#	bat_file.write("{}\n".format(packet))
	#bat_file.close()

	print("  * Starting copy...")
	buckets = 8
	packet_buckets = list(chunks(packets, buckets))
	pool = Pool(processes=buckets)
	pool.map(copy_packets, packet_buckets)

	print("Copied {} Packets".format(len(packets)))
