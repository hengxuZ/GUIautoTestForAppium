
class FloatUtil:
    def compare_float(self,f1,f2,difference):
        return abs(f1 - f2) <= difference


if __name__ == "__main__":
    instance = FloatUtil()
    print(instance.compare_float(1.11,1.2,0.01))
