__author__ = "ContraxSuite, LLC; LexPredict, LLC"
__copyright__ = "Copyright 2015-2021, ContraxSuite, LLC"
__license__ = "https://github.com/LexPredict/lexpredict-lexnlp/blob/2.2.1.0/LICENSE"
__version__ = "2.2.1.0"
__maintainer__ = "LexPredict, LLC"
__email__ = "support@contraxsuite.com"


from enum import Enum


class AnnotationLocatorType(Enum):
    RegexpBased = 1
    MlWordVectorBased = 2
