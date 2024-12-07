module full_adder ( 
input A, 
input B, 
input Cin, 
output Sum, 
output Cout 
); 
assign Sum = A ^ B ^ Cin; 
assign C = (A & B) | (B & Cin) | (A & Cin); 
endmodule