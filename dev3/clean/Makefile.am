bindir="./uselessbin"

bin_PROGRAMS = mistery_foo
mistery_foo_SOURCES = src/main/main.c src/main/main.h

noinst_PROGRAMS = libfoo.a
libfoo_a_SOURCES = src/lib_foo/foo.c src/lib_foo/foo.h

mistery_foo_LDADD = libfoo.a

mistery_foo_LDADD += $(LIB_CHOSEN)
mistery_foo_DEPENDENCIES = $(LIB_CHOSEN)

