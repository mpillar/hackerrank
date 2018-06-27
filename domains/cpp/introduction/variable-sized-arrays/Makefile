.PHONY: all clean

all: a.out
	cat input.txt | ./a.out

a.out: main.cpp
	@g++ -Wc++11-extensions main.cpp

clean:
	@rm -f a.out
