#!/bin/bash
while true
do
	echo
	echo started recording
	rm foo.raw
	./recordSound.sh &
	sleep 6
	echo
	echo started submit
	echo
	./submitSound.sh &
	sleep 4
done
