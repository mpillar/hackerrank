.PHONY: all clean

all:
	./.run.sh

clean:
	rm -f `find . -name *.pyc`
	rm -f `find . -name *.class`
