import json

input_path = 'neural_search/MultiSpanQA.json'
doc_output_path = 'neural_search/MultiSpanQA_converted.jsonl'
query_output_path = 'neural_search/MultiSpanQA_queries.json'

def main():
    with open(input_path, 'r') as f:
        data = json.load(f)
    docs = data['data']
    
    queries = []
    with open(doc_output_path, 'w') as doc_out:
        for idx, entry in enumerate(docs, 1):
            doc = {
                '_id': str(idx),
                'title': '',
                'text': ' '.join(entry['context'])
            }
            doc_out.write(json.dumps(doc) + '\n')
            queries.append(' '.join(entry['question']))
    
    with open(query_output_path, 'w') as query_out:
        json.dump(queries, query_out, indent=2)

if __name__ == '__main__':
    main() 