from sys import argv, exit, path
from os.path import dirname, realpath


# noinspection PyUnresolvedReferences,PyProtectedMember
def _():
    # lazy way to get PyInstaller to detect the libraries, since this won't run at runtime
    import _gui
    import fmt_detect
    import reg_shell
    from mount import _common, cci, cdn, cia, exefs, nand, nanddsi, ncch, romfs, sd, srl, threedsx, titledir
    from pyctr.types import crypto, exefs, ncch, romfs, smdh, tmd, util


path.insert(0, dirname(realpath(__file__)))

if len(argv) < 2 or argv[1] in {'gui', 'gui_i_want_to_be_an_admin_pls'}:
    print('Preparing...')
    from _gui import main
    print('Starting the GUI!')
    admin = False
    if len(argv) > 1:
        admin = argv.pop(1) == 'gui_i_want_to_be_an_admin_pls'
    exit(main(_pyi=True, _allow_admin=admin))
else:
    from main import mount
    exit(mount(argv.pop(1).lower()))
