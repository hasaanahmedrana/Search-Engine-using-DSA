## _***BASIC QUERY SEARCH ENGINE USING DATA STRUCTURES***_

_This project implements a basic search engine that processes search queries and tracks their occurrences.
It utilizes a binary search tree (BST) to store and manage the top queries efficiently. A balances BST is implemenented instead of AVL_.


## _**KEY FEAUTURE:**_

- _**Reading and Segregating:**   Utilize a hash table and a default dictionary to separate the top 10,000 searches from the search history file based on their frequency_.
- _**Populating BST:**   Arranges history queries to form a well-balanced tree. The most frequent queries with their URLs are populated in the BST._
- _**Handling less frequent Queries:**   Less frequent queries are stored in files, with each file containing 10,000 queries. All files are stored in a 'less frequent' folder._
- _**Time Report:**   Implements a time report showing the average time to search frequent and less frequent queries using the 50 most frequent and 50 less frequent words.._

## _**Files:**_
Problem statement: https://docs.google.com/document/d/1JjWTLVmz0yZjB2A1SK27ooDlG-xsmv-g/edit
ZIP: https://drive.google.com/file/d/1Y-Cy79ZiX67gStPXbtaP35KtPydpRL_Z/view?usp=sharing
- ZIP contains search-history.txt and search-results.txt which are provided with the problem statement. Other Files are the part of solution.
