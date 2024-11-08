Bulk RNAseq Analysis
====================
Derek Breton

-  [Introduction](#introduction)
-  [Methods](#methods)
-  [Results](#results)
    -  [PCA plot](#pca-plot)
    -  [Differential expression analysis](#differential-expression-analysis)
    -  [Gene set enrichment analysis](#gene-set-enrichment-analysis)  



Introduction
------------


Methods
-------
RNA sequencing data were obtained from 3 healthy and 6 COVID-19 infected human derived samples. Among the 6 infected patients, 3 were characterized as having a severe infection, but not requiring hospitalization in an intensive care unit (ICU), and 3 were characterized as having a severe infection that required hospitalization in an ICU. Quality control was ititially performed on the samples using FastQC v0.12.1-0 [1]. Transcript abundance was quantified using Kallisto v0.50.0 [2]. First, a Kallisto index was constructed from a combined FASTA file of cDNA and ncRNA sequences downloaded from Ensembl GRCh38 (release 113). The FASTA files were merged and indexed with Kallisto using default k-mer length. Raw RNA-Seq paired end reads were pseudo-aligned to the reference index using Kallisto’s quant function with 50 bootstrap samples and all other parameters set to default settings. Transcript abundance estimates were output as transcript per million (TPM) and estimated counts. These quantifications were then used for downstream analysis. Differential expression analysis and principal component analysis (PCA) were performed using DESeq2 v1.42.0 [3] using default parameters. Gene set enrichment analysis (GSEA) was performed using FGSEA v1.28.0 [4] using log2foldchange as a ranking metric and MSigDB C2 cannonical pathways [5]. Enrichment analysis was performed using DAVID v6.8 [6].

Results
-------

### PCA plot


### Differential expression analysis


### Gene set enrichment analysis


## Citations
1. https://www.bioinformatics.babraham.ac.uk/projects/fastqc/
2. https://www.nature.com/articles/nbt.3519
3. https://genomebiology.biomedcentral.com/articles/10.1186/s13059-014-0550-8
4. http://biorxiv.org/content/early/2016/06/20/060012
5. https://www.gsea-msigdb.org/gsea/msigdb/human/genesets.jsp?collection=CP
6. https://david.ncifcrf.gov/
