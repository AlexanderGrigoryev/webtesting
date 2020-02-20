if __name__ == '__main__':
    import os

    root = os.getcwd()
    generator = os.path.join(root, 'generator', 'bin', 'allure')
    buffer = os.path.join(root, 'buffer')
    report = os.path.join(root, 'report')
    gen = '"%s" generate "%s" -c -o "%s"' % (generator, buffer, report)
    os.system(gen)
