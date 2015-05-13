#!/usr/bin/python3

from renderlib import *
from itertools import zip_longest

def introFramesLight(p):
    frames = int(1.5*fps)
    max_opac = 0.7

    while True:
        for i in range(0, frames):
            yield [
                ('one', 'style', 'stroke-opacity', '{:.4f}'.format(easeLinear(i, 0, max_opac, frames)))
            ]
        for i in range(0, frames):
            yield [
                ('one', 'style', 'stroke-opacity', '{:.4f}'.format(easeLinear(frames-i, 0, max_opac, frames))),
                ('cee', 'style', 'stroke-opacity', '{:.4f}'.format(easeLinear(i, 0, max_opac, frames)))
            ]
        for i in range(0, frames):
            yield [
                ('cee', 'style', 'stroke-opacity', '{:.4f}'.format(easeLinear(frames-i, 0, max_opac, frames))),
                ('two', 'style', 'stroke-opacity', '{:.4f}'.format(easeLinear(i, 0, max_opac, frames)))
            ]
        for i in range(0, frames):
            yield [
                ('two', 'style', 'stroke-opacity', '{:.4f}'.format(easeLinear(frames-i, 0, max_opac, frames)))
            ]

def introFramesDot(p):
    frames = 10*fps
    steps  = [
        (5, 0, 159),
        (33, -848, 159),
        (37, -848, 53),
        (40, -742, 53),
        (43, -742, -106),
        (45, -795, -106),
        (47, -795, -212),
        (49, -742, -212),
        (51, -742, -265),
        (56, -583, -265),
        (58, -583, -212),
        (63, -424, -212),
        (65, -424, -265),
        (75, -106, -265),
        (77, -106, -212),
        (81, 0, -212),
        (86, 0, -53),
        (93, 0, 0),
        (100, 0, 0)
    ]

    prev = (0, 0, 0)
    for step in steps:
        dur = int((step[0] - prev[0]) * frames / 100)
        for i in range(0, dur):
            yield [
                ('dot1', 'attr', 'transform', 'translate({:.4f}, {:.4f})'.format(easeLinear(i, prev[1], step[1]-prev[1], dur),
                                                                                 easeLinear(i, prev[2], step[2]-prev[2], dur)))
            ]
        prev = step

def introFrameText(p):
    frames = 2*fps

    for i in range(0, frames):
        yield [
            ('text', 'style', 'opacity', '{:.4f}'.format(easeLinear(i, 0, 1, frames)))
        ]

def introFrames(p):
    for e in zip_longest(zip(introFramesDot(p), introFramesLight(p)), introFrameText(p), fillvalue=[('text', 'style', 'opacity', '1')]):
        yield e[0][0] + e[0][1] + e[1]

def outroFrames(p):
    # 5 Sekunden stehen bleiben
    frames = 1*fps
    for i in range(0, frames):
        yield []

def debug():
    render(
        'intro.svg',
        '../intro.ts',
        introFrames,
        parameters={
            '$id': 4711,
            '$title': 'D\'r Dom',
            '$subtitle': 'Hauptbahnhof',
            '$personnames': 'Tünnes und Schäl'
        }
    )

#   render(
#       'outro.svg',
#       '../outro.ts',
#       outroFrames
#   )

def tasks(queue):
    raise NotImplementedError('call with --debug to render your intro/outro')
