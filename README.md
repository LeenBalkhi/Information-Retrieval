# Information Retrieval System

A Python-based Information Retrieval (IR) system that processes a corpus of documents to enable efficient search and retrieval using TF-IDF vectorization.

## Overview

This project implements an Information Retrieval system that indexes a collection of documents and allows users to perform search queries. It utilizes Term Frequency-Inverse Document Frequency (TF-IDF) to represent documents and queries as vectors, facilitating the computation of similarity scores between them.

## Features

* Processes a corpus of text documents for indexing
* Implements TF-IDF vectorization for document representation
* Supports search queries to retrieve relevant documents based on cosine similarity
* Handles stop words removal to improve search accuracy

## Getting Started

### Prerequisites

* Python 3.x installed on your system

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/LeenBalkhi/Information-Retrieval.git
   cd Information-Retrieval
   ```


### Usage

1. Prepare your corpus by placing text documents in the `corpus/` directory.

2. Run the indexing script to process the corpus:

   ```bash
   python index.py
   ```

3. After indexing, you can perform search queries by running the search functionality provided in the script.

   *Note: Modify `index.py` as needed to input your search queries and display results.*

## Project Structure

* `corpus/` - Directory containing the text documents to be indexed
* `index.py` - Main script for indexing documents and handling search queries
* `stop words.txt` - File containing a list of stop words to be excluded during processing
* `idf_fileVector.txt` - Output file storing the TF-IDF vectors for documents
* `idf_term.txt` - Output file storing the IDF values for terms
* `term.txt` - Output file listing all terms processed

