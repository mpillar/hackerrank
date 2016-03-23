.PHONY: all clean

all:
	./.run.sh

clean:
	find . -name *.pyc | xargs rm -rf
	find . -name *.class | xargs rm -rf
	find . -name *.pyc | xargs rm -rf
