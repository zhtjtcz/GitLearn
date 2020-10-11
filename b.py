import yaml

if __name__ == '__main__':
    f = open('a.yaml')
    info = yaml.load(f, Loader=yaml.FullLoader)
    print(info)
