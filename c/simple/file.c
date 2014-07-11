#include <Python.h>
#include <stdio.h>

int main() {
	printf("In main\n");
	Py_Initialize();
	PyRun_SimpleString("x = 'brave' + ' sir robin'");
	PyRun_SimpleString("print x");
}

