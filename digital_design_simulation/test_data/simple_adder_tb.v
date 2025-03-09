// simple_adder_tb.v
`timescale 1ns / 1ps

module simple_adder_tb;

    // Declare inputs as reg and outputs as wire
    reg [1:0] A;
    reg [1:0] B;
    wire [2:0] SUM;

    // Instantiate the simple_adder module
    simple_adder uut (
        .A(A),
        .B(B),
        .SUM(SUM)
    );

    // Test stimulus
    initial begin
        // Display the header for simulation output
        $display("A B | SUM");
        $display("-----------");

        // Apply input values and observe the output
        A = 2'b00; B = 2'b00; #10;  // Apply inputs 00, 00
        $display("%b %b | %b", A, B, SUM);

        A = 2'b01; B = 2'b01; #10;  // Apply inputs 01, 01
        $display("%b %b | %b", A, B, SUM);

        A = 2'b10; B = 2'b10; #10;  // Apply inputs 10, 10
        $display("%b %b | %b", A, B, SUM);

        A = 2'b11; B = 2'b11; #10;  // Apply inputs 11, 11
        $display("%b %b | %b", A, B, SUM);

        $finish;  // End simulation
    end

endmodule
