from LSMART import *

def test1():
    console().printvl('performing tests.....') 

    console().printvl('')
    
    if console().printvl('  1. performing test1...') == console().printvl('    checking results...'):
        print('test1 successfull and returned an exit code of 1') 
        return True 

    else:
        print('test1 terminated with exit code 0')
        return False

def test2():

    console().printvl('') 
    console().printvl(' 2. performing test2...') 

    if console().printvl(f' {1 + 1}') == console().printvl('    checking results...'):
        print('test2 successfull and returned an exit code of 1')
        return True 

    else:
        print('test2 terminated with exit code 0')
        return False

def test3():
    console().printvl('')
    console().printvl(' 3. performing test3...')

    if console().printvl(f'   {1 - 1}') == console().printvl('  checking results...'):
        print('test3 successfull and returned an exit code of 1')
        return True 

    else:
        print('test3 terminated with exit code 0')
        return False 

def test4():
    console().printvl('')
    console().printvl(' 4. performing test4...')

    if console().printvl(f'   {1 * 1}') == console().printvl('  checking results...'):
        print('test4 successfull and returned an exit code of 1')
        return True 

    else:
        print('test4 terminated with exit code 0')
        return False 

def test5():
    console().printvl('')
    console().printvl(' 5. performing test5...')

    if console().printvl(f'   {1 / 1}') == console().printvl('  checking results...'):
        print('test5 successfull and returned an exit code of 1')
        return True 

    else:
        print('test5 terminated with exit code 0')
        return False 

def test6():
    console().printvl('')
    console().printvl(' 6. performing test6...')

    if console().printvl(f'   {1 % 1}') == console().printvl('  checking results...'):
        print('test6 successfull and returned an exit code of 1')
        return True 

    else:
        print('test6 terminated with exit code 0')
        return False

def test7():
    console().printvl('')
    console().printvl(' 7. performing test7...')

    if console().debug().d(tag='test7', message='debug info') == print('checking results...'):
        print('test7 successfull and returned an exit code of 1')
        return True

    else:
        print('test7 terminated with exit code 0')
        return False

def test8():
    console().printvl('')
    console().printvl(' 8. performing test8...')

    if console().warn().w(tag='test8', message='warning message') == print('checking results...'):
        print('test7 successfull and returned an exit code of 1')
        return True

    else:
        print('test7 terminated with exit code 0')
        return False 

def test9():
    console().printvl('')
    console().printvl(' 9. performing test9...')

    if console().printcvl(' hello world!', 'magenta') == print('checking results...'):
        print('test7 successfull and returned an exit code of 1')
        return True

    else:
        print('test7 terminated with exit code 0')
        return False 

# so far so good!!

if __name__ == '__main__':
    test1() 
    test2()
    test3() 
    test4() 
    test5()
    test6() 
    test7()
    test8()
    test9()