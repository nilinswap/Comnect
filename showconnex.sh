#!/bin/bash

for dest in `arp -a | tail +5 | awk '{print $2}'`
do
    nslookup $dest 1>/tmp/arp$$ 2>/dev/null
    if [ `wc -l /tmp/arp$$ | awk '{print $1}'` -ge 4 ]; then
        tail -2 /tmp/arp$$ | grep Address | awk '{print $2}'
    fi
done

rm /tmp/arp$$