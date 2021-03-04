# module for levels

_dt = 'dirt'
_gs = 'grass'
_rd = 'road'
_sd = 'sand'
_sl = 'soil'
_se = 'stone'
_wr = 'water'

level0 = [
    [_wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _gs, _gs, _gs, _gs, _gs, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr],
    [_wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr],
    [_wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _wr, _wr, _wr, _wr, _wr],
    [_wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _wr, _wr, _wr, _wr],
    [_wr, _wr, _wr, _wr, _wr, _wr, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _wr, _wr],
    [_wr, _wr, _wr, _wr, _wr, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_wr, _wr, _wr, _wr, _wr, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _wr, _wr, _wr, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs]
]

level1 = [
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs]
]

level2 = [
    [_sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _rd, _rd, _rd, _rd, _rd, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl],
    [_sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _rd, _rd, _rd, _rd, _rd, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl],
    [_sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _rd, _rd, _rd, _rd, _rd, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl],
    [_sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _rd, _rd, _rd, _rd, _rd, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sd],
    [_sd, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _rd, _rd, _rd, _rd, _rd, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sd, _sd],
    [_sd, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _rd, _rd, _rd, _rd, _rd, _sl, _sl, _sl, _sl, _sl, _sd, _sd, _sd, _sd],
    [_sd, _sd, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _rd, _rd, _rd, _rd, _rd, _sl, _sl, _sl, _sd, _sd, _sd, _sd, _sd, _sd, _sd],
    [_sd, _sd, _sd, _sd, _sd, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _rd, _rd, _rd, _rd, _rd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd],
    [_sd, _sd, _sd, _sd, _sd, _sd, _sd, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _sl, _rd, _rd, _rd, _rd, _rd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd],
    [_sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sl, _sl, _sl, _sl, _sl, _sl, _rd, _rd, _rd, _rd, _rd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd],
    [_sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sl, _sl, _sl, _sl, _rd, _rd, _rd, _rd, _rd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd],
    [_sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sl, _rd, _rd, _rd, _rd, _rd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd],
    [_sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _se, _se, _se, _rd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd],
    [_sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _se, _se, _se, _se, _se, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _wr, _wr, _wr, _wr],
    [_sd, _sd, _sd, _wr, _wr, _wr, _wr, _wr, _wr, _sd, _se, _se, _se, _se, _se, _se, _se, _wr, _wr, _wr, _sd, _sd, _sd, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr],
    [_sd, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _se, _se, _se, _se, _se, _se, _se, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _sd],
    [_wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _se, _se, _se, _se, _se, _se, _se, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _sd, _sd],
    [_wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _se, _se, _se, _se, _se, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _sd, _sd, _sd, _sd],
    [_wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _se, _se, _se, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _sd, _wr, _sd, _sd, _sd, _sd, _sd],
    [_wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _sd, _sd, _sd, _sd, _sd, _sd, _sd, _sd]
]

_levelList = [level0, level1, level2]


def getSize():
    return len(_levelList)


def getLevel(i):
    return _levelList[i]


if __name__ == "__main__":
    print('testing\n')
    print(_levelList)
