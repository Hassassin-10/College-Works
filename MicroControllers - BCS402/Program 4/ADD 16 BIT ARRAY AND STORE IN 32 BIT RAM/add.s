	AREA MULTIPLICATION, CODE, READONLY
ENTRY
START
	LDR R1,=0x1114
	LDR R2,=0x1116
	MUL R3,R1,R2;
STOP B STOP
END