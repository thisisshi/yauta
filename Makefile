install:
	python -m virtualenv --python=python3 .
	. bin/activate && pip install -r requirements.txt
	. bin/activate && pip install -e .

clean:
	rm -rf .Python bin include lib pip-selfcheck.json
