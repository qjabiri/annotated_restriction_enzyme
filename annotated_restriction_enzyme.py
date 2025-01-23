#!/usr/bin/env python3
# Name: Qudsi Aljabiri and Ziad Kedkad

def file_view(ss):
    fileRead = open(ss, "r")
    file = {}
    yes = 3
    key = ''
    value = ''
    for line in fileRead:
        # When file is created with the restriction enzyme sequence to name then we can finish the rest putting the key-value pair into the dictionary file
        if yes == 0:
            key = line.strip()
            yes += 1
        elif yes == 1:
            value = line.strip()
            file[str(key)] = str(value)
            yes += 1
        elif 'yes' in line:
            yes = 0
    return file

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)

def combination(nucSeq, file):
    enzymes = {}
    enzOrder = {}
    key_list = list(file.keys())
    val_list = list(file.values())
    
    for i in file.values():
        place = ""
        position = val_list.index(i)
        if i.strip() in nucSeq:
            position = val_list.index(i)
            find1 = find_all(nucSeq, i.strip())
            place1 = ""
            for j in find1:
                place1 = place1 + str(j) + ', '
            place = place + place1
            n = nucSeq.count(i.strip())
            if n > 0:
                val = "Number of times found: " + str(n) + " positions: " + str(place)
                val = val[:-2]  # Remove trailing ', '
                enzymes[key_list[position]] = val
                enzOrder[key_list[position]] = n
    return enzymes, enzOrder

def read_fasta(file_name):
    sequences = {}
    with open(file_name, 'r') as f:
        header = None
        sequence = []
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if header:
                    sequences[header] = ''.join(sequence)
                header = line[1:]  # Remove '>'
                sequence = []
            else:
                sequence.append(line)
        if header:
            sequences[header] = ''.join(sequence)
    return sequences

def main():
    c = 0
    while True:
        f = 'restriction_enzyme_result.txt'
        f1 = f
        if c > 0:
            f = str(c) + f1
        
        # Placeholder for file name
        fasta_file = input("Please enter the FASTA file name: ")
        file = file_view("restriction_enzymes_list.txt")
        
        sequences = read_fasta(fasta_file)
        
        for header, seq in sequences.items():
            enzymes, enzOrder = combination(seq, file)
            enzOrder2 = dict(sorted(enzOrder.items(), key=lambda kv: kv[1]))
            
            with open(f, 'w') as out_file:
                out_file.write('FASTA Header: '+ header + "\nNucleotide Sequence: "+ seq + "\nRestriction Enzymes Present:\n")
                for i in enzOrder2:
                    out_file.write(i.strip() + ': ' + enzymes[i] + '\n')
                out_file.write('Credit for restriction enzyme list is due to http://rebase.neb.com/rebase/azlist.re2.cy.html.\nSuppliers for these restriction enzymes can also be found at that link.')
            
            c += 1
            print(f"Results for {header} saved in {f}")

main()

