import json
from typing import List

from fire import Fire
from pydantic import BaseModel
from sacrebleu import BLEU


class Scorer(BaseModel):
    def update(self, pred: str, gold: str):
        raise NotImplementedError

    def get_score(self) -> dict:
        raise NotImplementedError


class ExactScorer(Scorer):
    records: List[bool] = []

    def update(self, pred: str, gold: str):
        self.records.append(pred.lower().startswith(gold.lower()))

    def get_score(self) -> float:
        return sum(self.records) / len(self.records)


class BleuScorer(Scorer):
    records: List[float] = []

    def update(self, pred: str, gold: str):
        scorer = BLEU(effective_order=True)
        result = scorer.sentence_score(pred.lower(), [gold.lower()])
        self.records.append(result.score)

    def get_score(self) -> float:
        return sum(self.records) / len(self.records)


def select_scorer(name: str):
    if name == "exact":
        return ExactScorer()
    elif name == "bleu":
        return BleuScorer()
    raise KeyError(name)


def main(path: str, scorer_name: str = "bleu"):
    with open(path) as f:
        data = json.load(f)

    info = dict()
    for key in ["cot_answer", "cot_sc_answer", "final_answer"]:
        scorer = select_scorer(scorer_name)
        for sample in data:
            if key in sample:
                scorer.update(sample[key], gold=sample["answer"])

        if scorer.records:
            info[f"num_{key}"] = len(scorer.records)
            info[f"score_{key}"] = scorer.get_score()

    print(json.dumps(info, indent=2))


"""
python run.py --dataset fetaqa --output outputs/fetaqa.json --num_test 100
{
  "num_cot_answer": 100,
  "score_cot_answer": 16.89817538133122,
  "num_cot_sc_answer": 100,
  "score_cot_sc_answer": 18.01273954751043
}

{
  "num_cot_answer": 500,
  "score_cot_answer": 17.24905600268704,
  "num_cot_sc_answer": 500,
  "score_cot_sc_answer": 17.89665614095217
}

{
  "num_cot_answer": 100,
  "score_cot_answer": 18.221874693418314,
  "num_cot_sc_answer": 100,
  "score_cot_sc_answer": 18.262021294031346,
  "num_final_answer": 54,
  "score_final_answer": 16.978702426670825
}

p run.py --dataset fetaqa_query --output outputs/fetaqa_query.json --num_test 100
{
  "num_cot_answer": 100,
  "score_cot_answer": 19.23742678438269,
  "num_cot_sc_answer": 100,
  "score_cot_sc_answer": 19.651697660478728
}

p run.py --dataset fetaqa_standard --output outputs/fetaqa_standard.json --num_test 100
{
  "num_cot_answer": 100,
  "score_cot_answer": 20.733321679243776
}

p run.py --dataset fetaqa_standard --output outputs/fetaqa_standard_6.json --num_test 100 --num_train 6
{
  "num_cot_answer": 100,
  "score_cot_answer": 23.052812827151175
}

p run.py --dataset fetaqa_query_standard --output outputs/fetaqa_query_standard.json --num_test 100
{
  "num_cot_answer": 100,
  "score_cot_answer": 21.828911109975916
}

p run.py --dataset fetaqa_no_table --output outputs/fetaqa_no_table.json --num_test 100
{
  "num_cot_answer": 100,
  "score_cot_answer": 16.0837166461521
}

p run.py --dataset fetaqa_no_table --output outputs/fetaqa_no_table_6.json --num_test 100 --num_train 6
{
  "num_cot_answer": 100,
  "score_cot_answer": 15.944002468189824
}

p run.py --dataset fetaqa_query_standard --output outputs/fetaqa_query_standard_6.json --num_test 100 --num_train 6
{
  "num_cot_answer": 100,
  "score_cot_answer": 23.14010063187766
}

p run.py --dataset fetaqa_sql_wiki --output outputs/fetaqa_sql_wiki.json --num_test 100
{
  "num_cot_answer": 100,
  "score_cot_answer": 24.963868147204522
}

p run.py --dataset fetaqa_sql_wiki --output outputs/fetaqa_sql_wiki_6.json --num_test 100 --num_train 6
{
  "num_cot_answer": 100,
  "score_cot_answer": 25.96826303303141
}

p run.py --dataset fetaqa_cot --output outputs/fetaqa_cot.json --num_test 100
{
  "num_cot_answer": 100,
  "score_cot_answer": 17.306547576852566
}

p run.py --dataset fetaqa_cot --output outputs/fetaqa_cot_6.json --num_test 100 --num_train 6
{
  "num_cot_answer": 100,
  "score_cot_answer": 19.447511706448008
}

"""


if __name__ == "__main__":
    Fire()
