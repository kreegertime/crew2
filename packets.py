import os
import shutil

packets = []
for root, dirs, files in os.walk('m:\\SP Information Database\\'):
    for file in files:
        if 'Packet' in file or 'packet' in file:
            packets.append(os.path.join(root, file))
                        print("  * {} Packets ({})".format(len(packets), file))

print("Total Found {} Packets".format(len(packets)))

print("  * Creating batch script file")
bat_file = open('c:\\copy_packets.bat', 'w')
for packet in packets:
    bat_file.write("xcopy /y {} m:\\packets \n".format(packet))
bat_file.close()

print("  * Starting copy")
for packet in packets:
    shutil.copy(packet, 'm:\\packets\\')
        print("  * Copied '{}')".format(packet))

print("Copied {} Packets".format(len(packets)))
