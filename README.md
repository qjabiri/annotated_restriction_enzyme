# Restriction Enzyme Locator

## Overview
This project provides a Python-based solution to identify restriction enzyme recognition sites within DNA sequences. It includes scripts, enzyme data, and example results to facilitate efficient and accurate sequence analysis.

## Project Structure
├── annotated_restriction_enzyme.py # Main Python script for processing sequences ├── annotated-restriction_enzymes_list-2.txt.pdf # List of restriction enzymes and their recognition sequences ├── annotated-BME160 Paper.pdf # Paper detailing project objectives and implementation ├── annotated-EXrestriction_enzyme_result-2.txt.pdf # Sample output file with enzyme recognition results ├── annotated-restriction_enzymes-2.py.pdf # Alternative Python script with similar functionality ├── README.md # Project documentation


## Files Description

### 1. `annotated_restriction_enzyme.py`
This Python script processes restriction enzyme data and identifies enzyme recognition sites within a DNA sequence.

**Main Functions:**
- `file_view(ss)`: Reads the enzyme list and stores it in a dictionary.
- `find_all(a_str, sub)`: Finds all occurrences of a restriction site in the DNA sequence.
- `combination(nucSeq, file)`: Identifies restriction enzyme sites and their positions.
- `read_fasta(file_name)`: Reads FASTA files containing DNA sequences.
- `main()`: Prompts the user for input, processes sequences, and saves results.

**Usage:**
```bash
python annotated_restriction_enzyme.py
2. annotated-restriction_enzymes_list-2.txt.pdf
A comprehensive list of restriction enzymes, including their recognition sequences and suppliers. The list is sourced from REBASE.

3. annotated-BME160 Paper.pdf
A detailed paper providing background information on restriction enzymes, the significance of the project, and implementation details. Key highlights include:

Importance of restriction enzymes in molecular biology.
Efficiency and accessibility improvements offered by the program.
Potential future enhancements such as a web interface.
4. annotated-EXrestriction_enzyme_result-2.txt.pdf
An example of the program's output, showing:

Input nucleotide sequence.
List of restriction enzymes found in the sequence.
Number of occurrences and positions of each enzyme.
5. annotated-restriction_enzymes-2.py.pdf
An alternative version of the main Python script with slight variations in implementation.

How to Use the Program
Ensure you have Python 3 installed.

Place your DNA sequence in a FASTA file.

Run the script:

python annotated_restriction_enzyme.py
Provide the FASTA file name when prompted.

View the output file, which lists restriction enzymes present in the sequence.

Example Usage
Input:


Please enter the FASTA file name: example.fasta
Output (saved in restriction_enzyme_result.txt):


FASTA Header: Sample1
Nucleotide Sequence: ACGTACGT...
Restriction Enzymes Present:
EcoRI: Number of times found: 2 positions: 12, 45
BamHI: Number of times found: 1 position: 78
Future Improvements
Develop a graphical user interface (GUI).
Enhance the output format with visual charts and graphs.
Automate enzyme supplier searches.
License
This project is released under the MIT License.

Authors
Qudsi Aljabiri
Ziad Kedkad
References
Roberts, R. J., Vincze, T., Posfai, J., & Macelis, D. (2009). "REBASE—a database for DNA restriction and modification enzymes." Nucleic Acids Research. DOI:10.1093/nar/gkp874
