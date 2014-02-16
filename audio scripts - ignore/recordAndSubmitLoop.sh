#!/bin/bash
while true
do
	rm foo.raw
	./recordSound.sh &
	sleep 6
	echo starting submit
	./submitSound.sh > lastRecognitionResponse.txt &
	sleep 4
	cat lastRecognitionResponse.txt
done
