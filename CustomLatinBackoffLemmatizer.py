# Clément Besnier's custom class for LatinBackoffLemmatizer() that returns an empty list if no match is found, Clément Besnier, 20 Dec 2022

from cltk.lemmatize.backoff import (
    DefaultLemmatizer,
    DictLemmatizer,
    IdentityLemmatizer,
    RegexpLemmatizer,
    UnigramLemmatizer,
)

from cltk.lemmatize.lat import LatinBackoffLemmatizer


class CustomLatinBackoffLemmatizer(LatinBackoffLemmatizer):
    
    def _define_lemmatizer(self: object):
        # Suggested backoff chain--should be tested for optimal order
        self.backoff1 = DefaultLemmatizer(verbose=self.VERBOSE)
        self.backoff2 = DictLemmatizer(
            lemmas=self.LATIN_OLD_MODEL,
            source="Morpheus Lemmas",
            backoff=self.backoff1,
            verbose=self.VERBOSE,
        )
        self.backoff3 = RegexpLemmatizer(
            self.latin_sub_patterns,
            source="CLTK Latin Regex Patterns",
            backoff=self.backoff2,
            verbose=self.VERBOSE,
        )
        self.backoff4 = UnigramLemmatizer(
            self.train_sents,
            source="CLTK Sentence Training Data",
            backoff=self.backoff3,
            verbose=self.VERBOSE,
        )
        self.backoff5 = DictLemmatizer(
            lemmas=self.LATIN_MODEL,
            source="Latin Model",
            backoff=self.backoff4,
            verbose=self.VERBOSE,
        )
        self.lemmatizer = self.backoff5

    def __repr__(self: object):
        return f"<CustomLatinBackoffLemmatizer>"

lemmatizer = CustomLatinBackoffLemmatizer()
