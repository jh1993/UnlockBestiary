INVERT = 0

import SteamAdapter

has_slain = SteamAdapter.has_slain
SteamAdapter.has_slain = lambda name: not has_slain(name) if INVERT else True