import csv

def generate_testbench(csv_filename, testbench_filename):
    with open(csv_filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        
        # Testbench header
        header = """
`timescale 1ns/1ps
module testbench;
  reg Input1, Input2, Input3;
  wire Output1, Output2;
  
  // Instantiate the DUT
  your_module_name dut (
    .Input1(Input1),
    .Input2(Input2),
    .Input3(Input3),
    .Output1(Output1),
    .Output2(Output2)
  );
  
  initial begin
"""
        
        # Testbench body
        body = ""
        for row in reader:
            # Apply inputs
            body += f"    Input1 = {row['Input1']}; Input2 = {row['Input2']}; Input3 = {row['Input3']}; #10;\n"
            
            # Check outputs
            if row['Output1'] != '*' and row['Output2'] != '*':
                body += f"    if (Output1 !== {row['Output1']} || Output2 !== {row['Output2']}) begin\n"
                body += "      $display(\"Error: Output mismatch at time %0t\", $time);\n"
                body += "      $finish;\n"
                body += "    end\n"
            else:
                if row['Output1'] != '*':
                    body += f"    if (Output1 !== {row['Output1']}) begin\n"
                    body += "      $display(\"Error: Output1 mismatch at time %0t\", $time);\n"
                    body += "      $finish;\n"
                    body += "    end\n"
                if row['Output2'] != '*':
                    body += f"    if (Output2 !== {row['Output2']}) begin\n"
                    body += "      $display(\"Error: Output2 mismatch at time %0t\", $time);\n"
                    body += "      $finish;\n"
                    body += "    end\n"
        
        # Testbench footer
        footer = """
    $display("Testbench finished successfully at time %0t", $time);
    $finish;
  end
endmodule
"""
        
        # Combine header, body, and footer
        testbench = header + body + footer
        
        # Write the testbench to a file
        with open(testbench_filename, 'w') as tb_file:
            tb_file.write(testbench)

generate_testbench('test_cases.csv', 'testbench.sv')