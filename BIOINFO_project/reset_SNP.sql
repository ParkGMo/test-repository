CREATE DATABASE IF NOT EXISTS 'SNP_matrix';

CREATE TABLE IF NOT EXISTS 'SNP_matrix_results';
CREATE TABLE IF NOT EXISTS 'SNP_matrix_results_SNP';
CREATE TABLE IF NOT EXISTS 'SNP_matrix_results_Insert';
CREATE TABLE IF NOT EXISTS 'SNP_matrix_results_Delete';
CREATE TABLE IF NOT EXISTS 'SNP_matrix_results_Missing';
CREATE TABLE IF NOT EXISTS 'SNP_matrix_results_else';

CREATE TABLE IF NOT EXISTS 'SNP_matrix_results_reverse';
CREATE TABLE IF NOT EXISTS 'SNP_matrix_results_reverse_SNP';
CREATE TABLE IF NOT EXISTS 'SNP_matrix_results_reverse_Insert';
CREATE TABLE IF NOT EXISTS 'SNP_matrix_results_reverse_Delete';
CREATE TABLE IF NOT EXISTS 'SNP_matrix_results_reverse_Missing';
CREATE TABLE IF NOT EXISTS 'SNP_matrix_results_reverse_else';


{'SNP': 
    {'SAMPLE1': 
        {'SNP0': {'REF': 'A', 'ALT': 'G', 'GT': 'R', 'AD/DP': '50,50/100'}, 'SNP1': {'REF': 'C', 'ALT': 'T', 'GT': 'T', 'AD/DP': '0,120/120'}, 'SNP2': {'REF': 'G', 'ALT': 'A', 'GT': 'G', 'AD/DP': '110,0/110'}}, 
    'SAMPLE2': 
        {'SNP0': {'REF': 'A', 'ALT': 'G', 'GT': 'A', 'AD/DP': '100,0/100'}, 'SNP1': {'REF': 'C', 'ALT': 'T', 'GT': 'Y', 'AD/DP': '60,60/120'}, 'SNP2': {'REF': 'G', 'ALT': 'A', 'GT': 'G', 'AD/DP': '110,0/110'}}, 
    'SAMPLE3': 
        {'SNP0': {'REF': 'A', 'ALT': 'G', 'GT': 'G', 'AD/DP': '0,100/100'}, 'SNP1': {'REF': 'C', 'ALT': 'T', 'GT': 'C', 'AD/DP': '120,0/120'}, 'SNP2': {'REF': 'G', 'ALT': 'A', 'GT': 'A', 'AD/DP': '0,110/110'}}}, 
'Insert': 
    {'SAMPLE1': 
        {'SNP4': {'REF': 'A', 'ALT': 'AG', 'GT': 'N', 'AD/DP': '45,45/90'}, 'SNP6': {'REF': 'G', 'ALT': 'GTTA', 'GT': 'N', 'AD/DP': '42,43/85'}}, 
    'SAMPLE2': 
        {'SNP4': {'REF': 'A', 'ALT': 'AG', 'GT': 'N', 'AD/DP': '45,45/90'}, 'SNP6': {'REF': 'G', 'ALT': 'GTTA', 'GT': 'N', 'AD/DP': '0,85/85'}}, 
    'SAMPLE3': 
        {'SNP4': {'REF': 'A', 'ALT': 'AG', 'GT': 'N', 'AD/DP': '0,90/90'}, 'SNP6': {'REF': 'G', 'ALT': 'GTTA', 'GT': 'N', 'AD/DP': '85,0/85'}}}, 
'Delete': 
    {'SAMPLE1': 
        {'SNP5': {'REF': 'TT', 'ALT': 'T', 'GT': 'T', 'AD/DP': '0,88/88'}, 'SNP7': {'REF': 'AT', 'ALT': 'A', 'GT': 'A', 'AD/DP': '0,80/80'}}, 
    'SAMPLE2': 
        {'SNP5': {'REF': 'TT', 'ALT': 'T', 'GT': 'TT', 'AD/DP': '88,0/88'}, 'SNP7': {'REF': 'AT', 'ALT': 'A', 'GT': 'N', 'AD/DP': '40,40/80'}}, 
    'SAMPLE3': 
        {'SNP5': {'REF': 'TT', 'ALT': 'T', 'GT': 'N', 'AD/DP': '44,44/88'}, 'SNP7': {'REF': 'AT', 'ALT': 'A', 'GT': 'AT', 'AD/DP': '80,0/80'}}}, 
'Missing': 
    {'SAMPLE1': 
        {'SNP12': {'REF': 'T', 'ALT': '.', 'GT': 'T', 'AD/DP': '100,0/100'}}, 
    'SAMPLE2': 
        {'SNP12': {'REF': 'T', 'ALT': '.', 'GT': 'T', 'AD/DP': '100,0/100'}}, 
    'SAMPLE3': 
        {'SNP12': {'REF': 'T', 'ALT': '.', 'GT': 'T', 'AD/DP': '100,0/100'}}}, 
'else': 
    {'SAMPLE1': 
        {'SNP3': {'REF': 'T', 'ALT': 'C,G', 'GT': 'N', 'AD/DP': '25,40,40/105'}, 'SNP9': {'REF': 'A', 'ALT': '<DEL>', 'GT': 'N', 'AD/DP': '50,50/100'}, 'SNP10': {'REF': 'A', 'ALT': '<INS>', 'GT': 'N', 'AD/DP': '0,102/102'}, 'SNP11': {'REF': 'ATG', 'ALT': '<INV>', 'GT': 'N', 'AD/DP': '0,98/98'}, 'SNP13': {'REF': 'G', 'ALT': 'T,<DEL>', 'GT': 'N', 'AD/DP': '30,30,30/90'}, 'SNP14': {'REF': 'T', 'ALT': 'TG,TC', 'GT': 'N', 'AD/DP': '30,20,35/85'}}, 
    'SAMPLE2': 
        {'SNP3': {'REF': 'T', 'ALT': 'C,G', 'GT': 'N', 'AD/DP': '60,45,0/105'}, 'SNP9': {'REF': 'A', 'ALT': '<DEL>', 'GT': 'N', 'AD/DP': '0,100/100'}, 'SNP10': {'REF': 'A', 'ALT': '<INS>', 'GT': 'N', 'AD/DP': '102,0/102'}, 'SNP11': {'REF': 'ATG', 'ALT': '<INV>', 'GT': 'N', 'AD/DP': '0,98/98'}, 'SNP13': {'REF': 'G', 'ALT': 'T,<DEL>', 'GT': 'N', 'AD/DP': '45,45,0/90'}, 'SNP14': {'REF': 'T', 'ALT': 'TG,TC', 'GT': 'N', 'AD/DP': '0,0,85/85'}}, 
    'SAMPLE3': 
        {'SNP3': {'REF': 'T', 'ALT': 'C,G', 'GT': 'N', 'AD/DP': '0,0,105/105'}, 'SNP9': {'REF': 'A', 'ALT': '<DEL>', 'GT': 'N', 'AD/DP': '100,0/100'}, 'SNP10': {'REF': 'A', 'ALT': '<INS>', 'GT': 'N', 'AD/DP': '51,51/102'}, 'SNP11': {'REF': 'ATG', 'ALT': '<INV>', 'GT': 'N', 'AD/DP': '98,0/98'}, 'SNP13': {'REF': 'G', 'ALT': 'T,<DEL>', 'GT': 'N', 'AD/DP': '0,0,90/90'}, 'SNP14': {'REF': 'T', 'ALT': 'TG,TC', 'GT': 'N', 'AD/DP': '43,42,0/85'}}}}