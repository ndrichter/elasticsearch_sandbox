# tutorial made from
# https://medium.com/naukri-engineering/elasticsearch-tutorial-for-beginners-using-python-b9cb48edcedc

from elasticsearch import Elasticsearch

# setting up elastic cluster
es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])

print(es)

e1 = {
    "first_name": "nitin",
    "last_name": "panwar",
    "age": 27,
    "about": "Love to play cricket",
    "interests": ['sports', 'music']
}
e2 = {
    "first_name": "Jane",
    "last_name": "Smith",
    "age": 32,
    "about": "I like to collect rock albums",
    "interests": ["music"]
}
e3 = {
    "first_name": "Douglas",
    "last_name": "Fir",
    "age": 35,
    "about": "I like to build cabinets",
    "interests": ["forestry"]
}

employeeList = [e1, e2, e3]
counter = 1
# inserting document into elasticsearch
# for employee in employeeList:
#     res = es.index(index='megacorp',
#                    doc_type='employee',
#                    id=counter,
#                    body=employee)
#     counter += 1
#    print("Employee number {} inserted".format(counter))

# retrieve document
res = es.get(index='megacorp',
             doc_type='employee',
             id=1)
# print(res['_source'])

# delete document
# res = es.delete(index='megacorp', doc_type='employee', id=3)
# print(res['result'])

# return all results
res = es.search(index='megacorp',
                body={'query': {'match_all': {}}})
# print(res['hits'])
print('Got {} hits'.format(res['hits']['total']['value']))

# search by first name
res = es.search(index='megacorp',
                body={'query':{
                    'match':{
                        'first_name': 'nitin'
                    }
                           }
                      }
                )
print("Match: {}".format(res['hits']['hits']))

# next up try bool operator
res = es.search(index='megacorp',
               body={'query':{
                   'bool':{
                       'must':[{
                           'match':{
                               'first_name':'nitin'
                        }
                    }]
            }
        }
    })

print("Bool match: {}".format(res['hits']['hits']))

# try the filter operator