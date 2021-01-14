# ACM Research Coding Challenge (Spring 2021)

# Background
This was the first time I worked with any kind of genbank or genome data. I did not know what genome circular diagrams were either so I first searched up examples. Google provided many complicated and intricate examples, but I also found a few simpler examples that highlighted the features and their labels efficiently. 

Then I researched more about how genome diagrams could be created using Python. I found a scholarly [article](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6728899/) (1) that outlines various software and libraries that are used to create genome diagrams. The article mentioned Python's GenomeDiagram (more specifically Bio.Graphics.GenomeDiagram) module from the Biopython library. With further research, I determined that I can use the GenomeDiagram module to complete the challenge.

# Process
I utilized both the GenomeDiagram [documentation](https://biopython.org/docs/1.75/api/Bio.Graphics.GenomeDiagram.html) (2) and a [tutorial](https://biopython-tutorial.readthedocs.io/en/latest/notebooks/17%20-%20Graphics%20including%20GenomeDiagram.html) on the module (3) when working to complete the challenge. The first time I created the diagram, the labels were too small and since I had only one track, several features seemed to have overlapped each other. I edited my solution to contain 2 tracks instead of 1 and implemented a color sequence that created a more appealing visualization. I also made the label size larger and positioned it to the middle. I found that there were a total of 5 gene features for the Tomato Curly Stunt Virus.

# Diagram
![alt text](https://github.com/SBodapati11/ACM-Research-Coding-Challenge-S21/blob/main/circularGenomeDiagram.png)

# Citations
1) Parveen, Alisha et al. “Overview of Genomic Tools for Circular Visualization in the Next-generation Genomic Sequencing Era.” Current genomics vol. 20,2 (2019): 90-99. doi:10.2174/1389202920666190314092044
2) “Bio.Graphics.GenomeDiagram Package.” Bio.Graphics.GenomeDiagram Package - Biopython 1.75 Documentation, biopython.org/docs/1.75/api/Bio.Graphics.GenomeDiagram.html. 
3) “Graphics Including GenomeDiagram.” Graphics Including GenomeDiagram - Test Test Documentation, biopython-tutorial.readthedocs.io/en/latest/notebooks/17%20-%20Graphics%20including%20GenomeDiagram.html. 
