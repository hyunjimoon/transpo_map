# Translated to .py by Meritxell Pacheco (December 2016)
########################################################
# Updated by Evanthia Kazagli (January 2017)
########################################################
########################################################
# Adapted for PandasBiogeme by Michel Bierlaire
# Sat Nov  3 18:53:58 2018
########################################################

import pandas as pd
import biogeme.database as db
import biogeme.biogeme as bio
from biogeme.models import logit
from datetime import datetime

pandas = pd.read_table("swissmetro.dat")
database = db.Database("swissmetro", pandas)
pd.options.display.float_format = '{:.3g}'.format

globals().update(database.variables)
from biogeme.expressions import *

exclude = ((PURPOSE != 1) * (PURPOSE != 3) + (CHOICE == 0)) > 0
database.remove(exclude)

# Parameters to be estimated
# Arguments:
#   1  Name for report. Typically, the same as the variable
#   2  Starting value
#   3  Lower bound
#   4  Upper bound
#   5  0: estimate the parameter, 1: keep it fixed
ASC_CAR = Beta('ASC_CAR', -1.54, None, None, 0)
ASC_SBB = Beta('ASC_SBB', 0, None, None, 1)
ASC_SM = Beta('ASC_SM', -0.995, None, None, 0)
BETA_CAR_COST_mean = Beta('BETA_CAR_COST_mean', -1.96, None, None, 0)
BETA_CAR_COST_std = Beta('BETA_CAR_COST_std', 1.08, None, None, 0)
BETA_HE_mean = Beta('BETA_HE_mean', -0.682, None, None, 0)
BETA_HE_std = Beta('BETA_HE_std', 0.411, None, None, 0)
BETA_SM_COST_mean = Beta('BETA_SM_COST_mean', -1.79, None, None, 0)
BETA_SM_COST_std = Beta('BETA_SM_COST_std', -1.02, None, None, 0)
BETA_TIME = Beta('BETA_TIME', -1.35, None, None, 0)
BETA_TRAIN_COST_mean = Beta('BETA_TRAIN_COST_mean', -6.45, None, None, 0)
BETA_TRAIN_COST_std = Beta('BETA_TRAIN_COST_std', -2.52, None, None, 0)
# Random parameters
BETA_CAR_COST_random = BETA_CAR_COST_mean + BETA_CAR_COST_std * bioDraws('BETA_CAR_COST_random', 'NORMAL')
BETA_HE_random = BETA_HE_mean + BETA_HE_std * bioDraws('BETA_HE_random', 'NORMAL')
BETA_SM_COST_random = BETA_SM_COST_mean + BETA_SM_COST_std * bioDraws('BETA_SM_COST_random', 'NORMAL')
BETA_TRAIN_COST_random = BETA_TRAIN_COST_mean + BETA_TRAIN_COST_std * bioDraws('BETA_TRAIN_COST_random', 'NORMAL')

# Expressions
CAR_AV_SP = DefineVariable('CAR_AV_SP', CAR_AV * (SP != 0), database)
SM_COST = DefineVariable('SM_COST', SM_CO * (GA == 0), database)
TRAIN_AV_SP = DefineVariable('TRAIN_AV_SP', TRAIN_AV * (SP != 0), database)
TRAIN_COST = DefineVariable('TRAIN_COST', TRAIN_CO * (GA == 0), database)

TRAIN_TT_SCALED = DefineVariable('TRAIN_TT_SCALED', TRAIN_TT / 100.0, database)
TRAIN_COST_SCALED = DefineVariable('TRAIN_COST_SCALED', TRAIN_COST / 100, database)
SM_TT_SCALED = DefineVariable('SM_TT_SCALED', SM_TT / 100.0, database)
SM_COST_SCALED = DefineVariable('SM_COST_SCALED', SM_COST / 100, database)
CAR_TT_SCALED = DefineVariable('CAR_TT_SCALED', CAR_TT / 100, database)
CAR_CO_SCALED = DefineVariable('CAR_CO_SCALED', CAR_CO / 100, database)
TRAIN_HE_SCALED = DefineVariable('TRAIN_HE_SCALED', TRAIN_HE / 100, database)
SM_HE_SCALED = DefineVariable('SM_HE_SCALED', SM_HE / 100, database)

# Utilities
V_Car_SP = ASC_CAR + BETA_TIME * CAR_TT_SCALED + BETA_CAR_COST_random * CAR_CO_SCALED
V_SBB_SP = ASC_SBB + BETA_TIME * TRAIN_TT_SCALED + BETA_TRAIN_COST_random * TRAIN_COST_SCALED + BETA_HE_random * TRAIN_HE_SCALED
V_SM_SP = ASC_SM + BETA_TIME * SM_TT_SCALED + BETA_SM_COST_random * SM_COST_SCALED + BETA_HE_random * SM_HE_SCALED
#
V = {3: V_Car_SP, 1: V_SBB_SP, 2: V_SM_SP}
av = {3: CAR_AV_SP, 1: TRAIN_AV_SP, 2: SM_AV}

# Choice model
prob = logit(V, av, CHOICE)
logprob = log(MonteCarlo(prob))

logger = msg.bioMessage()
logger.setGeneral()

biogeme = bio.BIOGEME(database, logprob, numberOfDraws=2000)
biogeme.modelName = "Mixture_SM_RandomCoeff"
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
