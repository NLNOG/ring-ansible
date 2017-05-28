#!/usr/bin/env python
#
# create-rpsl-as199036.py - FIXME

import sys,re,netaddr,ipaddr

raw_data = []
scrubbed_data = []

def loop_through_bird_puppet_config(): 
    with open('../manifests/init.pp') as input_data:
        for line in input_data:
            raw_data.append(line.strip()[1:-2])
            if "END_MARKER" in line.strip():
                break
    # COLOCLUE1,2a02:898:0:300::1,8283
    for entry in raw_data:
        entry = entry.split(',')
        if len(entry) == 3:
            try:
                ip = ipaddr.IPAddress(entry[1].strip())
                scrubbed_data.append(entry)
            except:
                pass
    for entry in scrubbed_data:
        ip = netaddr.IPAddress(entry[1])
        afi = ip.version
        name = entry[0]
        asn = entry[2]
        if afi == 4:
            print "mp-import: afi ipv4.unicast from AS%s %s at 82.94.230.130 accept ANY; # %s" % (asn, ip, name)
            print "mp-export: afi ipv4.unicast to AS%s %s at 82.94.230.130 announce NOT ANY; # %s" % (asn, ip, name)
        if afi == 6:
            print "mp-import: afi ipv6.unicast from AS%s %s at 2001:888:2001::130 accept ANY; # %s" % (asn, ip, name)
            print "mp-export: afi ipv6.unicast to AS%s %s at 2001:888:2001::130 announce NOT ANY; # %s" % (asn, ip, name)

print """inet-rtr: lg01.infra.ring.nlnog.net
descr: NLNOG RING Looking Glass lg01
local-as: AS199036
interface: 82.94.230.130 masklen 28
interface: 2001:888:2001::130 masklen 64
admin-c: JWJS1-RIPE
admin-c: PVD99-RIPE
admin-c: MP9136-RIPE
admin-c: EH4682
tech-c: JWJS1-RIPE
tech-c: PVD99-RIPE
tech-c: MP9136-RIPE
tech-c: EH4682
mnt-by: SNIJDERS-MNT
changed: job@snijders-it.nl
source: RIPE

aut-num: AS199036
as-name: NLNOG-RING-AS
descr: Job Snijders
remarks: ====================================================
remarks: This is ASN facilitates looking glass servers 
remarks: operated by the NLNOG RING. 
remarks: 
remarks: A web interface is available here: 
remarks:          lg.ring.nlnog.net
remarks: 
remarks: Visit https://ring.nlnog.net/ for more information.
remarks: ====================================================
remarks:"""

loop_through_bird_puppet_config()

print """org: ORG-SNIJ1-RIPE
admin-c: JWJS1-RIPE
admin-c: PVD99-RIPE
admin-c: MP9136-RIPE
admin-c: EH4682
tech-c: JWJS1-RIPE
tech-c: PVD99-RIPE
tech-c: MP9136-RIPE
tech-c: EH4682
mnt-by: RIPE-NCC-END-MNT
mnt-by: SNIJDERS-MNT
mnt-routes: SNIJDERS-MNT
changed: job@snijders-it.nl
source:  RIPE"""

