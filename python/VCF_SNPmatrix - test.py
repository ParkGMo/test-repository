# VCF

# vcf 형식의 파일을 읽고 쓸수 있는 파이썬 라이브러리로서, 생물정보분야의 SNP, INDEL, CNV 등 
# 유전자변이 연구에 쓰이는 VCF 형식의 파일을 다루기 유용한 모듈이다.
# pip install pyvcf

# import vcf
# vcf_reader = vcf.Reader(open('vcf/test/example-4.0.vcf', 'r'))
# for record in vcf_reader:

# ...     print record
# Record(CHROM=20, POS=14370, REF=G, ALT=[A])
# Record(CHROM=20, POS=17330, REF=T, ALT=[A])
# Record(CHROM=20, POS=1110696, REF=A, ALT=[G, T])
# Record(CHROM=20, POS=1230237, REF=T, ALT=[None])
# Record(CHROM=20, POS=1234567, REF=GTCT, ALT=[G, GTACT])

# 파일 형식
# VCF 파일을 열어보면 해당 데이터에 대한 설명이 ##을 통해 주석으로 달려있다. 
# CHROM, POS, ID, REF, ALT, QUAL, FILTER, INFO, FORMAT, Sample1 등과 같은 헤더 정보가 있으며, 
# 그 아래에 실제의 variant 정보를 확인할 수 있다.

##fileformat=VCFv4.0
##fileDate=20110705
##reference=1000GenomesPilot-NCBI37
##phasing=partial
##INFO=<ID=NS,Number=1,Type=Integer,Description="Number of Samples With Data">
##INFO=<ID=DP,Number=1,Type=Integer,Description="Total Depth">
##INFO=<ID=AF,Number=.,Type=Float,Description="Allele Frequency">
##INFO=<ID=AA,Number=1,Type=String,Description="Ancestral Allele">
##INFO=<ID=DB,Number=0,Type=Flag,Description="dbSNP membership, build 129">
##INFO=<ID=H2,Number=0,Type=Flag,Description="HapMap2 membership">
##FILTER=<ID=q10,Description="Quality below 10">
##FILTER=<ID=s50,Description="Less than 50% of samples have data">
##FORMAT=<ID=GQ,Number=1,Type=Integer,Description="Genotype Quality">
##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">
##FORMAT=<ID=DP,Number=1,Type=Integer,Description="Read Depth">
##FORMAT=<ID=HQ,Number=2,Type=Integer,Description="Haplotype Quality">
# CHROM POS    ID        REF  ALT     QUAL FILTER INFO                              FORMAT      Sample1        Sample2        Sample3
# 2      4370   rs6057    G    A       29   .      NS=2;DP=13;AF=0.5;DB;H2           GT:GQ:DP:HQ 0|0:48:1:52,51 1|0:48:8:51,51 1/1:43:5:.,.
# 2      7330   .         T    A       3    q10    NS=5;DP=12;AF=0.017               GT:GQ:DP:HQ 0|0:46:3:58,50 0|1:3:5:65,3   0/0:41:3
# 2      110696 rs6055    A    G,T     67   PASS   NS=2;DP=10;AF=0.333,0.667;AA=T;DB GT:GQ:DP:HQ 1|2:21:6:23,27 2|1:2:0:18,2   2/2:35:4
# 2      130237 .         T    .       47   .      NS=2;DP=16;AA=T                   GT:GQ:DP:HQ 0|0:54:7:56,60 0|0:48:4:56,51 0/0:61:2
# 2      134567 microsat1 GTCT G,GTACT 50   PASS   NS=2;DP=9;AA=G                    GT:GQ:DP    0/1:35:4       0/2:17:2       1/1:40:3

# , pos1 pos2 pos3 pos4 pos5
# ID1
# ID2
# ID3
# ID4
# ID5

# VCF header
# VCF 파일의 header 부분에서는 파일 본문 내용을 설명하는 메타데이터를 제공한다. 
# 권장되는 키워드에는 파일형식(fileformat), 파일생성일자(filedate), 참조파일(reference)가 있으며 선택적으로 아래 정보들을 포함한다.

# VCF columns
# VCF 파일의 본문은 header 정보를 기반으로, 
# 8개의 필수적인 열과 샘플에 대한 다른 정보들을 포함하는 무제한의 열로 이루어져 있으며, 
# 이들은 탭(tab)으로 분리되어 있다.

# import pandas_plink
# snp_info,sample_info,genotypes  = pandas_plink.read_plink('genotypes/chr.1')
# genotype_mat = genotypes.compute()

# pandas_plink.read_plink(https://pandas-plink.readthedocs.io/en/latest/api/pandas_plink.read_plink.html)
# from os.path import join
# from pandas_plink import read_plink
# from pandas_plink import get_data_folder
# (bim, fam, bed) = read_plink(join(get_data_folder(), "chr*.bed"),
#                              verbose=False)
# print(bim.head())
# #   chrom        snp       cm     pos a0 a1  i
# # 0    11  316849996     0.00  157439  C  T  0
# # 1    11  316874359     0.00  181802  G  C  1
# # 2    11  316941526     0.00  248969  G  C  2
# # 3    11  317137620     0.00  445063  C  T  3
# # 4    11  317534352     0.00  841795  C  T  4
# print(fam.head())
# #     fid   iid father mother gender trait  i
# # 0  B001  B001      0      0      0    -9  0
# # 1  B002  B002      0      0      0    -9  1
# # 2  B003  B003      0      0      0    -9  2
# # 3  B004  B004      0      0      0    -9  3
# # 4  B005  B005      0      0      0    -9  4
# print(bed.compute())
# # [[0.00 0.00 0.00 ... 2.00 2.00 0.00]
# #  [0.00 1.00 0.00 ... 2.00 1.00 0.00]
# #  [2.00 2.00 2.00 ... 0.00 0.00 2.00]
# #  ...
# #  [2.00 0.00 0.00 ... 2.00 2.00 1.00]
# #  [2.00 0.00 0.00 ... 2.00 2.00 0.00]
# #  [0.00  nan 0.00 ... 1.00 2.00 0.00]]


# SNP matrix
# SNP (Single Nucleotide Polymorphism) matrix는 유전학, 생물정보학, 진화학 등 다양한 연구에서 유용하게 사용됩니다. 
# SNP matrix는 각 샘플의 특정 SNP 위치에서의 염기 서열(대립 유전자) 정보를 행렬 형태로 표현한 것입니다. 
# 이를 사용하는 주요 이유는 다음과 같습니다:

# 1. 유전자 다양성 분석
# SNP matrix는 집단 간 유전적 다양성을 비교하거나, 특정 집단 내 유전적 다양성을 측정하는 데 사용됩니다.
# 예를 들어, 인류 집단의 유전적 차이를 분석하거나, 특정 종의 유전적 변이를 평가하는 데 활용됩니다.

# 2. 계통수 및 진화 분석
# SNP 데이터를 기반으로 종이나 집단 간의 진화적 관계를 재구성할 수 있습니다.
# SNP matrix를 사용해 계통수(phylogenetic tree)를 생성하고, 진화 경로를 추적할 수 있습니다.

# 3. 질병 연관 연구
# SNP는 특정 질병과 관련된 유전자 변이를 찾는 데 중요한 역할을 합니다.
# SNP matrix를 사용해 질병 집단과 건강 집단 간 SNP 차이를 비교하고, 질병 관련 변이를 식별합니다.

# 4. 유전자 지도 작성
# SNP 데이터를 사용하여 염색체 상의 유전자 위치를 더 정확히 매핑할 수 있습니다.
# 이를 통해 특정 형질이나 질병과 관련된 유전자 위치를 식별합니다.

# 5. 개인 맞춤 의학
# SNP matrix는 개인 유전체 분석에 활용되어 약물 반응성, 유전적 질병 소인, 영양소 대사 등을 예측하는 데 기여합니다.
# 예를 들어, 특정 SNP를 기반으로 환자 맞춤형 치료를 설계합니다.

# 6. 집단 유전학 연구
# SNP matrix는 유전적 유사성과 차이를 기반으로 개체나 집단의 계통 발생, 혼합 정도, 이동 경로 등을 분석하는 데 사용됩니다.
# 인류의 역사적 이동 경로나 동식물의 진화 경로 연구에 활용됩니다.

# SNP Matrix 활용의 장점
# 표준화된 데이터 표현: SNP 데이터를 효율적으로 저장하고 분석할 수 있습니다.
# 다양한 분석 가능: 통계, 머신러닝, 네트워크 분석 등 다양한 기법을 적용할 수 있습니다.


# 1번재 방법 (pyvcf : 버젼이 안맞아서 import 불가가)
# import vcf

# def vcf_to_SNP_matrix(vcf_file):
#     # Read VCF file
#     vcf_data = vcf.Reader(open(vcf_file, 'r'))
    
#     # Extract SNP information
#     snp_info = []
#     for record in vcf_data:
#         snp_info.append([record.CHROM, record.POS, record.ID, record.REF, record.ALT])
    
#     # Extract sample information
#     sample_info = []
#     for sample in vcf_data.samples:
#         sample_info.append([sample.sample, sample.ID, sample.family_id, sample.paternal_id, sample.maternal_id, sample.gender, sample.phenotype])
    
#     # Extract genotype data
#     genotype_data = []
#     for record in vcf_data:
#         genotype_data.append([record.CHROM, record.POS, record.ID, record.REF, record.ALT] + [sample.genotype(record) for sample in vcf_data.samples])
    
#     # Convert genotype data to matrix
#     snp_matrix = np.array(genotype_data)[:, 3:]  # Extract SNP genotypes
    
#     return snp_info, sample_info, snp_matrix

# snp_info, sample_info, snp_matrix = vcf_to_SNP_matrix("example.vcf")

# print("SNP Information:")


# (1) Unmapped or Non-standard Chromosomes:
# 기준: 비표준 염색체 제거 (예: chrUn, random, alt, contig 등).
# 이유: 이러한 염색체는 보통 불완전한 데이터로 간주되며, 분석에 포함할 실질적 가치가 없습니다.

# (2) Mitochondrial or Chloroplast DNA:
# 기준: chrM(미토콘드리아), chloroplast 등의 염색체 제외.
# 이유: SNP 분석의 주요 목적이 핵 염색체에 한정될 경우, 이러한 데이터를 제외합니다.

# (3) Low SNP Density Regions:
# 기준: SNP가 거의 없는 염색체 제거.
# 이유: 분석에 기여하는 변이가 거의 없는 영역은 제거하여 계산 자원을 절약할 수 있습니다.

# (4) High Recombination or Structural Variability Regions:
# 기준: 높은 재조합율이나 구조적 변이가 많은 영역 제외.
# 이유: 해당 영역은 분석의 왜곡을 일으킬 가능성이 높습니다.

# (5) Chromosome Length:
# 기준: 특정 기준 이하의 짧은 contig 또는 scaffold 제거. (예: 길이 < 1Mb)
# 이유: 짧은 염색체는 대부분 비표준이며 분석의 신뢰도를 떨어뜨릴 수 있습니다.

# 3. SNP 레벨 필터링 기준 (추가적으로 적용 가능)
# (1) Minor Allele Frequency (MAF):
# 기준: MAF < 0.01인 변이 제외.
# 이유: 너무 희귀한 변이는 통계적으로 의미가 없을 수 있습니다.

# (2) Call Rate:
# 기준: SNP가 너무 많은 샘플에서 결측된 경우 제외. (예: Call rate < 90%)
# 이유: 데이터의 신뢰도를 높이기 위함.

# (3) Hardy-Weinberg Equilibrium (HWE):
# 기준: HWE에서 크게 벗어나는 SNP 제외.
# 이유: 비정상적인 데이터나 기술적 오류를 나타낼 수 있습니다.

# (4) Depth of Coverage per SNP:
# 기준: 특정 SNP의 평균 깊이가 너무 낮거나 높을 경우 제외. (예: DP < 5 또는 DP > 100)
# 이유: 낮은 깊이는 신뢰도가 낮고, 높은 깊이는 PCR 중복 가능성이 있습
# 니다.

# 2번째 방법 (pandas) https://pypi.org/project/vcf2pandas/

# pip install pandas
import pandas as pd

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

# VCF 파일 읽기
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
                SNP_num=f'SNP{chromosome + 1}'
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
                    final_format_dict ={'REF':REF_data, 'ALT':ALT_data, 'GT':format_dict["GT"], 'AD/DP':format_dict['AD']+"/"+format_dict['DP']}
                    sample_FormatData_List = final_format_dict
                    SAMPLE_Total_raw.append(sample_FormatData_List)
                SAMPLE_dic = dict(zip(sample_List, SAMPLE_Total_raw))
                SNP_data_Dict[sample_name][SNP_num]=SAMPLE_dic[sample_name]
        return SNP_data_Dict
      

# VCF_to_SNP_matrix("vcfExample.vcf")
# VCF_to_SNP_matrix("example.vcf")

# def VCF_to_SNP_matrix_reverse(vcf_file):
    # result_reverse_matrix ={}

    # result_matrix = VCF_to_SNP_matrix_reverse{vcf_file}
    # for sample_key, sample_value in result_matrix 
    # for SNP_key, SNP_value in sample_value 
    # sample_List =  result_matrix의 첫번째 key값
    # SNP_List = result_matrix의 샘플 내의 key값

    # ex) {SNP1:{sample1:{GT:' ', AD/DP:" / "},sample2:{GT:' ', AD/DP:" / "}, ...}}

    # for 문
    # result_reverse_matrix[SNP_List][sample_List] = SNP_value


def VCF_to_SNP_matrix_reverse(vcf_file):
    result_reverse_matrix ={}
    result_matrix = VCF_to_SNP_matrix(vcf_file)
    sample_List = []
    SNP_List = []

    SNP_keys = {}
    for sample_key, sample_value in result_matrix.items():
        sample_List.append(sample_key)
        SNP_keys=sample_value
        # SNP_List.append(sample_value)
    SNP_List=SNP_keys.keys()

    for SNP_key in SNP_List:
        for sample_key in sample_List:
            result_reverse_matrix.setdefault(SNP_key, {})
            result_reverse_matrix[SNP_key][sample_key] = result_matrix[sample_key][SNP_key]
    return result_reverse_matrix

# input
import re
def SNP_SNPmatrix_delete (vcf_file):
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


SNP_SNPmatrix_delete("Capsicum_GBS_191ea_Filtered_SNP_10009.vcf")

# 함수 tuple
# def SNP_SNPmatrix_delete (vcf_file, select_samples_List):
#     result_matrix = VCF_to_SNP_matrix(vcf_file)
#     sample_List = []
#     for sample_key, sample_value in result_matrix.items():
#         sample_List.append(sample_key)
#     delimiters = r'[,\s/\\]'
#     select_samples=re.split(delimiters, select_samples_List)
#     select_samples=[x for x in select_samples if x]
#     if len(select_samples) == 0:
#         return result_matrix
#     elif len(select_samples) == 1:
#         if select_samples[0] not in result_matrix:
#             return result_matrix
#         else:
#             del result_matrix[str(select_samples[0])]
#         return result_matrix
#     elif len(select_samples) >= 2:
#         for select_sample in select_samples:
#             if select_sample not in result_matrix:
#                 return result_matrix
#             else:
#                 print(f"{str(select_sample)}")
#                 del result_matrix[str(select_sample)]
#         return result_matrix
#     print(result_matrix)

# select_samples_List="24BB2-1-1/24BB2-1-2"

# SNP_SNPmatrix_delete("Capsicum_GBS_191ea_Filtered_SNP_10009.vcf", select_samples_List)


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
        # 샘플별 초기화
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





   


# vcf to SNP matrix 1 (sample - SNP)
VCF_to_SNP_matrix("Capsicum_GBS_191ea_Filtered_SNP_10009.vcf")
# vcf to SNP matrix 2 (SNP - sample)
VCF_to_SNP_matrix_reverse("Capsicum_GBS_191ea_Filtered_SNP_10009.vcf")
# vcf to SNP matrix 3 - input
SNP_SNPmatrix_delete("Capsicum_GBS_191ea_Filtered_SNP_10009.vcf")
# vcf to SNP matrix 3 - tuple
select_samples_List="24BB2-1-1/24BB2-1-2"
# SNP_SNPmatrix_delete("Capsicum_GBS_191ea_Filtered_SNP_10009.vcf", select_samples_List)
# vcf to SNP matrix 4 - SNP_Indel
SNP_matrix_SNP_Indel("SNPINDELexample.vcf", "etc")

# import xlwings as xw

# # 엑셀 파일 생성
# wb = xw.Book('example.xlsx')  # example.xlsx 파일이 생성됨

# # 워크시트 추가 (이름이 "Sheet1"인 워크시트 삭제)
# if "Sheet1" in wb.sheets:
#     wb.sheets["Sheet1"].delete()

# ws = wb.sheets.add('Sheet1')  # 새로운 워크시트 추가

# # 데이터 쓰기
# ws.range('A1').value = '이름'
# ws.range('B1').value = '나이'
# ws.range('A2').value = '박우리'
# ws.range('B2').value = 30
# ws.range('A3').value = '함자영'
# ws.range('B3').value = 25

# # 차트 생성
# chart = ws.charts.add()
# chart.set_source_data(ws.range('A1:B3'))
# chart.chart_type = 'column_clustered'
# chart.name = '나이별 차트'
# chart.title = '나이별 데이터'
# chart.x_axis.title = '이름'
# chart.y_axis.title = '나이'

# # 차트 위치 및 크기 조정
# chart.top = 'C1'
# chart.left = 'E1'
# chart.width = 400
# chart.height = 300

# # 엑셀 파일 저장 및 닫기
# wb.save()
# wb.close()

# # 차트 출력 완료 메시지
# print('엑셀 파일 생성 및 차트 작성이 완료되었습니다.')