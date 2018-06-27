.PHONY: all clean

all: a.out
	cat input.txt | ./a.out

a.out: main.cpp
	@g++ main.cpp

clean:
	@rm -f a.out
