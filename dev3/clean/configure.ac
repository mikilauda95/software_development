AC_INIT([mistery_foo], [1.0])
AM_INIT_AUTOMAKE([foreign])
AC_CONFIG_FILES([Makefile src/main/Makefile src/lib_foo/Makefile])


AC_PROG_RANLIB
AC_PROG_CC
AC_CONFIG_HEADERS([config.h])

AC_COMPILE_IFELSE([AC_LANG_PROGRAM([[#include <mistery.h>]],\
                [[ mistery_value(1);]])],\
                [AC_DEFINE([MISTERY_VALUE_ONEPARAM],[],[CONSTANT])],[])

AC_SEARCH_LIBS([mistery_value],[magic voodoo mistery],[],[])
AC_OUTPUT
