#  This source file is part of the Avogadro project.
#  This source code is released under the 3-Clause BSD License, (see "LICENSE").

"""MMFF94 energy and gradient calculator using the text protocol."""

import json
import sys

import numpy as np
from openbabel import pybel


def run():
    # Avogadro sends one compact JSON line with the molecule and metadata.
    bootstrap = json.loads(sys.stdin.readline())
    cml_string = bootstrap["cml"]

    mol = pybel.readstring("cml", cml_string)

    ff = pybel._forcefields["mmff94"]
    success = ff.Setup(mol.OBMol)
    if not success:
        sys.exit("MMFF94 force field setup failed")

    num_atoms = len(mol.atoms)

    # Text protocol loop: read coordinates, write energy and gradients.
    while True:
        try:
            for i in range(num_atoms):
                coordinates = np.fromstring(input(), sep=" ")
                atom = mol.atoms[i]
                atom.OBAtom.SetVector(
                    coordinates[0], coordinates[1], coordinates[2]
                )
        except EOFError:
            break

        ff.SetCoordinates(mol.OBMol)

        energy = ff.Energy(True)  # in kJ/mol
        print("AvogadroEnergy:", energy)

        print("AvogadroGradient:")
        for atom in mol.atoms:
            grad = ff.GetGradient(atom.OBAtom)
            print(-1.0 * grad.GetX(), -1.0 * grad.GetY(), -1.0 * grad.GetZ())
