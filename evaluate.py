import argparse
import json

if __name__ == "__main__":
    # read arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", type=str, help="Dataset name")
    parser.add_argument("--output", type=str, help="Output path")
    parser.add_argument("--threshold", type=float, help="consistency threshold")

    args = parser.parse_args()
    
    # TODO: add other datasets, as well as a parser for each dataset
    if args.dataset == "hotpotqa":
        from utils.hotpotqa_parser import hotpotqa
        dataset = hotpotqa()
    elif args.dataset == "medmcqa":
        # noinspection PyUnresolvedReferences
        from utils.medmcqa_parser import medmcqa
        dataset = medmcqa()
    elif args.dataset == "fever":
        from utils.fever_parser import fever
        dataset = fever()
    elif args.dataset == "fetaqa":
        from utils.fetaqa_parser import FetaQADataset
        dataset = FetaQADataset()
    else:
        raise Exception("Invalid dataset name")
    
    data = json.load(open(args.output, "r"))
    print('Found {} existing outputs'.format(len(data)))
    
    count = 0
    domains = {}
    acc_records = {'plain': 0, 'cot': 0, 'cot_sc': 0, 'ka': 0}
    sc_records = []
    not_did_count = 0
    edited_out_false_ones = []
    for idx, ex in enumerate(data):
        if "cot_answer" in ex:
            
            gt = ex["label"]
            # use get_ans_text to normalize all answers: lower case, etc
            answer = dataset.get_ans_text(ex['answer'])
            cot_answer = dataset.get_ans_text(ex['cot_answer'])
            cot_sc_answer = dataset.get_ans_text(ex['cot_sc_answer'])
            sc_records.append(ex['cot_sc_score'])
            
            if ex['cot_sc_score'] < args.threshold:
                if 'final_answer' in ex:
                    ka_answer = ex['final_answer']
                    count += 1
                    for domain in ex['s1_domains']:
                        if domain not in domains:
                            domains[domain] = 0
                        domains[domain] += 1
                else:
                    print('instance id: ', ex['id'])
                    print('cot_sc_score: ', ex['cot_sc_score'])
                    raise Exception('Cannot find edited final answer for the above instance.')
            else:
                ka_answer = cot_sc_answer
            
            acc_records['plain'] += (answer == gt)
            acc_records['cot'] += (cot_answer == gt)
            acc_records['cot_sc'] += (cot_sc_answer == gt)
            acc_records['ka'] += (ka_answer == gt)
            if ex['cot_sc_score'] < args.threshold:
                if ka_answer == gt: #true
                    edited_out_false_ones.append(ex)
                print("--------------id: {}; {}--------------".format(ex['id'], (ka_answer == gt)))
                print('question: ', ex['question'])
                
                print('cot_rationale 1: ', ex['cot_sc_rationales'][0])
                print('retrieve_know 1: ', ex['rationale_1_knowl'])
                print('edited_ration 1: ', ex['edited_rationale_1'])
                print('cot_rationale 2: ', ex['cot_sc_rationales'][1])
                print('retrieve_know 2: ', ex['rationale_2_knowl'])
                print('edited_ration 2: ', ex['edited_rationale_2'])
                
                print('answer: ', answer)
                print('cot_answer: ', cot_answer)
                print('cot_sc_answer: ', cot_sc_answer)
                print('ka_final_answer: ', ka_answer)
                print('ground_truth: ', gt)
            else: #no change
                edited_out_false_ones.append(ex)
        else:
            not_did_count += 1
    print('not_did_count: ', not_did_count)
    print('##############################################')
    print('plain acc: ', acc_records['plain'] / len(data))
    print('cot acc: ', acc_records['cot'] / len(data))
    print('cot_sc acc: ', acc_records['cot_sc'] / len(data))
    print('ka acc: ', acc_records['ka'] / len(data))
    print('##############################################')
    print('Edited {} out of {} instances'.format(count, len(data)))
    print('domains used: ', domains)
    print('##############################################')
    print('sc score between 0 to 0.1: ', len([x for x in sc_records if x < 0.1]))
    print('sc score between 0.1 to 0.2: ', len([x for x in sc_records if 0.1 <= x < 0.2]))
    print('sc score between 0.2 to 0.3: ', len([x for x in sc_records if 0.2 <= x < 0.3]))
    print('sc score between 0.3 to 0.4: ', len([x for x in sc_records if 0.3 <= x < 0.4]))
    print('sc score between 0.4 to 0.5: ', len([x for x in sc_records if 0.4 <= x < 0.5]))
    print('sc score between 0.5 to 0.6: ', len([x for x in sc_records if 0.5 <= x < 0.6]))
    print('sc score between 0.6 to 0.7: ', len([x for x in sc_records if 0.6 <= x < 0.7]))
    print('sc score between 0.7 to 0.8: ', len([x for x in sc_records if 0.7 <= x < 0.8]))
    print('sc score between 0.8 to 0.9: ', len([x for x in sc_records if 0.8 <= x < 0.9]))
    print('sc score between 0.9 to 1.0: ', len([x for x in sc_records if 0.9 <= x < 1.0]))
    print('sc score 1.0: ', len([x for x in sc_records if x == 1.0]))
    # json.dump(edited_out_false_ones, open('outputs/fever/edited_out_false_ones.json', 'w'))
    # print('len(edited_out_false_ones): ', len(edited_out_false_ones))