from win32api import GetSystemMetrics


def printresolution():
    width = GetSystemMetrics (0)
    height = GetSystemMetrics (1)
    print ('Screen resolution = %dx%d' % (width, height))