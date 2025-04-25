# Translated to .py by Meritxell Pacheco (December 2016)
########################################################
# Updated by Evanthia Kazagli (January 2017)
########################################################
# Adapted for PandasBiogeme by Michel Bierlaire
# Fri Nov  2 15:44:49 2018
########################################################

import pandas as pd
import biogeme.database as db
import biogeme.biogeme as bio
from biogeme.models import logit
from datetime import datetime

pandas = pd.read_table("swissmetro.dat")
database = db.Database("swissmetro",pandas)
pd.options.display.float_format = '{:.3g}'.format

globals().update(database.variables)
from biogeme.expressions import *

exclude = ((  PURPOSE   !=  1  ) * (  PURPOSE   !=  3  ) + (  CHOICE   ==  0  ))>0
database.remove(exclude)

#Parameters to be estimated
# Arguments:
#   1  Name for report. Typically, the same as the variable
#   2  Starting value
#   3  Lower bound
#   4  Upper bound
#   5  0: estimate the parameter, 1: keep it fixed
ASC_CAR_mean = Beta('ASC_CAR_mean',-1.23,None,None,0)
ASC_CAR_std = Beta('ASC_CAR_std',5.02,None,None,0)
ASC_SBB = Beta('ASC_SBB',0,None,None,1)
ASC_SM_mean = Beta('ASC_SM_mean',0.708,None,None,0)
ASC_SM_std = Beta('ASC_SM_std',4.67,None,None,0)
BETA_COST = Beta('BETA_COST',-3.72,None,None,0)
BETA_HE = Beta('BETA_HE',-1.18,None,None,0)
BETA_TIME = Beta('BETA_TIME',-2.99,None,None,0)
# Random parameters
ASC_CAR_random = ASC_CAR_mean + ASC_CAR_std * bioDraws('ASC_CAR_random','NORMAL')
ASC_SM_random = ASC_SM_mean + ASC_SM_std * bioDraws('ASC_SM_random','NORMAL')

# Define here arithmetic expressions for variables that are not directly
# available in the data file
CAR_AV_SP = DefineVariable('CAR_AV_SP', CAR_AV    *  (  SP   !=  0  ),database)
SM_COST = DefineVariable('SM_COST', SM_CO   * (  GA   ==  0  ),database)
TRAIN_AV_SP = DefineVariable('TRAIN_AV_SP', TRAIN_AV    *  (  SP   !=  0  ),database)
TRAIN_COST = DefineVariable('TRAIN_COST', TRAIN_CO   * (  GA   ==  0  ),database)

TRAIN_TT_SCALED = DefineVariable('TRAIN_TT_SCALED',\
                                 TRAIN_TT / 100.0,database)
TRAIN_COST_SCALED = DefineVariable('TRAIN_COST_SCALED',\
                                   TRAIN_COST / 100,database)
SM_TT_SCALED = DefineVariable('SM_TT_SCALED', SM_TT / 100.0,database)
SM_COST_SCALED = DefineVariable('SM_COST_SCALED', SM_COST / 100,database)
CAR_TT_SCALED = DefineVariable('CAR_TT_SCALED', CAR_TT / 100,database)
CAR_CO_SCALED = DefineVariable('CAR_CO_SCALED', CAR_CO / 100,database)
TRAIN_HE_SCALED = DefineVariable('TRAIN_HE_SCALED', TRAIN_HE / 100,database)
SM_HE_SCALED = DefineVariable('SM_HE_SCALED', SM_HE / 100,database)

# Utilities
V_Car_SP = ASC_CAR_random + BETA_TIME * CAR_TT_SCALED + BETA_COST * CAR_CO_SCALED
V_SBB_SP = ASC_SBB + BETA_TIME * TRAIN_TT_SCALED + BETA_COST * TRAIN_COST_SCALED + BETA_HE * TRAIN_HE_SCALED
V_SM_SP = ASC_SM_random + BETA_TIME * SM_TT_SCALED + BETA_COST * SM_COST_SCALED + BETA_HE * SM_HE_SCALED

V = {3: V_Car_SP,1: V_SBB_SP,2: V_SM_SP}
av = {3: CAR_AV_SP,1: TRAIN_AV_SP,2: SM_AV}


# Choice model
prob = logit(V,av,CHOICE)
logprob = log(MonteCarlo(prob))

biogeme = bio.BIOGEME(database,logprob,numberOfDraws=2000)
biogeme.modelName = "Mixture_SM_Heteroskedastic"
start_time = datetime.now()
results = biogeme.estimate()
print(f"Estimation time: {datetime.now() - start_time}")
# Get the results in a pandas table
pandasResults = results.getEstimatedParameters()
print(pandasResults)
print(f"Nbr of observations: {database.getNumberOfObservations()}")
print(f"LL(0) =    {results.data.initLogLike:.3f}")
print(f"LL(beta) = {results.data.logLike:.3f}")
print(f"Output file: {results.data.htmlFileName}")
