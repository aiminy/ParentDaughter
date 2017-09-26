# ParentDaughter 

A pipeline for calling and anotating SNP using parent and daughter sequence data of bacteria  

## Set up environment

```{r set_up,eval=FALSE,echo=TRUE}
Python 2.7.13
R 3.4.1
bowtie2-build
picard
bowtie2
bcftools
seqtk
bedops
Java1.8.0_121

# it is better install conda, set bioconda channel, install some software as the following example
conda install -c bioconda seqtk

```

## Install ParentDaughter
```{r install}

# Install release version
# You need install devtools R package
install.packages("devtools")

# Then
R -e 'library(devtools);install_github("aiminy/ParentDaughter")'

# Install ver.0.1.0 
R -e 'library(devtools);install_github("SCCC-BBC/PathwaySplice",ref="ver.0.1.0")'
```

## Use ParentDaughter

```{r eval=FALSE}
# Usage:
# Suppose you install R in your home directry
python $HOME/R/x86_64-pc-linux-gnu-library/3.4/ParentDaughter/bin/python/Test.py -h
```

## Output from running as bash model

### Run as bash model

Assume you download all files into
```{r}
/media/H_driver/Aimin_project/Bioinformatics_Assessment directory
```

Then you can run bash model as the following

```{r}
python R/x86_64-pc-linux-gnu-library/3.4/ParentDaughter/bin/python/script3.py B /media/H_driver/Aimin_project/Bioinformatics_Assessment
```
You will get ouptuts like:

```{r}
run as bash model
Building a SMALL index
440100 reads; of these:
  440100 (100.00%) were paired; of these:
    230255 (52.32%) aligned concordantly 0 times
    206736 (46.97%) aligned concordantly exactly 1 time
    3109 (0.71%) aligned concordantly >1 times
    ----
    230255 pairs aligned concordantly 0 times; of these:
      61930 (26.90%) aligned discordantly 1 time
    ----
    168325 pairs aligned 0 times concordantly or discordantly; of these:
      336650 mates make up the pairs; of these:
        324714 (96.45%) aligned 0 times
        10076 (2.99%) aligned exactly 1 time
        1860 (0.55%) aligned >1 times
63.11% overall alignment rate
Picked up _JAVA_OPTIONS: -Xms512m -Xmx2048m
19:41:19.111 INFO  NativeLibraryLoader - Loading libgkl_compression.so from jar:file:/home/aiminyan/miniconda3/envs/bds_atac/share/picard-2.11.0-0/picard.jar!/com/intel/gkl/native/libgkl_compression.so
[Mon Sep 25 19:41:19 EDT 2017] SortSam INPUT=/media/H_driver/Aimin_project/Bioinformatics_Assessment/parent.bam OUTPUT=/media/H_driver/Aimin_project/Bioinformatics_Assessment/parent_sorted.bam SORT_ORDER=coordinate    VERBOSITY=INFO QUIET=false VALIDATION_STRINGENCY=STRICT COMPRESSION_LEVEL=5 MAX_RECORDS_IN_RAM=500000 CREATE_INDEX=false CREATE_MD5_FILE=false GA4GH_CLIENT_SECRETS=client_secrets.json USE_JDK_DEFLATER=false USE_JDK_INFLATER=false
[Mon Sep 25 19:41:19 EDT 2017] Executing as aiminyan@aiminyan-Precision-Tower-5810 on Linux 4.4.0-96-generic amd64; Java HotSpot(TM) 64-Bit Server VM 1.8.0_144-b01; Deflater: Intel; Inflater: Intel; Picard version: 2.11.0-SNAPSHOT
INFO	2017-09-25 19:41:28	SortSam	Finished reading inputs, merging and writing to output now.
[Mon Sep 25 19:41:39 EDT 2017] picard.sam.SortSam done. Elapsed time: 0.34 minutes.
Runtime.totalMemory()=1510998016
Note: none of --samples-file, --ploidy or --ploidy-file given, assuming all sites are diploid
[mpileup] 1 samples in 1 input files
<mpileup> Set max per-file depth to 8000

Building a SMALL index
649982 reads; of these:
  649982 (100.00%) were paired; of these:
    331778 (51.04%) aligned concordantly 0 times
    313698 (48.26%) aligned concordantly exactly 1 time
    4506 (0.69%) aligned concordantly >1 times
    ----
    331778 pairs aligned concordantly 0 times; of these:
      82191 (24.77%) aligned discordantly 1 time
    ----
    249587 pairs aligned 0 times concordantly or discordantly; of these:
      499174 mates make up the pairs; of these:
        486841 (97.53%) aligned 0 times
        10078 (2.02%) aligned exactly 1 time
        2255 (0.45%) aligned >1 times
62.55% overall alignment rate
Picked up _JAVA_OPTIONS: -Xms512m -Xmx2048m
19:50:27.357 INFO  NativeLibraryLoader - Loading libgkl_compression.so from jar:file:/home/aiminyan/miniconda3/envs/bds_atac/share/picard-2.11.0-0/picard.jar!/com/intel/gkl/native/libgkl_compression.so
[Mon Sep 25 19:50:27 EDT 2017] SortSam INPUT=/media/H_driver/Aimin_project/Bioinformatics_Assessment/daughter.bam OUTPUT=/media/H_driver/Aimin_project/Bioinformatics_Assessment/daughter_sorted.bam SORT_ORDER=coordinate    VERBOSITY=INFO QUIET=false VALIDATION_STRINGENCY=STRICT COMPRESSION_LEVEL=5 MAX_RECORDS_IN_RAM=500000 CREATE_INDEX=false CREATE_MD5_FILE=false GA4GH_CLIENT_SECRETS=client_secrets.json USE_JDK_DEFLATER=false USE_JDK_INFLATER=false
[Mon Sep 25 19:50:27 EDT 2017] Executing as aiminyan@aiminyan-Precision-Tower-5810 on Linux 4.4.0-96-generic amd64; Java HotSpot(TM) 64-Bit Server VM 1.8.0_144-b01; Deflater: Intel; Inflater: Intel; Picard version: 2.11.0-SNAPSHOT
INFO	2017-09-25 19:50:40	SortSam	Finished reading inputs, merging and writing to output now.
[Mon Sep 25 19:50:53 EDT 2017] picard.sam.SortSam done. Elapsed time: 0.44 minutes.
Runtime.totalMemory()=1530920960
Note: none of --samples-file, --ploidy or --ploidy-file given, assuming all sites are diploid
[mpileup] 1 samples in 1 input files
<mpileup> Set max per-file depth to 8000

Your results is in /media/H_driver/Aimin_project/Bioinformatics_Assessment/ann.vcf 
```
### Run as interactive model

you can run interactive model as the following
 ```{r}
python $HOME/R/x86_64-pc-linux-gnu-library/3.4/ParentDaughter/bin/python/script3.py I /media/H_driver/Aimin_project/Bioinformatics_Assessment
```
After this, you will ask to give 
```{r}
Enter ref genomeFile: /media/H_driver/Aimin_project/Bioinformatics_Assessment/GCF_000005845.2_ASM584v2_genomic.fna

Enter ref genomeIndex: /media/H_driver/Aimin_project/Bioinformatics_Assessment/dog

Enter parent fq1: /media/H_driver/Aimin_project/Bioinformatics_Assessment/sample-1_S1_L001_R1_001.fastq.gz

Enter parent fq2: /media/H_driver/Aimin_project/Bioinformatics_Assessment/sample-1_S1_L001_R2_001.fastq.gz

Enter parent outSam: /media/H_driver/Aimin_project/Bioinformatics_Assessment/parent2.sam        

Building a SMALL index
440100 reads; of these:
  440100 (100.00%) were paired; of these:
    230255 (52.32%) aligned concordantly 0 times
    206736 (46.97%) aligned concordantly exactly 1 time
    3109 (0.71%) aligned concordantly >1 times
    ----
    230255 pairs aligned concordantly 0 times; of these:
      61930 (26.90%) aligned discordantly 1 time
    ----
    168325 pairs aligned 0 times concordantly or discordantly; of these:
      336650 mates make up the pairs; of these:
        324714 (96.45%) aligned 0 times
        10076 (2.99%) aligned exactly 1 time
        1860 (0.55%) aligned >1 times
63.11% overall alignment rate

Picked up _JAVA_OPTIONS: -Xms512m -Xmx2048m
21:08:22.290 INFO  NativeLibraryLoader - Loading libgkl_compression.so from jar:file:/home/aiminyan/miniconda3/envs/bds_atac/share/picard-2.11.0-0/picard.jar!/com/intel/gkl/native/libgkl_compression.so

[Sat Sep 23 21:08:22 EDT 2017] SortSam INPUT=/media/H_driver/Aimin_project/Bioinformatics_Assessment/parent2.bam OUTPUT=/media/H_driver/Aimin_project/Bioinformatics_Assessment/parent2_sorted.bam SORT_ORDER=coordinate    VERBOSITY=INFO QUIET=false VALIDATION_STRINGENCY=STRICT COMPRESSION_LEVEL=5 MAX_RECORDS_IN_RAM=500000 CREATE_INDEX=false CREATE_MD5_FILE=false GA4GH_CLIENT_SECRETS=client_secrets.json USE_JDK_DEFLATER=false USE_JDK_INFLATER=false

[Sat Sep 23 21:08:22 EDT 2017] Executing as aiminyan@aiminyan-Precision-Tower-5810 on Linux 4.4.0-96-generic amd64; Java HotSpot(TM) 64-Bit Server VM 1.8.0_144-b01; Deflater: Intel; Inflater: Intel; Picard version: 2.11.0-SNAPSHOT
INFO	2017-09-23 21:08:31	SortSam	Finished reading inputs, merging and writing to output now.

[Sat Sep 23 21:08:43 EDT 2017] picard.sam.SortSam done. Elapsed time: 0.36 minutes.
Runtime.totalMemory()=1456996352
Note: none of --samples-file, --ploidy or --ploidy-file given, assuming all sites are diploid
[mpileup] 1 samples in 1 input files
<mpileup> Set max per-file depth to 8000

Well done, finish creating a consensus of the parent ! 

Enter parent consensus file: /media/H_driver/Aimin_project/Bioinformatics_Assessment/parent2_consensus.fna

Enter parent genomeIndex: /media/H_driver/Aimin_project/Bioinformatics_Assessment/dog2

Enter daughter fq1: /media/H_driver/Aimin_project/Bioinformatics_Assessment/sample-2_S6_L001_R1_001.fastq.gz

Enter daughter fq2: /media/H_driver/Aimin_project/Bioinformatics_Assessment/sample-2_S6_L001_R2_001.fastq.gz

Enter daughter outSam: /media/H_driver/Aimin_project/Bioinformatics_Assessment/daughter2.sam

Enter gff file:/media/H_driver/Aimin_project/Bioinformatics_Assessment/GCF_000005845.2_ASM584v2_genomic.gff

Building a SMALL index

649982 reads; of these:
  649982 (100.00%) were paired; of these:
    331778 (51.04%) aligned concordantly 0 times
    313698 (48.26%) aligned concordantly exactly 1 time
    4506 (0.69%) aligned concordantly >1 times
    ----
    331778 pairs aligned concordantly 0 times; of these:
      82191 (24.77%) aligned discordantly 1 time
    ----
    249587 pairs aligned 0 times concordantly or discordantly; of these:
      499174 mates make up the pairs; of these:
        486841 (97.53%) aligned 0 times
        10078 (2.02%) aligned exactly 1 time
        2255 (0.45%) aligned >1 times
62.55% overall alignment rate
Picked up _JAVA_OPTIONS: -Xms512m -Xmx2048m
12:09:59.883 INFO  NativeLibraryLoader - Loading libgkl_compression.so from jar:file:/home/aiminyan/miniconda3/envs/bds_atac/share/picard-2.11.0-0/picard.jar!/com/intel/gkl/native/libgkl_compression.so
[Sun Sep 24 12:09:59 EDT 2017] SortSam INPUT=/media/H_driver/Aimin_project/Bioinformatics_Assessment/daughter2.bam OUTPUT=/media/H_driver/Aimin_project/Bioinformatics_Assessment/daughter2_sorted.bam SORT_ORDER=coordinate    VERBOSITY=INFO QUIET=false VALIDATION_STRINGENCY=STRICT COMPRESSION_LEVEL=5 MAX_RECORDS_IN_RAM=500000 CREATE_INDEX=false CREATE_MD5_FILE=false GA4GH_CLIENT_SECRETS=client_secrets.json USE_JDK_DEFLATER=false USE_JDK_INFLATER=false
[Sun Sep 24 12:09:59 EDT 2017] Executing as aiminyan@aiminyan-Precision-Tower-5810 on Linux 4.4.0-96-generic amd64; Java HotSpot(TM) 64-Bit Server VM 1.8.0_144-b01; Deflater: Intel; Inflater: Intel; Picard version: 2.11.0-SNAPSHOT
INFO	2017-09-24 12:10:10	SortSam	Finished reading inputs, merging and writing to output now.
[Sun Sep 24 12:10:23 EDT 2017] picard.sam.SortSam done. Elapsed time: 0.39 minutes.
Runtime.totalMemory()=1427111936
[fai_load] build FASTA index.
Note: none of --samples-file, --ploidy or --ploidy-file given, assuming all sites are diploid
[mpileup] 1 samples in 1 input files
<mpileup> Set max per-file depth to 8000
```
