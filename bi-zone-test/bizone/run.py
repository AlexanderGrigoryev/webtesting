
if __name__ == '__main__':

    from os import system, path, mkdir, getcwd
    from shutil import rmtree
    from webium.wait import wait

    root = getcwd()
    buffer = path.join(root, 'allure-report', 'buffer')

    def clear_buffer():
        if path.exists(buffer):
            rmtree(buffer)
            wait(lambda: not path.exists(buffer))
        mkdir(buffer)

    def run(*modules):
        tests = ''
        for module in modules:
            tests += ' "%s"' % path.join(root, 'app_tests', module)
        run_tests = 'pytest -n 5 --alluredir="%s" %s' % (buffer, tests)
        system(run_tests)

    clear_buffer()

    run('test_smoke.py', 'test_pages.py')
