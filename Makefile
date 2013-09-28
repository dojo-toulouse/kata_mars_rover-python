tests:
	nosetests3

.ONESHELL:
ci:
	while true; do
		clear
		nosetests3 -s
		inotifywait -q -e create,modify,delete *.py
	done
