# TODO handle module stuff

_dt = 'dirt'
_gs = 'grass'
_rd = 'road'
_sd = 'sand'
_sl = 'soil'
_se = 'stone'
_wr = 'water'

level0 = [
    [_wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _gs, _gs, _gs, _gs, _gs, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr],
    [_wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs,
     _gs, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr],
    [_wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs,
     _gs, _gs, _gs, _gs, _wr, _wr, _wr, _wr, _wr],
    [_wr, _wr, _wr, _wr, _wr, _wr, _wr, _wr, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs,
     _gs, _gs, _gs, _gs, _gs, _wr, _wr, _wr, _wr],
    [_wr, _wr, _wr, _wr, _wr, _wr, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs,
     _gs, _gs, _gs, _gs, _gs, _gs, _gs, _wr, _wr],
    [_wr, _wr, _wr, _wr, _wr, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs,
     _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_wr, _wr, _wr, _wr, _wr, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs,
     _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _wr, _wr, _wr, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _gs,
     _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd,
     _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd,
     _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd,
     _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd,
     _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _gs,
     _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _gs, _gs,
     _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs,
     _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs,
     _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs,
     _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs,
     _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs,
     _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs,
     _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs]
]

level1 = [
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs,
     _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs,
     _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs,
     _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs, _gs,
     _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs,
     _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs,
     _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs, _gs,
     _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs,
     _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs,
     _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs, _gs,
     _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs,
     _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs,
     _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs, _gs,
     _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs,
     _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs,
     _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd, _gs,
     _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd,
     _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd,
     _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd,
     _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs],
    [_gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _rd, _rd, _rd, _rd, _rd,
     _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs, _gs]
]

'''
level# = [
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _]
]
'''

_levelList = [level0, level1]


def getLevel(i):
    return _levelList[i]

# w32 h20
