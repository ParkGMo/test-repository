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
from os.path import join
from pandas_plink import read_plink
from pandas_plink import get_data_folder
(bim, fam, bed) = read_plink(join(get_data_folder(), "chr*.bed"),
                             verbose=False)
print(bim.head())
#   chrom        snp       cm     pos a0 a1  i
# 0    11  316849996     0.00  157439  C  T  0
# 1    11  316874359     0.00  181802  G  C  1
# 2    11  316941526     0.00  248969  G  C  2
# 3    11  317137620     0.00  445063  C  T  3
# 4    11  317534352     0.00  841795  C  T  4
print(fam.head())
#     fid   iid father mother gender trait  i
# 0  B001  B001      0      0      0    -9  0
# 1  B002  B002      0      0      0    -9  1
# 2  B003  B003      0      0      0    -9  2
# 3  B004  B004      0      0      0    -9  3
# 4  B005  B005      0      0      0    -9  4
print(bed.compute())
# [[0.00 0.00 0.00 ... 2.00 2.00 0.00]
#  [0.00 1.00 0.00 ... 2.00 1.00 0.00]
#  [2.00 2.00 2.00 ... 0.00 0.00 2.00]
#  ...
#  [2.00 0.00 0.00 ... 2.00 2.00 1.00]
#  [2.00 0.00 0.00 ... 2.00 2.00 0.00]
#  [0.00  nan 0.00 ... 1.00 2.00 0.00]]


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
import os
print("현재 작업 디렉토리:", os.getcwd())

# content=""
# try:
#     with open("example.txt", "r") as file:
#         content = file.read()
#     print(content)
# except FileNotFoundError:
#     print("example.txt 파일이 현재 디렉토리에 없습니다.")

# print(content)

# Pseudo Code
# base_code_map = {
#     ('A', 'T'): 'W', ('T', 'A'): 'W', # A or T
#     ('C', 'G'): 'S', ('G', 'C'): 'S', # G or C
#     ('A', 'C'): 'M', ('C', 'A'): 'M', # A or C
#     ('G', 'T'): 'K', ('T', 'G'): 'K', # G or T
#     ('A', 'G'): 'R', ('G', 'A'): 'R', # A or G
#     ('C', 'T'): 'Y', ('T', 'C'): 'Y'  # C or T
# }
# def get_base_code(base1, base2):
#     pair = (base1, base2)
#     return base_code_map.get(pair, 'N') 

# 1. VCF 파일을 DataFrame으로 변환
# def  VCF_to_SNP_matrix(불러올 파일):
    # 1-1 파일을 불러온다.
    # with open(불러올파일, 'r' )as file:
    #     라인들을 불러온다
        
    #     # 1-2 라인을 불러온다.
    #     metaLine = ## 들어있는 라인을 가져온다.
    #     headerLine = # 들어있는 라인을 가져온다.(header)
    #     dataLine = #이 없는 라인을 가져온다.(data)

    #     # 1-3 라인의 헤더에서 단어만 가져온다.
    #     header= 헤더 값만 리스트로 가져온다.

    #     # 1-4 염색체 하나의 필요한 data를 샘플마다 모든 data를 정제하여여 가져온다.
    #     SNP_data_dict={smaple1:{CHROM POS ID REF ALT GT AD/DP}, smaple2:{CHROM POS ALT ID REF GT AD/DP}}
    #     for sample in range(len(header_samples)):
    #       CHROM = dataLine[해당하는 위치], SNP_data_Dict[sample] 
    #       POS = dataLine[해당하는 위치], SNP_data_Dict[sample] 
    #       ID = dataLine[해당하는 위치], SNP_data_Dict[sample] 
    #       REF = dataLine[해당하는 위치] 
    #       ALT = dataLine[해당하는 위치] 
    #       FILTER = dataLine[해당하는 위치] , SNP_data_Dict[sample]  
    #       INFO = dataLine[해당하는 위치] , SNP_data_Dict[sample]  
    #       FORMAT = dataLine[해당하는 위치] , SNP_data_Dict[sample]  
    #       SAMPLE_data = dataLine[해당하는 위치] - split(":") - SAMPLE_List
    #       GT = SAMPLE_List[해당하는 위치] 
    #       AD = SAMPLE_List[해당하는 위치] 
    #       DP = SAMPLE_List[해당하는 위치] 
    #       GQ = SAMPLE_List[해당하는 위치] 
    #       PL = SAMPLE_List[해당하는 위치] 
    
    #       REF ALT염기서열을 get_base_code(base1, base2)를 통해 하나의의 코드로 변환 
    #         if GT=="0/0": REF_homo값 = REF
    #           elif GT=="0/1" or GT=="1/0": hetero 값 = get_base_code(base1, base2)
    #           elif GT=="1/1' : ALT_homo값 = ALT
    #       
    #       AD/DP = ":" 을 "/"로 바꾼다

    #       1-5 SNP_data_dict를 제작 완료
    #       SNP_data_dict={smaple1:{CHROM POS ID REF ALT GT AD/DP}, smaple2:{CHROM POS ALT ID REF GT AD/DP}}


    #       print(dataList)

# 2. 샘플 순서서 변환 ...




# 2번째 방법 (pandas) https://pypi.org/project/vcf2pandas/
# pip install pandas
import pandas as pd

# 염기 조합을 코드로 매핑
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

        # 메타데이터와 데이터 분리
        metadata = [line for line in lines if line.startswith('##')]
        header_line = [line for line in lines if line.startswith('#') and not line.startswith('##')]
        data_lines = [line for line in lines if not line.startswith('#')]
        # print(f'metadata: {metadata} Header: {header_line}  Data: {data_lines}')
        # 헤더 추출
        # header = header_line[0].strip().split('\t')[0].split(' ')
        header = header_line[0].strip().split('\t')
        header_title= list(filter(lambda x: len(x)>1,header))
        # 샘플 추출
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
                # print(f'SNP data List: {SNP_data_Dict}')
                # datas = data_lines[chromosome].strip().split('\t')[0].split(' ')
                datas = data_lines[chromosome].strip().split('\t')
                data_values = list(filter(lambda x: len(x)>=1,datas))
                # print(data_values)
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
                # SNP_data_Dict[sample_name][SNP_num]["QUAL"]=QUAL_data
                INFO_data=data_values[7]
                # SNP_data_Dict[sample_name][SNP_num]["INFO"]=INFO_data

                FORMAT_raw=data_values[8]
                FORMAT_list=FORMAT_raw.split(':')
                # print (f"FORMAT {FORMAT_list}")
                # SNP_data_Dict["FORMAT"]=FORMAT_data
                # 
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
                        GT_data="N"
                    final_format_dict ={'GT':format_dict["GT"], 'AD/DP':format_dict['AD']+"/"+format_dict['DP']}
                    sample_FormatData_List = final_format_dict
                    SAMPLE_Total_raw.append(sample_FormatData_List)
                SAMPLE_dic = dict(zip(sample_List, SAMPLE_Total_raw))
                
        #         SNP_data_Dict[sample_name][SNP_num]["GT"]=GT_data
                # ADDP=f'{AD_value}/{DP_value}'
        #         SNP_data_Dict[sample_name][SNP_num]['AD/DP']=ADDP
                SNP_data_Dict[sample_name][SNP_num]=SAMPLE_dic[sample_name]

        print(SNP_data_Dict)

# #               샘플 하나의 여러 염색체 표(사전(샘플) - 사전(SNP) - 사전(data))
# #               SNP_data_dict=
# #                             {smaple1:{SNP1:{CHROM POS ID REF ALT GT AD/DP},
# #                                       SNP2:{CHROM POS ID REF ALT GT AD/DP},
# #                                       SNP3:{CHROM POS ID REF ALT GT AD/DP}}, 
# #                              smaple2:{SNP1:{CHROM POS ID REF ALT GT AD/DP},
# #                                       SNP2:{CHROM POS ID REF ALT GT AD/DP}}




# VCF_to_SNP_matrix("vcfExample.vcf")
VCF_to_SNP_matrix("Capsicum_GBS_191ea_Filtered_SNP_10009.vcf")
