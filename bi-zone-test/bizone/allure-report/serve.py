if __name__ == '__main__':
    import os

    root = os.getcwd()
    srv = os.path.join(root, 'generator', 'bin', 'allure')
    source = os.path.join(root, 'buffer')
    os.system(srv + ' serve ' + source)
