from appGui.common.LocateUtil import LocateUtil
from appGui.config.EnvSwitch import EnvSwitch
class KingKongDistrict:
    def __init__(self):
        self.staking = 'Staking' if EnvSwitch().is_online_env() else "Staking挖矿"
        self.recharge = "充提币" if EnvSwitch().is_online_env() else "充币/提币"

if __name__ == "__main__":
    ins = KingKongDistrict()
    print(ins.recharge)

