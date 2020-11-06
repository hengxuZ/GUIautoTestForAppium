class EnvSwitch(object):
    '''控制环境执行不同的代码'''
    # env = "online"
    env = "test"



    @classmethod
    def get_current_env(cls):
        return cls.env

    @classmethod
    def is_online_env(cls):
        return cls.env == "online"




if __name__ == "__main__":
    print(not EnvSwitch().is_online_env())
