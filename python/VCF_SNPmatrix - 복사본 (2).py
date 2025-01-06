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
        # print(SNP_data_Dict)
        return SNP_data_Dict

# input
import re
def SNP_matrix_delete1 (vcf_file):
    result_matrix = VCF_to_SNP_matrix(vcf_file)
    sample_List = []
    for sample_key, sample_value in result_matrix.items():
        sample_List.append(sample_key)
    input_value = str(input())
    delimiters = r'[,\s/\\]'
    select_samples=re.split(delimiters, input_value)
    select_samples=[x for x in select_samples if x]
    if len(select_samples) == 0:
        return result_matrix
    elif len(select_samples) == 1:
        if select_samples[0] not in result_matrix:
            return result_matrix
        else:
            del result_matrix[str(select_samples[0])]
        return result_matrix
    elif len(select_samples) >= 2:
        for select_sample in select_samples:
            if select_sample not in result_matrix:
                return result_matrix
            else:
                print(f"{str(select_sample)}")
                del result_matrix[str(select_sample)]
        return result_matrix
    print(result_matrix)
    return result_matrix

# 함수 tuple
def SNP_matrix_delete2 (vcf_file, select_samples_List):
    result_matrix = VCF_to_SNP_matrix(vcf_file)
    sample_List = []
    for sample_key, sample_value in result_matrix.items():
        sample_List.append(sample_key)
    delimiters = r'[,\s/\\]'
    select_samples=re.split(delimiters, select_samples_List)
    select_samples=[x for x in select_samples if x]
    if len(select_samples) == 0:
        return result_matrix
    elif len(select_samples) == 1:
        if select_samples[0] not in result_matrix:
            return result_matrix
        else:
            del result_matrix[str(select_samples[0])]
        return result_matrix
    elif len(select_samples) >= 2:
        for select_sample in select_samples:
            if select_sample not in result_matrix:
                return result_matrix
            else:
                print(f"{str(select_sample)}")
                del result_matrix[str(select_sample)]
        return result_matrix
    # print(result_matrix)

def SNP_matrix_SNP_Indel(vcf_file, search = "all"):
    # 모든 데이터의 사전
    SNP_Indel_Dic = {
        "SNP": {},
        "Insert": {},
        "Delete": {},
        "Missing": {},
        "else": {}
    }

    # 결과 매트릭스
    result_matrix = VCF_to_SNP_matrix(vcf_file)
    sample_List = []
    SNP_List = []
    SNP_keys = {}

    for sample_key, sample_value in result_matrix.items():
        sample_List.append(sample_key)
        SNP_keys = sample_value
    SNP_List = SNP_keys.keys()

    for sample in sample_List:
        for category in SNP_Indel_Dic.keys():
            if sample not in SNP_Indel_Dic[category]:
                SNP_Indel_Dic[category][sample] = {}

        for SNP in SNP_List:
            REF = result_matrix[sample][SNP]["REF"]
            ALT = result_matrix[sample][SNP]["ALT"]
            if len(REF) == 1 and len(ALT) == 1:
                # Missing
                if ALT == '.' or ALT == ',':
                    SNP_Indel_Dic["Missing"][sample][SNP] = result_matrix[sample][SNP]
                # SNP
                else:
                    SNP_Indel_Dic["SNP"][sample][SNP] = result_matrix[sample][SNP]
                    
            else:
                # Indel
                if len(REF) > 1 or len(ALT) > 1:
                    if len(REF) > len(ALT):
                    # Delete 
                        if len(ALT) == 1 :
                            SNP_Indel_Dic["Delete"][sample][SNP] = result_matrix[sample][SNP]
                        else:
                            SNP_Indel_Dic["else"][sample][SNP] = result_matrix[sample][SNP]
                    elif len(ALT) > len(REF):
                        # Insert
                        if len(str(ALT).split(",")) > 1:
                            SNP_Indel_Dic["else"][sample][SNP] = result_matrix[sample][SNP]
                        elif str(ALT).find("<")>=0:
                            SNP_Indel_Dic["else"][sample][SNP] = result_matrix[sample][SNP]
                        elif len(REF) == 1 :
                            SNP_Indel_Dic["Insert"][sample][SNP] = result_matrix[sample][SNP]
                        else:
                            SNP_Indel_Dic["else"][sample][SNP] = result_matrix[sample][SNP]
                else:
                    SNP_Indel_Dic["else"][sample][SNP] = result_matrix[sample][SNP]

    if search.upper() == "ALL":
        print(SNP_Indel_Dic)
    elif search.upper() == "SNP":
        print(SNP_Indel_Dic["SNP"])
    elif search.upper() == "INSERT":
        print(SNP_Indel_Dic["Insert"])
    elif search.upper() == "INSERTION":
        print(SNP_Indel_Dic["Insert"])
    elif search.upper() == "DELETE":
        print(SNP_Indel_Dic["Delete"])
    elif search.upper() == "DELETION":
        print(SNP_Indel_Dic["Delete"])
    elif search.upper() == "MISS":
        print(SNP_Indel_Dic["Missing"])
    elif search.upper() == "MISSING":
        print(SNP_Indel_Dic["Missing"])
    elif search.upper() == "ELSE":
        print(SNP_Indel_Dic["else"])
    elif search.upper() == "ETC":
        print(SNP_Indel_Dic["else"])
    else:
        print(SNP_Indel_Dic)

    if search.upper() == "ALL":
        return SNP_Indel_Dic
    elif search.upper() == "SNP":
        return SNP_Indel_Dic["SNP"]
    elif search.upper() == "INSERT":
        return SNP_Indel_Dic["Insert"]
    elif search.upper() == "INSERTION":
        return SNP_Indel_Dic["Insert"] 
    elif search.upper() == "DELETE":
        return SNP_Indel_Dic["Delete"]
    elif search.upper() == "DELETION":
        return SNP_Indel_Dic["Delete"]
    elif search.upper() == "MISS":
        return SNP_Indel_Dic["Missing"]
    elif search.upper() == "MISSING":
        return SNP_Indel_Dic["Missing"]
    elif search.upper() == "ELSE":
        return SNP_Indel_Dic["else"]
    elif search.upper() == "ETC":
        return SNP_Indel_Dic["else"]
    else:
        return SNP_Indel_Dic
    
def vcf_SNP_matrix_filtering(vcf_file, select_samples_list, search="all"):
    # vcf to SNP matrix
    result_matrix = VCF_to_SNP_matrix(vcf_file)
    # vcf to SNP matrix delete
    result_matrix_filtered = SNP_matrix_delete2(vcf_file, select_samples_list)
    # SNP_Indel search
    SNP_Indel_Dic = SNP_matrix_SNP_Indel(vcf_file, search)
    # SNP_Indel filtering
    SNP_Indel_filtered = {}
    for category, sample_dict in SNP_Indel_Dic.items():
        for sample, SNP_dict in sample_dict.items():
            if sample in result_matrix_filtered:
                SNP_Indel_filtered.setdefault(category, {})
                SNP_Indel_filtered[category][sample] = SNP_dict
    # print(SNP_Indel_filtered)
    return SNP_Indel_filtered

def VCF_to_SNP_matrix_reverse(vcf_file,select_samples_list, search="all"):
    result_reverse_matrix ={}
    result_matrix = vcf_SNP_matrix_filtering(vcf_file, select_samples_list, search)
    sample_List = []
    SNP_List = []
    SNP_keys = {}
    for sample_key, sample_value in result_matrix.items():
        sample_List.append(sample_key)
        SNP_keys=sample_value
    SNP_List=SNP_keys.keys()

    for SNP_key in SNP_List:
        for sample_key in sample_List:
            result_reverse_matrix.setdefault(SNP_key, {})
            result_reverse_matrix[SNP_key][sample_key] = result_matrix[sample_key][SNP_key]
    print (result_reverse_matrix)
    return result_reverse_matrix    

# def VCF_to_SNP_matrix_finally():


# vcf to SNP matrix 1
VCF_to_SNP_matrix("SNPINDELexample.vcf")
# vcf to SNP matrix 2
VCF_to_SNP_matrix_reverse("SNPINDELexample.vcf", "")
# vcf to SNP matrix 3 - input
SNP_matrix_delete1("SNPINDELexample.vcf")
# vcf to SNP matrix 3 - tuple
select_samples_List="SAMPLE1"
select_samples_List=" "
SNP_matrix_delete2("SNPINDELexample.vcf", select_samples_List)
# vcf to SNP matrix 4 - SNP_Indel
SNP_matrix_SNP_Indel("SNPINDELexample.vcf", "SNP")

vcf_SNP_matrix_filtering("SNPINDELexample.vcf", select_samples_List,"all")

