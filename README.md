# dendropy

[DendroPy](http://dendropy.org/) is a Python library for phylogenetic computing.
It provides classes and functions for the simulation, processing, and manipulation of phylogenetic trees and character matrices, and supports the reading and writing of phylogenetic data in a range of formats, such as NEXUS, NEWICK, NeXML, Phylip, FASTA, etc.
More advanced functionality allows you to manipulate (reroot, rotate, restructure, prune, graft, etc.) trees, calculate range of metrics and statistics on splits/bipartitions, trees, collections of trees, or character data.
DendroPy takes care of all of the complex, tedious, yet necessary heavy-lifting of phylogenetic data reading, writing, manipulation, and management, leaving you free to focus YOUR development efforts on actually solving the problem at hand.
Its rich data model provides convenient logical building blocks with which you can develop your own programs, allowing you to think about your data in terms of, e.g., "trees", "taxa", and "DNA alignments" instead of dictionaries, strings, or lists.
DendroPy can thus function as a stand-alone library for phylogenetics, a component of more complex multi-library phyloinformatic pipelines, scripting "glue" that assembles and drives such pipelines, or the core supporting infrastructure for full-scale enterprise-level applications.

With this workshop you will learn to use DendroPy to power your bio/phylo/evo-informatics adventures!
We will begin with a conceptual overview of DendroPy's phylogenetic data model and its usage.
This will be followed by a series of practicals that will provide all you need to get started working with phylogenetic data: reading/writing data in various formats, merging and splitting data from multiple sources, basic tree and tree collection iteration, calculations of tree and character-data statistics and metrics, etc.
We will then visit some of the more advanced wings of this sprawling library, with practical examples motivated by real-world problems.

Some basic [shell](https://github.com/jeetsukumaran/Phylogenetic_Computing_with_DendroPy/blob/master/source/preliminaries.rst) and [Python skills](https://github.com/jeetsukumaran/Phylogenetic_Computing_with_DendroPy/blob/master/source/python-lang.rst) are required to get the most from this workshop.
If you are not comfortable with either, please refer to the these documents to get started: [preliminaries](https://github.com/jeetsukumaran/Phylogenetic_Computing_with_DendroPy/blob/master/source/preliminaries.rst) and [Python fundamentals](https://github.com/jeetsukumaran/Phylogenetic_Computing_with_DendroPy/blob/master/source/python-lang.rst).
Even if you have no background at all, the above two documents should be able to guide you to sufficient fluency very quickly.
