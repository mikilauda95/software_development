CC=gcc

all: $(shell date +%B).o strange_app

$(shell date +%B).o : $(shell date +%B).c
	$(CC) -c $(shell date +%B).c

strange_app: $(shell date +%B).o  strange_app.c strange_app.h
		$(CC) strange_app.c $(shell date +%B).o -o strange_app

clean:
	rm -f *.o
	rm -f strange_app
