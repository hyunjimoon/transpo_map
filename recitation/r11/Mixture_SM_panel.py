# Translated to .py by Evanthia Kazagli (January 2017)
########################################################
# Adapted to PandasBiogeme by Michel Bierlaire
# Sun Nov  4 13:45:30 2018

import pandas as pd
import biogeme.database as db
import biogeme.biogeme as bio
from biogeme.models import logit
from datetime import datetime

pandas = pd.read_table("swissmetro.dat")
database = db.Database("swissmetro",pandas)
database.panel("ID")

pd.options.display.float_format = '{:.3g}'.format

globals().update(database.variables)
from biogeme.expressions import *

exclude = ((  PURPOSE   !=  1  ) * (  PURPOSE   !=  3  ) + (  CHOICE   ==  0  ) + ( AGE == 6 ))>0
database.remove(exclude)

#Parameters to be estimated
# Arguments:
#   1  Name for report. Typically, the same as the variable
#   2  Starting value
#   3  Lower bound
#   4  Upper bound
#   5  0: estimate the parameter, 1: keep it fixed
ASC_CAR = Beta('ASC_CAR',-1.33,None,None,0)
ASC_SBB = Beta('ASC_SBB',0,None,None,1)
ASC_SM = Beta('ASC_SM',-0.0916,None,None,0)
BETA_CAR_COST = Beta('BETA_CAR_COST',-2.92,None,None,0)
BETA_HE = Beta('BETA_HE',-0.965,None,None,0)
BETA_SM_COST = Beta('BETA_SM_COST',-3.06,None,None,0)
BETA_TIME = Beta('BETA_TIME',-3.17,None,None,0)
BETA_TRAIN_COST = Beta('BETA_TRAIN_COST',-5.21,None,None,0)
SIGMA_PANEL_CAR = Beta('SIGMA_PANEL_CAR',4.35,None,None,0)
SIGMA_PANEL_TRAIN = Beta('SIGMA_PANEL_TRAIN',3.16,None,None,0)
SIGMA_PANEL_SM = Beta('SIGMA_PANEL_SM',0.0752,None,None,0)

# Random parameters for Panel data
ZERO_SIGMA_PANEL_CAR = SIGMA_PANEL_CAR * bioDraws('ZERO_SIGMA_PANEL_CAR','NORMAL')
ZERO_SIGMA_PANEL_TRAIN = SIGMA_PANEL_TRAIN * bioDraws('ZERO_SIGMA_PANEL_TRAIN','NORMAL')
ZERO_SIGMA_PANEL_SM = SIGMA_PANEL_SM * bioDraws('ZERO_SIGMA_PANEL_SM','NORMAL')

# Define here arithmetic expressions for variables that are not directly
# available in the data file
CAR_AV_SP  = DefineVariable('CAR_AV_SP', CAR_AV    *  (  SP   !=  0  ),database)
SM_COST  = DefineVariable('SM_COST', SM_CO   * (  GA   ==  0  ),database)
TRAIN_AV_SP  = DefineVariable('TRAIN_AV_SP', TRAIN_AV    *  (  SP   !=  0  ),database)
TRAIN_COST  = DefineVariable('TRAIN_COST', TRAIN_CO   * (  GA   ==  0  ),database)

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
V_Car_SP = ASC_CAR + BETA_TIME * CAR_TT_SCALED + BETA_CAR_COST * CAR_CO_SCALED + ZERO_SIGMA_PANEL_CAR
V_SBB_SP = ASC_SBB + BETA_TIME * TRAIN_TT_SCALED + BETA_TRAIN_COST * TRAIN_COST_SCALED + BETA_HE * TRAIN_HE_SCALED + ZERO_SIGMA_PANEL_TRAIN
V_SM_SP = ASC_SM + BETA_TIME * SM_TT_SCALED + BETA_SM_COST * SM_COST_SCALED + BETA_HE * SM_HE_SCALED + ZERO_SIGMA_PANEL_SM
#
V = {3: V_Car_SP,1: V_SBB_SP,2: V_SM_SP}
av = {3: CAR_AV_SP,1: TRAIN_AV_SP,2: SM_AV}

obsprob = logit(V,av,CHOICE)
condprobIndiv = PanelLikelihoodTrajectory(obsprob)
logprob = log(MonteCarlo(condprobIndiv))

biogeme = bio.BIOGEME(database,logprob,numberOfDraws=2000)
biogeme.modelName = "Mixture_SM_panel"
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
