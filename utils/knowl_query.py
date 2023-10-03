from utils.retrieval.wikidata import retrieve_wikidata_knowledge
from utils.retrieval.wikitable import retrieve_wikitable_knowledge
from utils.retrieval.dpr import retrieve_dpr_knowledge
from utils.retrieval.wikipedia import retrieve_wikipedia_knowledge

from utils.retrieval.flashcard import retrieve_flashcard_knowledge
from utils.retrieval.uptodate import retrieve_uptodate_knowledge

from utils.retrieval.scienceqa_bio import retrieve_scienceqa_bio_knowledge
from utils.retrieval.ck12 import retrieve_ck12_knowledge

from utils.retrieval.scienceqa_phy import retrieve_scienceqa_phy_knowledge
from utils.retrieval.physicsclassroom import retrieve_physicsclassroom_knowledge

# domain and knowledge sources mapping
domain_mapping = {
    "factual": {
        "wikidata": retrieve_wikidata_knowledge,
        # "wikitable": retrieve_wikitable_knowledge,
        # "dpr": retrieve_dpr_knowledge,
        "wikipedia": retrieve_wikipedia_knowledge,
    },
    "medical": {
        # "flashcard": retrieve_flashcard_knowledge,
        "uptodate": retrieve_uptodate_knowledge,
    },
    "biology": {
        "scienceqa_bio": retrieve_scienceqa_bio_knowledge,
        "ck12": retrieve_ck12_knowledge,
    },
    "physical": {
        "scienceqa_phy": retrieve_scienceqa_phy_knowledge,
        "physicsclassroom": retrieve_physicsclassroom_knowledge,
    },
}


def retrieve_knowledge(domain, input, data_point):
    # input is a string
    knowl = {}
    # If not in mapping, automatically use "factual"
    domain = [x if x in domain_mapping else "factual" for x in domain]
    # Remove duplicates
    domain = list(dict.fromkeys(domain))
    for x in domain:
        knowl[x] = {}
        domain_sources = domain_mapping[x]
        for y in domain_sources:
            print("--- Retrieving knowledge from", x, y)
            tmp_knowl = domain_sources[y](input, data_point)
            # print(tmp_knowl)
            knowl[x][y] = tmp_knowl

    return knowl

def knowl_is_empty(knowl):
    for x in knowl:
        for y in knowl[x]:
            if knowl[x][y] != '':
                return False
    return True