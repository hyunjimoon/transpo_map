# Authors: G. Antonini, E. Frejinger, C. Gioia, M. Thémans
# Translated to .py by Jing Ding-Mastera
# Adapted for PandasBiogeme by Michel Bierlaire
# Thu Nov  1 16:30:55 2018

import pandas as pd
import biogeme.database as db
import biogeme.biogeme as bio
from biogeme.models import lognested
from biogeme.expressions import Beta, DefineVariable

df = pd.read_csv("swissmetro.dat",'\t')
database = db.Database("swissmetro",df)
pd.options.display.float_format = '{:.3g}'.format
globals().update(database.variables)

exclude = ((  PURPOSE   !=  1  ) * (  PURPOSE   !=  3  ) + (  CHOICE   ==  0  ) + ( AGE == 6 ))>0
database.remove(exclude)

#Parameters to be estimated
# Arguments:
#   1  Name for report. Typically, the same as the variable
#   2  Starting value
#   3  Lower bound
#   4  Upper bound
#   5  0: estimate the parameter, 1: keep it fixed

ASC_CAR = Beta('ASC_CAR',0,None,None,0)
ASC_TRAIN = Beta('ASC_TRAIN',0,None,None,1)
ASC_SM = Beta('ASC_SM',0,None,None,0)
B_COST = Beta('B_COST',0,None,None,0)
B_CAR_TIME = Beta('B_CAR_TIME',0,None,None,0)
B_TRAIN_TIME = Beta('B_TRAIN_TIME',0,None,None,0)
B_SM_TIME = Beta('B_SM_TIME',0,None,None,0)
B_HE = Beta('B_HE',0,None,None,0)
B_GA = Beta('B_GA',0,None,None,0)
MU = Beta('MU',1,None,None,0)


#If the person has a GA (season ticket) her incremental cost is actually 0 
#rather than the cost value gathered from the
# network data. 
SM_COST =  SM_CO   * (  GA   ==  0  ) 
TRAIN_COST =  TRAIN_CO   * (  GA   ==  0  )
CAR_AV_SP =  DefineVariable('CAR_AV_SP',CAR_AV  * (  SP   !=  0  ),database)
TRAIN_AV_SP =  DefineVariable('TRAIN_AV_SP',TRAIN_AV  * (  SP   !=  0  ),database)

# For numerical reasons, it is good practice to scale the data to
# that the values of the parameters are around 1.0. 
# A previous estimation with the unscaled data has generated
# parameters around -0.01 for both cost and time. Therefore, time and
# cost are multipled my 0.01.

TRAIN_TT_SCALED = DefineVariable('TRAIN_TT_SCALED', TRAIN_TT / 100.0,database)
TRAIN_COST_SCALED = DefineVariable('TRAIN_COST_SCALED', TRAIN_COST / 100,database)
SM_TT_SCALED = DefineVariable('SM_TT_SCALED', SM_TT / 100.0,database)
SM_COST_SCALED = DefineVariable('SM_COST_SCALED', SM_COST / 100,database)
CAR_TT_SCALED = DefineVariable('CAR_TT_SCALED', CAR_TT / 100,database)
CAR_CO_SCALED = DefineVariable('CAR_CO_SCALED', CAR_CO / 100,database)
TRAIN_HE_SCALED = DefineVariable('TRAIN_HE_SCALED', TRAIN_HE / 100,database)
SM_HE_SCALED = DefineVariable('SM_HE_SCALED', SM_HE / 100,database)

# Utility functions
V1 = ASC_TRAIN + B_TRAIN_TIME * TRAIN_TT_SCALED + B_COST * TRAIN_COST_SCALED + B_HE * TRAIN_HE_SCALED + B_GA * GA
V2 = ASC_SM + B_SM_TIME * SM_TT_SCALED + B_COST * SM_COST_SCALED + B_HE * SM_HE_SCALED + B_GA * GA
V3 = ASC_CAR + B_CAR_TIME * CAR_TT_SCALED + B_COST * CAR_CO_SCALED

# Associate utility functions with the numbering of alternatives
V = {1: V1,
     2: V2,
     3: V3}

# Associate the availability conditions with the alternatives

av = {1: TRAIN_AV_SP,
      2: SM_AV,
      3: CAR_AV_SP}

#Definition of nests:
# 1: nests parameter
# 2: list of alternatives
public = MU , [1,2]
private = 1.0 , [3]
nests = public,private

# The choice model is a nested logit, with availability conditions
logprob = lognested(V,av,nests,CHOICE)
biogeme  = bio.BIOGEME(database,logprob)
biogeme.modelName = "MEV_SM_NL_Challenge"
results = biogeme.estimate()
# Get the results in a pandas table
pandasResults = results.getEstimatedParameters()
print(pandasResults)
print(f"Nbr of observations: {database.getNumberOfObservations()}")
print(f"LL(0) =    {results.data.initLogLike:.3f}")
print(f"LL(beta) = {results.data.logLike:.3f}")
print(f"rho bar square = {results.data.rhoBarSquare:.3g}")
print(f"Output file: {results.data.htmlFileName}")

