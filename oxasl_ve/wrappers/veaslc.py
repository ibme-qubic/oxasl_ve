"""
Wrapper for epi_reg command
"""

from fsl.wrappers import wrapperutils  as wutils

@wutils.fileOrImage('data', 'roi', outprefix='out')
@wutils.fileOrArray('veslocs', 'encdef')
@wutils.fslwrapper
def veaslc(data, roi, veslocs, encdef, imlist, modmat, out="veaslc", method="map", **kwargs):
    """
    Wrapper for the ``veaslc`` command.
    
    Required options:
    
    Additional options:
    """

    valmap = {
        'inferv' : wutils.SHOW_IF_TRUE,
        'debug' : wutils.SHOW_IF_TRUE,
    }

    cmd = ['veasl', '--data=%s' % data, '--mask=%s' % roi, '--enc-setup=%s' % encdef, 
           '--imlist=%s' % imlist, '--vessels=%s' % veslocs, '--modmat=%s' % modmat,
           '--out=%s' % out]
    if method == "map":
        cmd.append('--map')

    cmd += wutils.applyArgStyle('--=', valmap=valmap, singlechar_args=True, **kwargs)
    
    return cmd