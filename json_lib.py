'''
This module is used to perform JSON operation
    author: Rahul Shah
    email: rahul.shah.9191@gmail.com
    version : 1.0
'''
import json

class JSON:

    @staticmethod
    def get_key(self, json_data, value, stack=[], path=[]):
        '''
        from given JSON in dictionary formate and value, return all path having this valueh
        :param json_data: input json data
        :param value: value
        :param stack: stack to use JSON path
        :param path: JSON path having value matched
        :return: return list of path having value match
        '''
        for k,v in json_data.items():
            if type(v)  == dict:
                stack.append(k)
                get_key(v, value, stack)
            elif type(v) == list:
                stack.append(k)
                for i in range(0, len(v)):
                    stack.append(str(i))
                    get_key(v[i], value, stack, path)
                    #stack.pop()
            else:
                if str(v).lower() == str(value).lower():
                    stack.append(k)
                    #print("-".join(stack))
                    path.append("-".join(stack))
        if len(stack) > 0:
            stack.pop()
        return path

    @staticmethod
    def get_value(json_data, key, stack=[], path={}):
        '''
        from given JSON in dictionary formate and key, return all possible values from json with path
        :param json_data: input json data
        :param key: json leaf node key
        :param stack: stack to store path
        :param path: path values
        :return: return dictionary of key as path and value as json value
        '''
        for k,v in json_data.items():
            if type(v)  == dict:
                if str(k).lower() == str(key).lower():
                    path["-".join(stack)] = v
                stack.append(k)
                get_value(v, key, stack)
            elif type(v) == list:
                stack.append(k)
                if str(k).lower() == str(key).lower():
                    path["-".join(stack)] = v
                for i in range(0, len(v)):
                    stack.append(str(i))
                    get_value(v[i], key, stack, path)
                    #stack.pop()
            else:
                if str(k).lower() == str(key).lower():
                    stack.append(k)
                    #print(f"-".join(stack), end=' :: ')
                    #print(v)
                    path["-".join(stack)] = v
        if len(stack) > 0:
            stack.pop()
        return path

    @staticmethod
    def is_valid_json(json_data):
        '''
        Given string input, check if it is value JSON
        :param json_data: input json data in string format
        :return: return True if input string is valid JSON else return False
        '''
        try:
            json.loads(json_data)
            return True
        except:
            return False

    @staticmethod
    def key_count(json_data, key, stack=[], count=0):
        '''
        Given input JSON in dict formate, return number of keys present in JSON
        :param json_data: input JSON
        :param key: key string
        :param stack: inuput stack used for store path
        :param count: key's count
        :return: key count from input JSON
        '''
        return len(get_value(json_data,key).keys())
