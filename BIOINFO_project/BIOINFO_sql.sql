CREATE DATABASE IF NOT EXISTS 'SNP_matrix';
CREATE DATABASE "SNP_matrix";
CREATE TABLE IF NOT EXISTS 'SNP_matrix_results';
CREATE TABLE "SNP_matrix_results" ('SNP' VARCHAR(100), 'SAMPLE1' VARCHAR(2), 'SAMPLE2' VARCHAR(2));
CREATE TABLE IF NOT EXISTS 'SNP_matrix_results_reverse';
CREATE TABLE "SNP_matrix_results_reverse" ('SAMPLE' VARCHAR(100), 'SNP1' VARCHAR(2), 'SNP2' VARCHAR(2));
