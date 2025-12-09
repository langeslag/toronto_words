# Toronto Words

This repository hosts the text of historical [Toronto CMS](https://www.medieval.utoronto.ca/) Latin exams (predating the 2024 Level One format change) in a plaintext/minimal markdown format, alongside notebooks processing and evaluating their text content.

I use it mostly as a resource by which to demonstrate basic NLP routines in the classroom, but it may also serve language study.

## Requirements

`CustomLatinBackoffLemmatizer.py` represents a modification, kindly provided by Clément Besnier, of the backoff chain included in the Latin Backoff Lemmatizer for CLTK 1.x. The modification serves purely to return an empty string if no match is found, so that other lemmatization sources can be consulted if CLTK fails to retrieve a match. It is not compatible with CLTK 2.0.

## Document Formatting

In order to facilitate processing as plaintext, the only markdown convention here implemented that deviates from strict plaintext formatting is the double space at line-end to mark a hard return in exam headings and in verse passages.

I have corrected a range of typographical errors, and introduced consistency of tokenization in such sequences as _se ipsum_ and _nonnulla_. For the full list of changes, see [`changes.txt`](https://github.com/langeslag/toronto_words/blob/main/changes.txt).

A notable change from the exam's original character formatting is the restriction of capital initials in the exam passages proper to personal names and sentence-initial words; this change was implemented during OCR proofreading in order to facilitate named entity recognition. Place-names were lowercased on the understanding that the interpretation of place-names requires more translation than that of personal names, so that for the purpose of assessing exam difficulty only personal names should be discounted.

## Further Development

This project was held up in lemmatization optimization for a considerable time. I had/have plans to add a lexicon and a notebook on lexical analysis once I'm happy with the lemmata. However, illness and then the apparent demise of the Latin WordNet lemmatizer halted development for the time being. I have decided to include in this release the lemmata as I was able to obtain them before these complications arose; these have not been proofread and will contain errors. If more favourable conditions should arise in future, I may well continue development of the lemmatization routine and the lexical evaluation of these exams.

## Permissions

PDFs of the exams were [made public](https://www.medieval.utoronto.ca/graduate/curriculum-course-information/past-language-exams) without any kind of licence by the Centre for Medieval Studies. I provide plaintext conversions here on the understanding that their distribution is not restricted.

[CLTK](https://github.com/cltk) is (c) 2013 Classical Language Toolkit and distributed under an [MIT licence](https://github.com/cltk/cltk/blob/master/LICENSE).

Since for the time being I am including a snippet of modified CLTK code, I am bound by the MIT licence for that portion of the code (which was provided by Clément Besnier); but as far as the code in my own notebooks is concerned I do not expect to be acknowledged for reuse.
