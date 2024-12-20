base_code_map = {
    ('A', 'T'): 'W', ('T', 'A'): 'W', # A or T
    ('C', 'G'): 'S', ('G', 'C'): 'S', # G or C
    ('A', 'C'): 'M', ('C', 'A'): 'M', # A or C
    ('G', 'T'): 'K', ('T', 'G'): 'K', # G or T
    ('A', 'G'): 'R', ('G', 'A'): 'R', # A or G
    ('C', 'T'): 'Y', ('T', 'C'): 'Y'  # C or T
}
def get_base_code(base1, base2):
    pair = (base1, base2)
    return base_code_map.get(pair, 'N') 

def VCF_to_SNP_matrix(vcf_file):
    with open(vcf_file, 'r') as file:
        lines = file.readlines()
        metadata = [line for line in lines if line.startswith('##')]
        header_line = [line for line in lines if line.startswith('#') and not line.startswith('##')]
        data_lines = [line for line in lines if not line.startswith('#')]
        header = header_line[0].strip().split('\t')
        header_title= list(filter(lambda x: len(x)>1,header))
        header_samples = header_title[9:]
        SNP_data_Dict ={}
        sample_List=[]
        for sample in range(len(header_samples)):
            sample_name=header_samples[sample]
            sample_List.append(sample_name)
            SNP_data_Dict[sample_name] = {}
            for chromosome in range(len(data_lines)):
                SNP_num=f'SNP{chromosome}'
                SNP_data_Dict[sample_name][SNP_num]={}
                datas = data_lines[chromosome].strip().split('\t')
                data_values = list(filter(lambda x: len(x)>=1,datas))
                CHROM_data=data_values[0]
                SNP_data_Dict[sample_name][SNP_num]["CHROM"]=CHROM_data
                POS_data=data_values[1]
                SNP_data_Dict[sample_name][SNP_num]["POS"]=POS_data
                ID_data=data_values[2]
                SNP_data_Dict[sample_name][SNP_num]["ID"]=ID_data
                REF_data=data_values[3]
                SNP_data_Dict[sample_name][SNP_num]["REF"]=REF_data
                ALT_data=data_values[4]
                SNP_data_Dict[sample_name][SNP_num]["ALT"]=ALT_data
                QUAL_data=data_values[5]
                INFO_data=data_values[7]
                FORMAT_raw=data_values[8]
                FORMAT_list=FORMAT_raw.split(':')
                SAMPLE_Total_raw=[]
                SAMPLE_data_raw=data_values[9:]
                for sample in range(len(SAMPLE_data_raw)):
                    sample_Data_List= SAMPLE_data_raw[sample].split(':')
                    format_dict = dict(zip(FORMAT_list, sample_Data_List))
                    if len(ALT_data) < 2 :
                        if format_dict["GT"]=="0/0":
                            format_dict["GT"]=REF_data
                        elif format_dict["GT"]=="0/1" or format_dict["GT"]=="1/0":
                            format_dict["GT"]=get_base_code(REF_data, ALT_data)
                        elif format_dict["GT"]=="1/1":
                            format_dict["GT"]=ALT_data
                        else:
                            format_dict["GT"]='N'
                    else :
                        format_dict["GT"]="N"
                    final_format_dict ={'GT':format_dict["GT"], 'AD/DP':format_dict['AD']+"/"+format_dict['DP']}
                    sample_FormatData_List = final_format_dict
                    SAMPLE_Total_raw.append(sample_FormatData_List)
                SAMPLE_dic = dict(zip(sample_List, SAMPLE_Total_raw))
                SNP_data_Dict[sample_name][SNP_num]=SAMPLE_dic[sample_name]
        print(SNP_data_Dict)

VCF_to_SNP_matrix("Capsicum_GBS_191ea_Filtered_SNP_10009.vcf")
