#Find the path exists in the given the dictionary.


def find_item(dictionary, path):
    path_split = path.split('.')
    final_item = dictionary
    for item in path_split:
        if item in final_item.keys():
                final_item = final_item[item]                    
        else:
            return None
    return final_item 

print(find_item({'fruit': {'seed': 'Yes'}}, 'fruit.seed'))
