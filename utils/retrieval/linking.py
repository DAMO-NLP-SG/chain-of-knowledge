import pickle
from typing import Dict, List, Optional, Tuple, Set

import marisa_trie
import spacy
from fire import Fire
from pydantic import BaseModel
from spacy import Language
from tqdm import tqdm
from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
    PreTrainedModel,
    PreTrainedTokenizer,
)


Span = Tuple[int, int]


class Trie(object):
    # Copyright (c) Facebook, Inc. and its affiliates.
    # All rights reserved.
    #
    # This source code is licensed under the license found in the
    # LICENSE file in the root directory of this source tree.
    def __init__(self, sequences: List[List[int]] = ()):
        self.trie_dict = {}
        self.len = 0
        if sequences:
            for sequence in sequences:
                Trie._add_to_trie(sequence, self.trie_dict)
                self.len += 1

        self.append_trie = None
        self.bos_token_id = None

    def append(self, trie, bos_token_id):
        self.append_trie = trie
        self.bos_token_id = bos_token_id

    def add(self, sequence: List[int]):
        Trie._add_to_trie(sequence, self.trie_dict)
        self.len += 1

    def get(self, prefix_sequence: List[int]):
        return Trie._get_from_trie(
            prefix_sequence, self.trie_dict, self.append_trie, self.bos_token_id
        )

    @staticmethod
    def load_from_dict(trie_dict):
        trie = Trie()
        trie.trie_dict = trie_dict
        trie.len = sum(1 for _ in trie)
        return trie

    @staticmethod
    def _add_to_trie(sequence: List[int], trie_dict: Dict):
        if sequence:
            if sequence[0] not in trie_dict:
                trie_dict[sequence[0]] = {}
            Trie._add_to_trie(sequence[1:], trie_dict[sequence[0]])

    @staticmethod
    def _get_from_trie(
        prefix_sequence: List[int],
        trie_dict: Dict,
        append_trie=None,
        bos_token_id: int = None,
    ):
        if len(prefix_sequence) == 0:
            output = list(trie_dict.keys())
            if append_trie and bos_token_id in output:
                output.remove(bos_token_id)
                output += list(append_trie.trie_dict.keys())
            return output
        elif prefix_sequence[0] in trie_dict:
            return Trie._get_from_trie(
                prefix_sequence[1:],
                trie_dict[prefix_sequence[0]],
                append_trie,
                bos_token_id,
            )
        else:
            if append_trie:
                return append_trie.get(prefix_sequence)
            else:
                return []

    def __iter__(self):
        def _traverse(prefix_sequence, trie_dict):
            if trie_dict:
                for next_token in trie_dict:
                    yield from _traverse(
                        prefix_sequence + [next_token], trie_dict[next_token]
                    )
            else:
                yield prefix_sequence

        return _traverse([], self.trie_dict)

    def __len__(self):
        return self.len

    def __getitem__(self, value):
        return self.get(value)


class MarisaTrie(object):
    # Copyright (c) Facebook, Inc. and its affiliates.
    # All rights reserved.
    #
    # This source code is licensed under the license found in the
    # LICENSE file in the root directory of this source tree.
    def __init__(
        self,
        sequences: List[List[int]] = (),
        cache_fist_branch=True,
        max_token_id=256001,
    ):

        self.int2char = [chr(i) for i in range(min(max_token_id, 55000))] + (
            [chr(i) for i in range(65000, max_token_id + 10000)]
            if max_token_id >= 55000
            else []
        )
        self.char2int = {self.int2char[i]: i for i in range(max_token_id)}

        self.cache_fist_branch = cache_fist_branch
        if self.cache_fist_branch:
            self.zero_iter = list({sequence[0] for sequence in sequences})
            assert len(self.zero_iter) == 1
            self.first_iter = list({sequence[1] for sequence in sequences})

        self.trie = marisa_trie.Trie(
            "".join([self.int2char[i] for i in sequence]) for sequence in sequences
        )

    def get(self, prefix_sequence: List[int]):
        if self.cache_fist_branch and len(prefix_sequence) == 0:
            return self.zero_iter
        elif (
            self.cache_fist_branch
            and len(prefix_sequence) == 1
            and self.zero_iter == prefix_sequence
        ):
            return self.first_iter
        else:
            key = "".join([self.int2char[i] for i in prefix_sequence])
            return list(
                {
                    self.char2int[e[len(key)]]
                    for e in self.trie.keys(key)
                    if len(e) > len(key)
                }
            )

    def __iter__(self):
        for sequence in self.trie.iterkeys():
            yield [self.char2int[e] for e in sequence]

    def __len__(self):
        return len(self.trie)

    def __getitem__(self, value):
        return self.get(value)


class EntityDetector(BaseModel):
    def run(self, text: str) -> List[Span]:
        raise NotImplementedError


class SpacyEntityDetector(EntityDetector, arbitrary_types_allowed=True):
    model_name: str = "en_core_web_trf"
    model: Optional[Language] = None

    def load(self):
        if self.model is None:
            self.model = spacy.load(self.model_name)

    def run(self, text: str) -> List[Span]:
        self.load()
        doc = self.model(text)

        outputs = []
        for entity in doc.ents:
            outputs.append((entity.start_char, entity.end_char))
        return outputs


# class FlairEntityDetector(EntityDetector, arbitrary_types_allowed=True):
#     """https://huggingface.co/flair/ner-multi"""
#
#     model_name: str = "flair/ner-multi"
#     model: Optional[SequenceTagger]
#
#     def load(self):
#         if self.model is None:
#             self.model = SequenceTagger.load(self.model_name)
#
#     def run(self, text: str) -> List[str]:
#         self.load()
#         sentence = Sentence(text)
#         self.model.predict(sentence)
#
#         outputs = []
#         for entity in sentence.get_spans("ner"):
#             outputs.append(entity.text)
#         return outputs


def test_detector(
    text: str = "George Washington went to Washington in 1989 for ten days",
):
    model = SpacyEntityDetector()
    # print(model.run(text))


class EntityLinker(BaseModel):
    def run(self, text: str, span: Span) -> List[str]:
        raise NotImplementedError


class GenreEntityLinker(EntityLinker, arbitrary_types_allowed=True):
    """https://huggingface.co/facebook/mgenre-wiki"""

    model_name: str = "facebook/mgenre-wiki"  # Multilingual
    # model_name: str = "facebook/genre-linking-blink"  # English
    path_title_map: str = "utils/retrieval/linking_data/genre/title_to_id_en.pkl"
    title_id_map: Optional[Dict[str, str]] = None
    model: Optional[PreTrainedModel] = None
    tokenizer: Optional[PreTrainedTokenizer] = None

    def load_titles(self):
        if self.title_id_map is None:
            # for _ in tqdm(range(1), desc=self.path_title_map):
            #     with open(self.path_title_map, "rb") as f:
            #         self.title_id_map = pickle.load(f)
            for _ in range(1):
                with open(self.path_title_map, "rb") as f:
                    self.title_id_map = pickle.load(f)
        # print(dict(title_id_map=len(self.title_id_map)))

    def load_model(self):
        if self.model is None:
            self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name).eval()
        if self.tokenizer is None:
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)

    def load(self):
        self.load_titles()
        self.load_model()

    def run(self, text: str, span: Span) -> List[str]:
        self.load()
        mention = text[slice(*span)]
        parts = [text[: span[0]], "[START]", mention, "[END]"]
        x = " ".join(parts)

        # TODO: Add the prefix trie
        output_ids = self.model.generate(
            **self.tokenizer([x], return_tensors="pt"),
            num_beams=5,
            num_return_sequences=5,
            max_length=20,
            # OPTIONAL: use constrained beam search
            # prefix_allowed_tokens_fn=lambda batch_id, sent: trie.get(sent.tolist()),
        )

        preds = self.tokenizer.batch_decode(output_ids, skip_special_tokens=True)
        outputs = []
        for p in preds:
            if p in self.title_id_map:
                outputs.append(self.title_id_map[p])

        return outputs


def test_linking(
    text: str = "Einstein was a German-born theoretical physicist.",
    # text: str = "Einstein era un fisico tedesco.",
):
    detector = SpacyEntityDetector()
    linker = GenreEntityLinker()

    opt = []
    for span in detector.run(text):
        links = linker.run(text, span=span)
        # print(dict(char_span=span, mention=text[slice(*span)], links=links))
        opt.append(dict(char_span=span, mention=text[slice(*span)], links=links))

    return opt

    """
    {'char_span': (0, 8), 'mention': 'Einstein', 'links': ['Q937']}
    {'char_span': (15, 21), 'mention': 'German', 'links': ['Q42884', 'Q183', 'Q22633', 'Q43287', 'Q188']}
    """


def process_titles(
    path_in: str = "utils/retrieval/linking_data/genre/lang_title2wikidataID-normalized_with_redirect.pkl",
    path_out="utils/retrieval/linking_data/genre/title_to_id_en.pkl",
    languages: List[str] = ("en",),
):
    for _ in tqdm(range(1), desc=path_in):
        # ~5min to load once
        with open(path_in, "rb") as f:
            raw: Dict[Tuple[str, str], Set[str]] = pickle.load(f)

    mapping: Dict[str, List[str]] = {}
    for k, v in tqdm(raw.items()):
        if k[0] in languages:
            k_new = k[1] + " >> " + k[0]  # Match model output format
            v_new = sorted(v)[0]  # Str instead of list for speed
            mapping[k_new] = v_new  # TODO: Disambiguate the v

    for _ in tqdm(range(1), desc=path_out):
        with open(path_out, "wb") as f:
            pickle.dump(mapping, f)


if __name__ == "__main__":
    Fire()
