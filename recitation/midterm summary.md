Based on [lecture transcripts](https://github.com/hyunjimoon/transpo_map/tree/main/class), I extracted and synthesize the key concepts Moshe emphasized in class that I covered in computer lab.

### Computer lab 6: Time Series & Instrumental Variables
- **Time Series Autocorrelation & Consequences:**
  - OLS estimators remain unbiased and consistent under autocorrelation but become inefficient
  - Standard errors from normal OLS calculations are incorrect
  - With lagged dependent variables, OLS becomes inconsistent and biased

- **Endogeneity & Instrumental Variables:**
  - Key causes: omitted variables, measurement errors, simultaneity, lagged dependent variables with autocorrelation, self-selection
  - Instrumental variables as a solution when proper instruments can be found

- **Simultaneous Equations Models & Identification:**
  - Identification requires different exogenous variables in each equation
  - Using variables that shift one curve but not the other
  - Two-Stage Least Squares estimation of structural equations

### Computer lab 5: OLS Violations & GLS
- **Violation of OLS Assumptions:**
  - No Perfect Multicollinearity → Non-existence of estimates
  - Strict Exogeneity → Biased estimates
  - Spherical Error Variance → Inefficient but unbiased estimates
  - Normality → Affects distribution-based inference

- **Weighted Least Squares for Heteroscedasticity:**
  - Weighting observations to create homoscedastic errors
  - Implementation approaches: transformed variables vs. weighted least squares

- **Generalized Least Squares for Non-Spherical Errors:**
  - Comprehensive solution for non-spherical errors
  - GLS estimator and variance
  - Feasible GLS when variance structure is unknown

### Computer lab 3-4: Hypothesis Testing & Sample Size
- **Type I vs Type II Error Trade-off:**
  - Type I (α): Probability of rejecting H0 when true (false positive)
  - Type II (β): Probability of accepting H0 when false (false negative)
  - Key trade-off: Reducing α increases β for given sample size

- **Sample Size Determination:**
  - Setting allowable error and confidence levels
  - Effect size considerations
  - Cost constraints and budget implications

- **Stratified Sampling:**
  - Efficiency when population variance differs by strata
  - Allocation of sampling resources

### Collected hypotheses students care about and have domain knowledge on (being developed)
- 👩🏽‍🍳Chef's hypothesis: Later shift 👨🏻‍🚒workers are more likely to order 🍔lunch items at 10am
- 👨🏼‍💼Marketer's hypothesis: Umbrella usage of 👨‍👩‍👧‍👦 Boston locals during snow is lower than during ☔️ rain
- 🏢City council's hypothesis: Citizens' car ownership affects likelihood to support 🚸pedestrianization
- 🌙Angie's hypothesis: 👨‍🎓Student's 📚assignment load and 😋hungriness affect computer lab attendance
