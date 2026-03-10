# avogadro-ob-energy
Avogadro2 plugin to use Open Babel forcefields

Open Babel offers several forcefields:
- GAFF
- MMFF94 & MMFF94s
- UFF

While Avogadro includes its own UFF implementation, depending on how your package is compiled, it may not include fast integration with Open Babel for GAFF and MMFF94 / MMFF94s

This plugin installs Open Babel through Python. It's also a good example of implementing a force field / energy model in Avogadro2
