'''
A SCons module to ease the creation of a SConstruct or SConscript file
to use with Google Test.
'''

import os

from SCons.Script import Platform, Environment, Copy

def getGtestDir():
    '''
    Determine the Google Test directory. Use the environment variable
    GTEST_DIR if found, or ~/projects/gtest if not.
    '''
    
    gtest_dir = os.environ.get('GTEST_DIR', 
        os.path.join(os.environ['HOME'], 'projects', 'gtest'))
    return gtest_dir

def gtestEnvironment(**kwargs):
    '''
    Create an environment to build a Google Test application. 
    Parameters are the same keyworded parameters passed into
    Environment()
    '''

    # Create the build environment
    gtest_dir = getGtestDir()
    env = Environment(**kwargs)

    # Copy the two files needed for Google Test over
    env.Command('gtest-all.cc', os.path.join(gtest_dir, 'src', 'gtest-all.cc'),
        Copy("$TARGET", "$SOURCE"))
    env.Command('gtest_main.cc', os.path.join(gtest_dir, 'src', 'gtest_main.cc'),
        Copy("$TARGET", "$SOURCE"))

    # Build the two Google Test libraries locally
    env.Library('gtest', 'gtest-all.cc')
    env.Library('gtest_main', 'gtest_main.cc')

    # Setup the build environment
    env.AppendUnique(CPPPATH=gtest_dir)
    env.AppendUnique(CPPPATH=os.path.join(gtest_dir, 'include'))
    env.AppendUnique(LIBPATH='.')
    env.AppendUnique(LIBS=['gtest', 'gtest_main'])

    platform = Platform()
    if platform.name in ['posix', 'darwin']:
        env.AppendUnique(LIBS=['pthread'])

    return env

def getCommonFlags():
    '''
    Return a set of common flags for each platform. For example, -ggdb 
    for posix and darwin, -Zi for win32.
    '''
    flags = {}
    platform = Platform()
    if platform.name in ['posix', 'darwin']:
        flags['CCFLAGS'] = ['-ggdb', '-Wall']
    elif platform.name in ['win32']:
        flags['CCFLAGS'] = ['-Zi', '-Wall']
    return flags

