#!/usr/bin/env python2

# Usage: python R/x86_64-pc-linux-gnu-library/3.4/ParentDaughter/bin/python/Test.py -h

import os
import ntpath
import subprocess
import argparse

# install seqtk from bioconda
bashCommand = "conda install -c bioconda seqtk"
output = subprocess.check_output(['bash','-c', bashCommand])

# Set memory
bashCommand='export _JAVA_OPTIONS="-Xms512m -Xmx2048m"'
output = subprocess.check_output(['bash','-c', bashCommand])

def getBam(genomeFile,genomeIndex,fq1,fq2,outSam):

    # build index
    bashCommand = "bowtie2-build " + genomeFile + " " + genomeIndex
    output = subprocess.check_output(['bash','-c', bashCommand])

    # Perform alignment
    bashCommand = "bowtie2 -x " + genomeIndex + " -1 " + fq1 + " -2 " + fq2 + " -S " + outSam
    output = subprocess.check_output(['bash','-c', bashCommand])

    # convert sam to bam
    path = os.path.dirname(outSam)
    sname = os.path.splitext(ntpath.basename(outSam))[0]

    bashCommand = "samtools view -b " + outSam + " > " + path + "/" + sname + ".bam"
    output = subprocess.check_output(['bash','-c', bashCommand])

    # Sort bam
    bashCommand= "picard SortSam I=" + path + "/" + sname + ".bam" + " O="+ path + "/" + sname + "_sorted.bam" + " SORT_ORDER=coordinate"
    output = subprocess.check_output(['bash','-c', bashCommand])

    # Index bam
    bashCommand = "samtools index " + path + "/" + sname + "_sorted.bam"
    output = subprocess.check_output(['bash','-c', bashCommand])

def BashMode(Input):


    genomeFile = Input + "/" + "GCF_000005845.2_ASM584v2_genomic.fna"
    genomeIndex = Input + "/" + "genomeIndex"
    fq1 = Input + "/" + "sample-1_S1_L001_R1_001.fastq.gz"
    fq2 = Input + "/" + "sample-1_S1_L001_R2_001.fastq.gz"
    outSam = Input + "/" + "parent.sam"

    getBam(genomeFile,genomeIndex,fq1,fq2,outSam)

    # Get consensus.fastq
    bashCommand = "samtools mpileup -uf " + Input +"/" + "GCF_000005845.2_ASM584v2_genomic.fna " + Input + "/"+"parent.sorted.bam | bcftools call -c | vcfutils.pl vcf2fq > " + Input+ "/"+"consensus.fastq"
    output = subprocess.check_output(['bash','-c', bashCommand])

    # Get consensus.fna
    bashCommand = "seqtk seq -A " + Input + "/" + "consensus.fastq > "+ Input + "/"+ "consensus.fna"
    output = subprocess.check_output(['bash','-c', bashCommand])

    genomeFile = Input + "/"+ "consensus.fna"
    genomeIndex = Input + "/" + "genomeIndex2"
    fq1 = Input + "/" +  "sample-2_S6_L001_R1_001.fastq.gz"
    fq2 = Input + "/" + "sample-2_S6_L001_R2_001.fastq.gz"
    outSam = Input + "/" + "daughter.sam"

    getBam(genomeFile,genomeIndex,fq1,fq2,outSam)

    bashCommand = "samtools mpileup -uf "+Input+"/"+"consensus.fna " + Input + "/"+"daughter.sorted.bam | bcftools call -mv -Oz > " + Input +"/"+"daughter.raw.vcf.gz"
    output = subprocess.check_output(['bash','-c', bashCommand])

    bashCommand = "gff2bed < " + Input + "/"+"GCF_000005845.2_ASM584v2_genomic.gff" + " > " + Input + "/" + "GCF_000005845.2_ASM584v2_genomic.bed"
    output = subprocess.check_output(['bash','-c', bashCommand])

    bashCommand = "tabix -s1 -b2 -e3 -f "+ Input +"/"+"GCF_000005845.2_ASM584v2_genomic.bed.gz"
    output = subprocess.check_output(['bash','-c', bashCommand])

    bashCommand = "bcftools annotate -a "+ Input+ "/"+"GCF_000005845.2_ASM584v2_genomic.bed.gz -c CHROM,FROM,TO,ID "+ Input + "/"+"daughter.raw.vcf.gz > "+ Input+ "/"+"ann.vcf"
    output = subprocess.check_output(['bash','-c', bashCommand])

    out = Input + "/"+"ann.vcf"
    print "Your results is in %s " % (out)

def InteractiveModel():

    genomeFile = raw_input("Enter ref genomeFile: ")
    genomeIndex = raw_input("Enter ref genomeIndex: ")
    fq1 = raw_input("Enter parent fq1: ")
    fq2 = raw_input("Enter parent fq2: ")
    outSam =  raw_input("Enter parent outSam: ")

    getBam(genomeFile,genomeIndex,fq1,fq2,outSam)

    path = os.path.dirname(outSam)
    sname = os.path.splitext(ntpath.basename(outSam))[0]

    # Get parent consensus.fastq
    bashCommand = "samtools mpileup -uf " + genomeFile + " " + path + "/" + sname + "_sorted.bam" + " | bcftools call -c | vcfutils.pl vcf2fq > " + path + "/" + sname + "_consensus.fastq"
    output = subprocess.check_output(['bash','-c', bashCommand])

    #Get parent consensus.fna
    bashCommand = "seqtk seq -A " + path + "/" + sname + "_consensus.fastq" + " > " + path + "/" + sname + "_consensus.fna"
    output = subprocess.check_output(['bash','-c', bashCommand])

    print "Well done, finish creating a consensus of the parent ! \n"

    genomeFile = raw_input("Enter parent consensus file: ")
    genomeIndex = raw_input("Enter parent genomeIndex: ")
    fq1 = raw_input("Enter daughter fq1: ")
    fq2 = raw_input("Enter daughter fq2: ")
    outSam =  raw_input("Enter daughter outSam: ")
    gff = raw_input("Enter gff file:")

    pathd = os.path.dirname(outSam)
    snamed = os.path.splitext(ntpath.basename(outSam))[0]

    getBam(genomeFile,genomeIndex,fq1,fq2,outSam)

    bashCommand = "samtools mpileup -uf " + path + "/" + sname + "_consensus.fna " + pathd + "/" + snamed + "_sorted.bam" + " | bcftools call -mv -Oz > " + pathd + "/"+ snamed + "_raw.vcf.gz"
    output = subprocess.check_output(['bash','-c', bashCommand])

    gffpath = os.path.dirname(gff)
    gffname = os.path.splitext(ntpath.basename(gff))[0]

    bashCommand = "gff2bed < " + gff + " > " + gffpath + "/"+ gffname + ".bed"
    output = subprocess.check_output(['bash','-c', bashCommand])

    bashCommand = "tabix -s1 -b2 -e3 -f " + gffpath + "/"+ gffname + ".bed.gz"
    output = subprocess.check_output(['bash','-c', bashCommand])

    bashCommand = "bcftools annotate -a " + gffpath + "/"+ gffname + ".bed.gz" + " -c CHROM,FROM,TO,ID " + pathd + "/"+ snamed + "_raw.vcf.gz" +  " > " + pathd + "/" + "ann.vcf"
    output = subprocess.check_output(['bash','-c', bashCommand])

    out = pathd + "/"+"ann.vcf"
    print "Your results is in %s " % (out)

def main():

    parser = argparse.ArgumentParser(description="ParentDaughter Usage:")

    parser.add_argument('model', help='Enter "B": run as bash model, Enter "I" : run as interactive model')
    parser.add_argument('input', help='Path for your input files')

    args = parser.parse_args()

    if args.model == "B":
      print("run as bash model")
      Input = args.input
      BashMode(Input)


    if args.model == "I":
      print("run as interactive model")
      InteractiveModel()


main()
