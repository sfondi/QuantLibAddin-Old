'global constants'

# XML

FUNCGROUPS = 'funcgroups'
FUNC = 'function'
FUNCLIST = 'functionlist'
NAME = 'name'
CODENAME = 'codename'
DESC = 'description'
CTOR = 'constructor'
CLASS = 'class'
HDRONLY = 'headeronly'
PARAMS = 'parameters'
PARAM = 'param'
TYPE = 'type'
DESC = 'desc'
NUMFUNC = 'numfunc'
RETVAL = 'returnval'
PROPVEC = 'propertyvector'
XMLSUFFIX = r'(.*).xml\Z'
QLFUNC = 'qlfunction'
STRING = 'string'
LONG = 'long'
HANDLE = 'handle'

# General

CR_FILENAME = 'copyright.txt'
CR_BUFFER = ''
HEADER = '%s this file generated automatically by %s on %s\n\
%s editing this file manually is not recommended\n\n'
ADDIN_ROOT = '../Addins/'

# QuantLibAddin

QLA_ROOT = '../QuantLibAddin/functions/'
QLA_INCLUDES = 'stub.qla.includes'
QLA_INCLUDES2 = 'stub.qla.includes2'
QLA_CTOR = 'stub.qla.constructor'
QLA_FUNC = 'stub.qla.function'
QLA_CONV = 'stub.qla.conversion'

# C

C_ROOT = ADDIN_ROOT + 'C/'
C_INCLUDES = 'stub.C.includes'
C_BODY = 'stub.C.body'

# Calc

CALC_ROOT = ADDIN_ROOT + 'Calc/'
CALC_MAPFILE = 'funcdef.cpp'
CALC_MAPLINE='    funcMap[ STRFROMANSI( "%s" ) ]\n\
        =  STRFROMANSI( "%s" );\n'
CALC_AUTOHDR = 'autogen.hpp'
CALC_IDL = 'QuantLibAddin.idl'
CALC_BODY_BUF = ''
CALC_MAP = 'stub.Calc.map'
CALC_INCLUDES = 'stub.Calc.includes'
CALC_BODY = 'stub.Calc.body'
CALC_IDL_HEAD = 'stub.Calc.idlhead'
CALC_IDL_FOOT = 'stub.Calc.idlfoot'
CALC_IDL_FUNC = 'stub.Calc.idlfunc'

# Excel

XL_ROOT = ADDIN_ROOT + 'Excel/'
XL_FUNCDEF = 'funcdef.hpp'
XL_BODY_BUF = ''
XL_INCLUDES = 'stub.Excel.includes'
XL_BODY = 'stub.Excel.body'
XL_FUNC = 'stub.Excel.func'
XLMAXPARMERR = 'number of parameters exceeds Excel max of %d'
XLMAXLENERR  = 'list of parameter names exceeds max Excel length of 255:\n'
# maximum number of parameters to be passed to an Excel function -
# if you change this number you must also change the call to xlfRegister
# in QuantLibAddin\Addins\Excel\qladdin.cpp
XLMAXPARAM=15

