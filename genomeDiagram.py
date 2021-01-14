from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.Graphics import GenomeDiagram
from Bio import SeqIO

file = SeqIO.read("Genome.gb", "genbank")
diagram = GenomeDiagram.Diagram("Tomato Curly Stunt Virus")
featureTrack1 = diagram.new_track(1, name="Annotated Features 1")
featureTrack2 = diagram.new_track(2, name="Annotated Features 2")
featureSet1 = featureTrack1.new_set()
featureSet2 = featureTrack2.new_set()

colorList = ["blue", "red", "green", "yellow", "pink"]
colorNum = 0;

for feature in file.features:
    if feature.type == "gene":
        color = colorList[colorNum]
        if colorNum % 2 == 0:
            featureSet1.add_feature(feature, color=color, label=True, label_size=15, label_position="middle")
        else:
            featureSet2.add_feature(feature, color=color, label=True, label_size=15, label_position="middle")
        if colorNum == 4:
            colorNum = 0
        else:
            colorNum += 1
    else:
        continue

diagram.draw(format="circular", circular=True, pagesize=(25*cm,25*cm), start=0, end=len(file), circle_core=0.7)
diagram.write("circularGenomeDiagram.png", "PNG")