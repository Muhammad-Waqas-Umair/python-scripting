# SystemVerilog Testbench Generator

This Python script generates a SystemVerilog testbench from a CSV file containing input and output test cases. The generated testbench can be used to verify the functionality of a digital design.

## **How to Use**

### **1. Prepare the CSV File**

Create a CSV file (`test_cases.csv`) with the following format:

| Input1 | Input2 | Input3 | Output1 | Output2 |
|--------|--------|--------|---------|---------|
| 0      | 0      | 0      | 0       | 0       |
| 0      | 0      | 1      | 0       | 1       |
| 0      | 1      | 0      | 1       | 0       |
| 0      | 1      | 1      | 1       | 1       |
| 1      | 0      | 0      | 0       | *       |
| 1      | 0      | 1      | *       | 1       |
| 1      | 1      | 0      | 1       | 0       |
| 1      | 1      | 1      | 1       | 1       |

- **Inputs**: `0` or `1`.
- **Outputs**: `0`, `1`, or `*` (don't care).

Save this file as `test_cases.csv` in the same directory as the script.

---

### **2. Run the Python Script**

Run the Python script to generate the SystemVerilog testbench:

```bash
python generate_testbench.py