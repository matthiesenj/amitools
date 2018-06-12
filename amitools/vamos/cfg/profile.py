from amitools.vamos.cfgcore import *


class ProfileParser(Parser):
  def __init__(self):
    def_cfg = {
        "profile": {
            "libs": {
                "names": ValueList(str),
                "all": False,
                "calls": False
            },
            "output": {
                "file": Value(str),
                "append": False,
                "dump": False
            }
        }
    }
    arg_cfg = {
        "profile": {
            "libs": {
                "names": Argument('--profile-libs', action='append',
                                  help="lib/dev name list to profile"),
                "all": Argument('--profile-all-libs', action='store_true',
                                help="profile all vamos libraries and devices"),
                "calls": Argument('--profile-lib-calls', action='store_true',
                                  help="store each lib call individually")
            },
            "output": {
                "file": Argument('--profile-file', action='store',
                                 help="file name for profile data"),
                "append": Argument('--profile-file-append', action='store_true',
                                   help="if profile file exists add data"),
                "dump": Argument('--profile-dump', action='store_true',
                                 help="dump the profile result to log")
            }
        }
    }
    Parser.__init__(self, def_cfg, arg_cfg,
                    "profile", "lib profiling options")
