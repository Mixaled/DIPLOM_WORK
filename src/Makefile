all: test debtors json
json:
	python json_format.py
test: clear
	python testBD.py
clear:
	python clear.py
debtors: clear_deb
	python find_debtors.py
clear_deb:
	python clear_deb.py
send: debtors
	python send.py
get:
	python get.py
