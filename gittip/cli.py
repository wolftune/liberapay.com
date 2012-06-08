"""This is installed as `payday`.
"""
from gittip import wireup


def payday():
    wireup.db()
    wireup.samurai()


    # Lazily import the billing module.
    # =================================
    # This dodges a problem where db in billing is None if we import it from 
    # gittip before calling wire_samurai, and it also dodges:
    #
    #   https://github.com/FeeFighters/samurai-client-python/issues/8

    from gittip import billing


    try:
        billing.payday()
    except KeyboardInterrupt:
        pass
    except:
        import aspen
        import traceback
        aspen.log(traceback.format_exc())
