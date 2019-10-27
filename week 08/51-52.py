# Day 51


>>> import platform
>>> a = platform.system()
>>> print(a)
Darwin
>>> print(platform.python_version())
3.7.4
>>> x = dir(platform)
>>> print(x)
['DEV_NULL', '_UNIXCONFDIR', '_WIN32_CLIENT_RELEASES', '_WIN32_SERVER_RELEASES', '__builtins__', '__cached__', '__copyright__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_comparable_version', '_component_re', '_default_architecture', '_dist_try_harder', '_follow_symlinks', '_ironpython26_sys_version_parser', '_ironpython_sys_version_parser', '_java_getprop', '_libc_search', '_linux_distribution', '_lsb_release_version', '_mac_ver_xml', '_node', '_norm_version', '_parse_release_file', '_platform', '_platform_cache', '_pypy_sys_version_parser', '_release_filename', '_release_version', '_supported_dists', '_sys_version', '_sys_version_cache', '_sys_version_parser', '_syscmd_file', '_syscmd_uname', '_syscmd_ver', '_uname_cache', '_ver_output', '_ver_stages', 'architecture', 'collections', 'dist', 'java_ver', 'libc_ver', 'linux_distribution', 'mac_ver', 'machine', 'node', 'os', 'platform', 'popen', 'processor', 'python_branch', 'python_build', 'python_compiler', 'python_implementation', 'python_revision', 'python_version', 'python_version_tuple', 're', 'release', 'subprocess', 'sys', 'system', 'system_alias', 'uname', 'uname_result', 'version', 'warnings', 'win32_ver']


# Day 52


>>> import datetime
>>> X = datetime.datetime.now()
>>> print(X)
2019-10-27 04:16:19.828306
>>> print(X.year)
2019
>>> print(X.strftime("%A"))
Sunday
>>> y = datetime.datetime(2020, 5, 17)
>>> print(y)
2020-05-17 00:00:00
>>> Y = datetime.datetime(2018, 6, 4)
>>> print(Y.strftime("%B"))
June
>>> 
