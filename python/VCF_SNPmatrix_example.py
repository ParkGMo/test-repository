import os
print("현재 작업 디렉토리:", os.getcwd())

# VCF to SNP Matrix Conversion (chat GPT)
import pandas as pd

def vcf_to_snp_matrix(vcf_file):
    snp_matrix = []
    sample_names = []

    with open(vcf_file, 'r') as file:
        for line in file:
            if line.startswith("##"):
                continue
            elif line.startswith("#CHROM"):
                header = line.strip().split('\t')
                sample_names = header[9:]
            else:
                columns = line.strip().split('\t')
                chrom, pos, _, ref, alt, _, _, info, format_, *samples = columns

                # Parse genotype information
                genotypes = []
                for sample in samples:
                    genotype = sample.split(':')[0]  # Extract genotype (GT)
                    alleles = genotype.replace('|', '/').split('/')
                    genotypes.append(''.join([ref if allele == '0' else alt.split(',')[int(allele)-1] for allele in alleles if allele != '.']))

                snp_matrix.append([f"{chrom}:{pos}"] + genotypes)

    # Create DataFrame
    df = pd.DataFrame(snp_matrix, columns=["Variant"] + sample_names)
    return df

# Example usage
vcf_file = "vcfExample.vcf"  # Replace with your VCF file path
snp_matrix_df = vcf_to_snp_matrix(vcf_file)

# Save SNP matrix to a file
snp_matrix_df.to_csv("vcfExample.vcf", index=False)
print(snp_matrix_df)


import pandas as pd

# VCF 파일 읽기
def VCF_to_SNP_matrix(vcf_file):
    with open(vcf_file, 'r') as file:
        lines = file.readlines()

        # 메타데이터와 데이터 분리
        metadata = [line for line in lines if line.startswith('##')]
        header_line = [line for line in lines if line.startswith('#') and not line.startswith('##')]
        data_lines = [line for line in lines if not line.startswith('#')]
        # 컬럼 헤더 추출
        header = header_line[0].strip().split('\t')

        # 데이터프레임 생성
        # pd.DataFrame 함수(a,b): a는 불러올 데이터 : b는 dataframe의 column name을 열로 변환환
        data = [line.strip().split('\t') for line in data_lines]
        df = pd.DataFrame(data, columns=header)

        # 데이터프레임 확인
        # head()는 pandas에서 데이터확인하는 방법으로 dataframe의 처음 n줄데이터를 출력 
        print(df.head())
        # tail()는 dataframe의 마지막 n줄 데이터를 출력

        # 'CHROM' 열의 값 확인
        # nunique()는 데이터에 고유값들의 수를 출력해주는 함수
        print(df['#CHROM'].unique())

VCF_to_SNP_matrix("example.vcf")