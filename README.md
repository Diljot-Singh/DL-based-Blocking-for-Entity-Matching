# DL based blocking for entity matching

Entity Matching (EM) is the process of finding instances of data records associated with the same real-world entity. Comparison across all the records pairs leads to a quadratic matching complexity hence blocking is essential to group most probable pairs. Once the blocked set is created it can then be passed for matching, however capturing all the promising sets is a major challenge faced by current methods.

This project aims to perform blocking for entity matching using deep learning. It includes functionalities for transforming tuples into embeddings customized for blocking. This is a self-supervised approach and does not require any labeled data. We provide provides multiple instantiations for tuple embedding  and vector pairing for performing blocking. 

# Original Code, Paper and Data

For details on the architecture of the models used, take a look at authors paper
[Deep Learning for Blocking in Entity Matching: A Design Space Exploration (VLDB '21)](http://vldb.org/pvldb/vol14/p2459-thirumuruganathan.pdf).

This work is an extension of the code available at:
https://github.com/saravanan-thirumuruganathan/DeepBlocker. We have added a new more techniques mentioned in the paper in this repository

All datasets used can be downloaded from the [datasets page](https://github.com/anhaidgroup/deepmatcher/blob/master/Datasets.md).


## Author
Diljot Singh, 
Pranav Gupta 

