; DESCENDING ORDER
	AREA DECENDING, CODE, READONLY
ENTRY
	MOV R0, #0X04;
NXT
	MOV R1, #03;
	MOV R2,#0X40000000;
COMPARE
	LDR R3,[R2]
	ADD R2,R2,#04;
	LDR R4,[R2]
	CMP R3,R4;
	BGT NOEXCHANGE
	STR R3,[R2];
	SUB R2,R2,#04;
	STR R4,[R2]
	ADD R2,R2,#04
NOEXCHANGE
	SUB R1,R1, #01;
	CMP R1,#00;
	BNE COMPARE
	SUB R0,R0,#01;
	CMP R0,#00
	BNE NXT
STOP B STOP
END