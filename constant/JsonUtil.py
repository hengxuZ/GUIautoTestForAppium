import json

class JsonUtil:
    def __init__(self):
        pass

    @classmethod
    def read_json(self,path,key=None):
        json_tmp={}
        with open(path, 'r') as f:
            json_tmp = json.load(f)

        if key != None:
            return json_tmp[key]

        return json_tmp

    @classmethod
    def modify_json(self,path,data):
        '''拼接好的data,传入进行修改'''
        with open(path,'w') as f:
            f.write(json.dumps(data, indent=4))
            f.close()

if __name__ == "__main__":
    pass
