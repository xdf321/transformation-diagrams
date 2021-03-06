#!/usr/bin/env python3
#! -*- coding: utf-8 -*-

"""
Plot TTT and CCT diagrams
"""
import argparse
import matplotlib.pyplot as plt
from transformation_models import Alloy, TransformationDiagrams

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script for plotting TTT and CCT diagrams')
    parser.add_argument('-g', '--gs', type=float, default=6, help='Grain size')
    parser.add_argument('-C', '--C', type=float, default=0., help='Carbon wt.%%')
    parser.add_argument('-Si', '--Si', type=float, default=0., help='Silicon wt.%%')
    parser.add_argument('-Mn', '--Mn', type=float, default=0., help='Manganese wt.%%')
    parser.add_argument('-Ni', '--Ni', type=float, default=0., help='Nickel wt.%%')
    parser.add_argument('-Mo', '--Mo', type=float, default=0., help='Molybdenum wt.%%')
    parser.add_argument('-Cr', '--Cr', type=float, default=0., help='Chromium wt.%%')
    parser.add_argument('-V', '--V', type=float, default=0., help='Vanadium wt.%%')
    parser.add_argument('-Co', '--Co', type=float, default=0., help='Cobalt wt.%%')
    parser.add_argument('-Cu', '--Cu', type=float, default=0., help='Copper wt.%%')
    parser.add_argument('-Al', '--Al', type=float, default=0., help='Aluminium wt.%%')
    parser.add_argument('-W', '--W', type=float, default=0., help='Tungsten wt.%%')
    parser.add_argument('-Tini', '--Tini', type=float, default=900., help='Initial continuous cooling temperature')

    args = parser.parse_args()

    comp = vars(args)
    gs = comp.pop('gs')
    Tini = comp.pop('Tini')

    # Defines alloy (grain size gs and composition)
    alloy = Alloy(gs=gs, **comp)

    # Initializes diagrams object
    diagrams = TransformationDiagrams(alloy)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    fig.subplots_adjust(wspace=.2)

    diagrams.TTT(ax=ax1)
    ax1.set_ylim(alloy.Ms - 200, Tini + 50)

    diagrams.CCT(Tini=Tini, ax=ax2)
    ax2.set_ylim(alloy.Ms - 200, Tini + 50)

    fig.suptitle(ax1.get_title())
    ax1.set_title('')
    ax2.set_title('')

    plt.show()
