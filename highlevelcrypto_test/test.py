__author__ = 'vlim'

from highlevelcrypto import *
import pyelliptic
def authorize(request=None, public_key=None):
    # pub_k = "04fce3e9faa11a5e09de2b8e31c7a9c92dbf98f7b8fd0e49a9d3b73781e0e1a87b5e105f90d3cbaf15e1a0c9460c32b403311cc181a561fdb6dd5bdee5ac665934"
    pub_k = "04bb572205085c370623cefd2525f91fb5266cb21cad26c0a75b439d5dc5d14f5d7e5b16f1fda2dfa19835787d846825cfaf3264394b2c32e78cc849043b248036"
    cipher = encrypt("Hello", str(pub_k))
    print cipher

authorize()