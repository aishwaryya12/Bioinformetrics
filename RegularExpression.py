def gen_reg_exp(seq_list, no_of_col):
    final_list=[] 
    for colnum in range(no_of_col): 
        collist=[] 
        for colseq in seq_list: 
            collist.append(colseq[colnum]) 
        if len(set(collist))==len(collist): 
            final_list.append('x') 
        else: 
            if len(set(collist))==1: 
                final_list.append(collist[0]) 
            else: 
                final_list.append(''.join(set(collist))) 
    display_output(final_list)
def display_output(final_list): 
    print(*final_list, sep='-') 
no_of_seq=int(input("Enter the number of sequence: ")) 
print("Enter all the sequences") 
seq_list=[] 
for _ in range(no_of_seq): 
    seq_list.append(list(map(str, input("").split()))) 
gen_reg_exp(seq_list, len(seq_list[0])) 
