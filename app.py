from flask import Flask, render_template, jsonify, request
from openai import OpenAI
import json
import os
import random
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL = os.getenv("OPENAI_MODEL", "gpt-5.4-mini")

KNOWLEDGE_BASE = """
KEY CONCEPTS FOR O&G E&P ACCOUNTING, 3-STATEMENT MODELING & VALUATION
=====================================================================

OVERVIEW: IS, BS, CF CONNECTIONS
- IS shows performance over a period (revenue, royalties, LOE, G&A, exploration expense, DD&A, impairment, interest, tax)
- BS shows position at a point in time (assets: cash, A/R, E&E assets, PP&E, accumulated DD&A; liabilities: A/P, debt, ARO; equity: share capital, retained earnings)
- CF shows actual cash movement: CFO (operating), CFI (investing), CFF (financing)

CORE CONNECTIONS:
1. Closing retained earnings = Opening RE + Net income - Dividends
2. Closing cash = Opening cash + CFO + CFI + CFF
3. Accrual accounting creates timing differences: revenue before cash (A/R), expense before payment (A/P), capex to BS then IS via DD&A

E&P SPECIFIC RULES:
- Big capex before production; exploration accounting policy choice; DD&A driven by reserves/UOP; impairment risk; decommissioning; debt-funded cycles
- Negative CF but low IS expense (capitalized spend); positive EBITDA but weak cash (capex); large accounting loss with little cash effect (impairment)

TEN CORE E&P EXAMPLES:
1. Oil sale on credit: Dr A/R / Cr Revenue -> Dr Cash / Cr A/R (CFO when collected)
2. Royalty accrual: Dr Royalty Expense / Cr Royalty Payable -> payment CFO outflow
3. LOE: Dr LOE / Cr A/P -> payment CFO outflow
4. Development well: Dr PP&E / Cr A/P (no IS impact; CFI outflow) - KEY: cash leaves now, IS hit later via DD&A
5. DD&A: Dr DD&A Expense / Cr Accumulated DD&A (non-cash; added back in indirect CFO)
6. Dry hole (SE): Initially Dr E&E Asset / Cr Cash; later Dr Exploration Expense / Cr E&E Asset
7. ARO: Initial Dr PP&E / Cr ARO Liability; accretion Dr Accretion Expense / Cr ARO; settlement Dr ARO / Cr Cash
8. RBL draw: Dr Cash / Cr Debt (CFF; no IS impact); repayment Dr Debt / Cr Cash
9. Interest: Dr Interest Expense / Cr Interest Payable; payment CFO outflow
10. Impairment: Dr Impairment Expense / Cr PP&E (non-cash; added back in CFO)

DEFERRED TAXES:
- DTL = tax relief came earlier than book expense (e.g., accelerated tax depreciation vs book DD&A)
- DTA = book expense came earlier than tax relief (e.g., impairment not yet deductible, ARO liability)
- Total tax expense = Current tax ± movement in DTA/DTL
- ARO creates BOTH: asset side -> DTL, liability side -> DTA
- Deferred taxes are NON-CASH

SE vs FC DRY HOLE:
- Successful Efforts: dry hole expensed when determined unsuccessful; faster P&L pain; more volatile earnings
- Full Cost: dry hole stays in pool; cost recognized later via depletion/ceiling test; smoother earnings
- Cash flow IDENTICAL under both methods (CFI outflow when drilled)
- FC has ceiling test risk: if pool > PV of reserves, impairment required

VALUATION CONCEPTS:
- EV/EBITDA, NAV, DCF, reserve-based valuation
- DD&A non-cash so EBITDA strips it out
- Capex intensity matters for FCF
- Reserve life, decline curves, price assumptions drive value
- Decommissioning obligations reduce NAV

O&G ENTERPRISE VALUE & KEY METRICS:
- O&G EV = Equity Value - Cash - Net Value of Hedges/Derivatives + Debt + ARO + Preferred Stock + Minority Interest + Unfunded Pensions + Capital Leases
- Net value of hedges: total derivative assets minus total derivative liabilities on BS
- EBITDA = Operating Income + DD&A; EBITDAX = EBITDA + Exploration Expense (normalizes SE vs FC)
- Key O&G metrics: Production Costs per Mcfe/BOE, F&D Costs (All Sources and Excl. Purchases/Sales), Production Replacement Ratio, Reserve Life (R/P) Ratio, Daily Production, Oil Mix %
- F&D Costs All Sources = (Dev + Expl + Acq Expenses) / Net Reserve Additions
- Production Replacement Ratio = Net Reserve Additions / Annual Production
- Reserve Life = Proved Reserves / Annual Production
- Common multiples: EV/EBITDA, EV/EBITDAX, EV/Proved Reserves, EV/Daily Production
- Use EV-based multiples because reserves/production accrue to all investors (debt + equity)
- P/E and NI-based multiples are less relevant due to unusual tax situations and non-cash items
- Revenue growth and margins are not meaningful for commodity companies — no control over prices
- Reserve Life Ratio correlates with EV/EBITDA: longer reserves = higher multiple

EQUITY VALUE & ENTERPRISE VALUE:
- Basic Equity Value = Shares * Price; Diluted uses TSM for options, conversion for convertibles
- TSM dilution from options = # Options - (# Options * Exercise Price) / Share Price (only if in-the-money)
- Convertible dilution = # Bonds * Conversion Ratio; Conversion Ratio = Par Value / Conversion Price
- If convertibles in-the-money: count dilution in shares. If out-of-the-money: count as debt
- EV = Equity Value - Cash + Debt + Minority Interest + Preferred Stock
- Subtract equity investments (cash-like, <50% owned, not consolidated)
- Subtract NOLs (future tax shield = "free gift")
- Add capital leases, unfunded pension obligations, environmental liabilities, abandonment provisions
- Minority Interest added because subsidiary revenue/profit consolidated into parent's statements

TYPES OF DEBT & FINANCING:
- Revolver: lowest rate, floating, no amortization, 3-5yr tenor, like a credit card, maintenance covenants
- Term Loan A: low rate, floating, straight-line amortization, 4-6yr, prepayable, conservative banks
- Term Loan B: higher rate, floating, minimal amortization (e.g. 5%/yr), 4-8yr, HFs invest
- Senior Notes: fixed higher rate, cash pay, 7-10yr bullet maturity, no prepayment, incurrence covenants
- Subordinated Notes: fixed even higher rate, 8-10yr bullet, no prepayment, incurrence covenants
- Mezzanine: highest rate, fixed, 8-12yr, cash or PIK, includes preferred stock/convertible debt/PIK notes
- PIK interest: appears on IS, added back on CF (non-cash), debt balance increases each year
- Seniority order: Revolver > TLA > TLB > Senior Notes > Sub Notes > Mezz > Equity
- Secured debt backed by collateral; senior secured has first claim in bankruptcy
- Maintenance covenants: ongoing ratios (Debt/EBITDA < X, EBITDA/Interest > Y)
- Incurrence covenants: one-time restrictions (max debt, capex caps, no large acquisitions)
- Revolver draw = MAX(0, net cash shortfall after mandatory repayments)
- Optional repayment: pay down in seniority order (revolver first, then TLA, then TLB)
- RBL (Reserve-Based Lending): borrowing base set by PV of proved reserves, common in E&P

DCF ANALYSIS:
- UFCF = EBIT - Taxes + D&A + SBC - Increase in WC - CapEx → discounted at WACC → Enterprise Value
- LFCF = Pre-Tax Income - Taxes + D&A + SBC - Increase in WC - CapEx → discounted at Cost of Equity → Equity Value
- WACC = Cost of Equity * %E + Cost of Debt * %D * (1-Tax Rate) + Cost of Pref * %P
- Cost of Equity = Risk-Free Rate + Equity Risk Premium * Levered Beta
- Unlevered Beta = Levered Beta / (1 + (1-Tax Rate) * (D/E)); Relevering: reverse formula
- Terminal Value: Multiples Method (EBITDA * exit multiple) or Gordon Growth (FCF * (1+g) / (r-g))
- O&G DCF differences: additional non-cash add-backs (accretion, unrealized derivative losses, impairment); terminal multiple on EBITDA/EBITDAX/Daily Production not FCF; Gordon Growth usually 0% for depleting assets; often use 10% industry discount rate instead of WACC
- DCFs often don't work well for E&P: high capex makes FCF low/negative, over-reliance on terminal value
- Mid-year convention: discount periods 0.5, 1.5, 2.5 instead of 1, 2, 3
- Sensitivity tables: vary commodity prices and discount rate (not revenue growth/margins)

NAV MODELING (NET ASSET VALUE):
- NAV = sum of PV of after-tax cash flows from each asset, valued separately, then aggregated
- Key difference vs DCF: NAV assumes no new reserve additions (no exploration/acquisition capex beyond developing existing reserves); valued at asset level not corporate level
- Reserve categories: PDP (Proved Developed Producing), PDNP (Proved Developed Non-Producing), PUD (Proved Undeveloped), PROB (Probable), POSS (Possible), POT (Potential)
- Reserve credits (risk factors): ~90%+ for Proved, ~50% for Probable, ~10% for Possible, <10% for Potential
- 1P NAV (Proved only), 2P NAV (Proved + Probable), 3P NAV (Proved + Probable + Possible)
- Price decks: High/Mid/Low scenarios; Strip Pricing (NYMEX futures); SEC Pricing (trailing 12-month avg)
- PDP/PDNP: use fixed decline rate (solve via Goal Seek so reserves exhaust over expected life); R/P ratio guides reserve life
- PUD/PROB/POSS: project new wells drilled per region per year; use type curves (gross → net after royalties)
- EUR (Estimated Ultimate Recovery): total reserves per well; IP Rate = initial production rate
- D&C Costs (Drilling & Completion): capex per well, does NOT include ongoing LOE or maintenance
- Production decline: steep in year 1-2 (especially unconventional/horizontal), then levels off
- Working Interest: proportional ownership of well — splits revenue, opex, and capex proportionally
- Royalty Rate: landowner gets % of production/revenue but pays NO expenses; Revenue Interest = 1 - Royalty Rate
- Net production = Gross * Working Interest * (1 - Royalty Rate); Net Wells = Gross * WI%
- Opex in NAV: LOE per Mcfe/BOE, production taxes (% of revenue), gathering/transport per Mcfe
- When adjusting opex for royalty-adjusted revenue, divide by (1 - Royalty Rate) to get true cost
- NAV CapEx for new wells = D&C cost * net wells drilled * reserve credit
- Standard discount rate = 10% for O&G industry; mid-year convention and stub period adjustment apply
- After NAV of reserves: add undeveloped acreage value ($/acre), add value of other segments (midstream, downstream, chemicals via EBITDA multiples)
- Balance sheet adjustments: add cash, subtract debt/preferred/minority to get implied equity value and per-share price
- Hedging: swaps (fixed price for portion of production), puts (floor price protection), collars (floor + ceiling range)
- Tax in NAV: IDC (Intangible Drilling Costs) expensed immediately for tax; TDC (Tangible) capitalized and depreciated via MACRS; Tax basis of Net PP&E = Book PP&E - DTL/Tax Rate; NOL carryforwards offset future taxable income

M&A / MERGER MODELING:
- Stock Purchase: buyer gets all assets/liabilities, shareholders sell, single taxation (cap gains), buyer assumes seller's tax basis, goodwill not tax-deductible
- Asset Purchase: buyer picks assets/liabilities, double taxation, buyer gets tax step-up, goodwill amortized 15yr and tax-deductible, seller NOLs lost
- 338(h)(10): stock purchase treated as asset purchase for tax — buyer gets everything, tax step-up, goodwill tax-deductible, seller NOLs lost
- New Goodwill = Equity Purchase Price - Seller Book Value + Seller Existing Goodwill - PP&E Write-Up - Intangibles Write-Up - Seller DTL + DTA Write-Down + New DTL (stock purchase only)
- New DTL (stock purchase) = Total Asset Write-Up * Buyer Tax Rate; zero in asset/338
- Intangibles Write-Up = % of (Purchase Price - Book Value + Existing Goodwill); amortized ~5yr book, 15yr tax
- Sources & Uses must balance; Sources: cash, new stock, new debt, assumed debt; Uses: equity value, fees, refinanced debt
- Combined IS: add revenues + synergies; add operating income + expense synergies; apply buyer tax rate
- Acquisition effects: foregone interest on cash used, new interest on acquisition debt, intangibles amortization, financing fee amortization, PP&E write-up depreciation
- Synergies: revenue (higher ASP/volume), expense (headcount, buildings, capex), CapEx reduction → lower depreciation
- Accretion/Dilution: Combined EPS vs buyer standalone EPS; accretive if higher, dilutive if lower
- Contribution analysis: buyer% EBITDA = Buyer EBITDA / (Buyer + Seller EBITDA); implies ownership split
- Book vs Cash taxes: book tax from combined pre-tax income * rate; cash tax adjusts for items deductible/non-deductible for tax; DTL increases if book taxes > cash taxes, decreases if opposite

UKCS (UK CONTINENTAL SHELF) TAX REGIME:
- Permanent regime: 30% RFCT + 10% SC = 40% base; plus EPL 38% (since 1 Nov 2024, runs to 31 Mar 2030)
- Headline stack often quoted as 78% but you must NOT tax a single base at 78% — the bases and relief rules differ
- RFCT (Ring Fence Corporation Tax): 30%, charged on ring-fence upstream trading profits; ring fence isolates upstream from other group activities; most qualifying capex gets 100% first-year allowances (FYA); PRT paid is deductible from RFCT base
- Supplementary Charge (SC): 10% on adjusted ring-fence profits; CRITICAL: financing costs are EXCLUDED from SC base (common modeling mistake); SC has its own Investment Allowance (IA) = 62.5% of qualifying expenditure, reduces SC only, not RFCT; activated when field has production income
- Energy Profits Levy (EPL): 38% rate, separate levy schedule; investment allowance removed post-Nov 2024; decarbonisation allowance reduced to 66%; 100% FYA still allowed; EPL losses are separate — cannot cross into RFCT/SC; EPL losses: 12-month carryback, terminal losses 3-year carryback, carryforward while trade continues; CRITICAL: decommissioning expenditure is NOT deductible for EPL
- Decommissioning: immediate 100% relief for RFCT and SC; extended carryback to 17 Apr 2002 for qualifying periods; legacy PRT refunds on pre-16-Mar-1993 fields (PRT rate = 0% but historic payments refundable via decomm losses); Decommissioning Relief Deeds (DRDs) lock in 2013-regime relief
- RFES (Ring Fence Expenditure Supplement): 10% uplift on unused ring-fence losses for pre-production companies, up to 10 accounting periods
- Cash tax timing: CT due 9 months + 1 day after period end; large/very large companies pay quarterly instalments; EPL follows CT payment mechanics
- Common modeling mistakes: flat 78% rate, deducting finance costs from SC, deducting decomm from EPL, ignoring SC IA, ignoring PRT refunds, hard-coding post-2030 tax without separating current law from announced policy
- NSTA economics ≠ commercial after-tax valuation; NSTA uses pre-tax, 10% real discount rate
- Proposed future: OGPM (Oil and Gas Price Mechanism) 35% revenue-based tax above $90/bbl and 90p/therm, intended to replace EPL; not yet enacted
"""

TOPIC_PROMPTS = {
    "ep_accounting": "Focus on E&P-specific accounting: journal entries, double-entry mechanics, successful efforts vs full cost, exploration accounting, capitalization rules, DD&A unit-of-production, ARO/decommissioning recognition and accretion, impairment triggers and entries, royalty and LOE treatment.",
    "three_statement": "Focus on three-statement modeling: how IS, BS, and CF connect, the indirect CFO method, why DD&A/impairment are added back, how capex flows through BS then IS, working capital movements, how debt affects CF but not IS at inception, retained earnings bridge, cash bridge.",
    "valuation": "Focus on E&P valuation: EV/EBITDA, NAV calculation, DCF for upstream, reserve-based lending, how reserves drive DD&A and value, impact of price assumptions, decommissioning in NAV, FCF vs accounting profit, why EBITDA strips DD&A, capex intensity impact on FCF multiples.",
    "deferred_tax": "Focus on deferred tax accounting in E&P: DTA vs DTL mechanics, accelerated tax depreciation creating DTL, impairment creating DTA, ARO creating both DTA and DTL simultaneously, accretion increasing DTA, DD&A releasing DTL, settlement reversing DTA, total tax expense formula, cash taxes vs book taxes.",
    "ukcs_tax": "Focus on UKCS (UK Continental Shelf) upstream tax regime: RFCT at 30%, Supplementary Charge at 10% (financing costs excluded), EPL at 38% (separate loss pool, no decomm deduction), the headline 78% stack and why you must not apply it as a flat rate, SC Investment Allowance (62.5%), 100% first-year allowances, decommissioning relief and extended carryback, legacy PRT refunds, RFES for pre-production companies, DRDs, cash tax timing and quarterly instalments, NSTA vs commercial economics, and common UKCS modeling mistakes.",
    "og_ev_metrics": "Focus on O&G enterprise value calculation and key operating/valuation metrics: how EV differs for O&G (net hedges, ARO), EBITDA vs EBITDAX, F&D costs (all sources vs excl. purchases/sales), production replacement ratio, reserve life R/P ratio, daily production, oil mix %, EV/EBITDA, EV/EBITDAX, EV/Proved Reserves, EV/Daily Production, why EV-based not P/E, why revenue metrics are irrelevant for commodity companies, reserve life correlation with multiples.",
    "debt_financing": "Focus on types of debt and financing: revolver mechanics, Term Loan A vs B, Senior Notes, Subordinated Notes, Mezzanine/PIK, floating vs fixed rates, tenor, amortization vs bullet maturity, prepayment, seniority/priority in bankruptcy, secured vs unsecured, call protection, maintenance vs incurrence covenants, leverage ratios (Debt/EBITDA), coverage ratios (EBITDA/Interest), PIK interest treatment on IS/CF/BS, revolver draw formula, optional repayment waterfall, reserve-based lending in E&P.",
    "dcf": "Focus on DCF analysis: unlevered vs levered free cash flow formulas, WACC calculation, cost of equity via CAPM, beta unlevering and relevering, terminal value via multiples method and Gordon Growth, mid-year discount convention, O&G DCF specifics (10% industry discount, 0% terminal growth for depleting assets, EBITDAX terminal multiple, sensitivity on commodity prices not revenue growth), why DCFs often don't work well for high-capex E&P companies.",
    "nav_modeling": "Focus on O&G NAV modeling: asset-level valuation vs corporate DCF, no new exploration/acquisition assumption, reserve categories (PDP/PDNP/PUD/PROB/POSS), reserve credits as risk factors, price deck scenarios (strip/SEC/custom), decline curves and Goal Seek for PDP, EUR and IP rate for new wells, D&C costs, working interest and royalty rate mechanics (gross vs net production/wells), type curves (gross and net), royalty adjustment in opex, well spacing and drilling schedules, IDC vs TDC for tax, MACRS depreciation, NOL carryforwards, hedging (swaps/puts/collars), undeveloped acreage valuation, aggregation across regions.",
    "ma_modeling": "Focus on M&A and merger modeling: stock purchase vs asset purchase vs 338(h)(10) election, goodwill creation formula, PP&E and intangibles write-ups, new DTL in stock purchase, DTA write-down from lost NOLs, sources and uses balancing, combined balance sheet adjustments, acquisition effects (foregone interest, new debt interest, intangibles amortization, financing fees, PP&E depreciation), revenue and expense synergies, accretion/dilution analysis, contribution analysis, book vs cash taxes in merger model, debt schedules for acquisition debt.",
}

MIXED_SUB_TOPICS = {
    "ep_accounting": [
        "Journal entries for an oil sale on credit and subsequent cash collection",
        "Royalty / production tax accrual, payment, and IS/BS/CF impact",
        "Lease operating expense (LOE) invoice booking and cash settlement",
        "Capitalizing a development well: why no IS hit now, CFI outflow mechanics",
        "DD&A on a producing field using unit-of-production method",
        "Successful efforts: exploratory well initially capitalized then written off as dry hole",
        "Full cost method: dry hole stays in pool, later depletion or ceiling test",
        "Comparing SE vs FC treatment of the same dry hole across all 3 statements",
        "Full cost ceiling test: when it triggers, journal entry, statement impact",
        "ARO / decommissioning initial recognition: Dr PP&E / Cr ARO",
        "ARO accretion expense over time and how the BS still balances",
        "ARO settlement: actual abandonment payment vs. carrying amount, gain or loss",
        "Impairment of producing assets after a commodity price drop",
        "Non-cash expenses in E&P: DD&A, impairment, accretion, exploration write-off",
        "Working capital in upstream: A/R from oil sales, A/P to drilling contractors",
        "Inventory accounting for produced crude: cost of sales entry",
        "G&A expense recognition in an E&P company",
        "Exploration expense under successful efforts when a well is still being evaluated",
    ],
    "three_statement": [
        "How net income bridges from IS into retained earnings on BS",
        "The indirect CFO method: starting from net income and adjusting for non-cash items",
        "Why DD&A is added back in indirect CFO even though it is a real expense",
        "Why impairment is added back in CFO: large accounting loss with no cash impact",
        "How development capex flows: cash out now (CFI), BS asset now, IS expense later via DD&A",
        "Working capital movements: increase in A/R reduces CFO, increase in A/P increases CFO",
        "Debt draw affects CFF and BS but not IS at inception — only interest hits IS later",
        "The cash bridge: opening cash + CFO + CFI + CFF = closing cash",
        "How a company can have positive EBITDA but negative free cash flow",
        "How a company can report an accounting loss but no cash drain (impairment period)",
        "Retained earnings roll-forward: opening + NI - dividends = closing",
        "Interest accrual: IS expense now, BS payable now, CFO outflow when paid",
        "Dry hole write-off under SE: non-cash in CFO at the write-off date, CFI outflow when drilled",
        "Accretion is non-cash on CF but real on IS and BS — how to reconcile",
        "How debt principal repayment is CFF only and never hits IS",
        "Capex-heavy periods: why CFI can be large negative while IS looks clean",
    ],
    "valuation": [
        "EV/EBITDA for E&P: why EBITDA strips DD&A and what that means for comparability",
        "NAV calculation for an upstream company: PV of reserves minus liabilities",
        "DCF valuation for an E&P asset: production profile, price deck, opex, capex, discount rate",
        "How proved reserves drive both DD&A (UOP) and asset value simultaneously",
        "Impact of oil price assumptions on NAV and impairment testing",
        "Decommissioning obligations reducing NAV: ARO as a valuation deduction",
        "FCF vs accounting profit: why capex intensity matters for E&P multiples",
        "Reserve-based lending (RBL): how lenders use PV of reserves as collateral",
        "Decline curve analysis and its impact on production forecasts and valuation",
        "Reserve replacement ratio and its significance for long-term E&P value",
        "Why two similar E&P operators can have very different book values (SE vs FC)",
        "PV-10 as a standardized reserve valuation metric",
        "Finding & development cost per BOE as an efficiency metric",
        "Recycle ratio: operating netback per BOE divided by F&D cost",
        "How tax shields from DD&A and DTA affect after-tax DCF valuation",
    ],
    "deferred_tax": [
        "DTL from accelerated tax depreciation vs slower book DD&A on a producing well",
        "DTA from impairment booked now but not tax-deductible until disposal",
        "ARO at inception creating BOTH a DTL (asset side) and DTA (liability side)",
        "Year-over-year DTL release as DD&A on the ARO asset progresses",
        "Year-over-year DTA growth as accretion increases the ARO liability",
        "Final abandonment payment: DTA reversal as tax deduction finally arrives",
        "Total tax expense = current tax + deferred tax expense - deferred tax benefit",
        "Why deferred tax entries are non-cash and how they appear in indirect CFO",
        "Accrued remediation expense creating a DTA (liability-side DTA pattern)",
        "NOL carryforward as a DTA in an E&P company with exploration losses",
        "IDC (intangible drilling costs) immediate tax deduction creating a DTL",
        "How cash taxes differ from book tax expense due to DTA/DTL timing",
    ],
    "og_ev_metrics": [
        "How O&G Enterprise Value differs: subtracting net value of hedges/derivatives and adding ARO",
        "EBITDA vs EBITDAX: why EBITDAX normalizes the SE vs FC accounting policy difference",
        "Calculating F&D costs all sources vs excluding purchases and sales, and what each version tells you",
        "Production Replacement Ratio: formula, what it means if below 100%, all sources vs organic",
        "Reserve Life Ratio (R/P): formula, interpretation, and why it correlates with EV/EBITDA multiples",
        "Why EV/EBITDA and EV/EBITDAX are the primary O&G multiples, not P/E or revenue multiples",
        "EV/Proved Reserves and EV/Daily Production as O&G-specific valuation multiples",
        "Why revenue growth and EBITDA margins are not meaningful for commodity companies",
        "Production costs per Mcfe/BOE: what it measures and how to calculate it",
        "Oil Mix % and its impact on valuation and comparability between E&P companies",
        "Common EBITDAX add-backs: ARO accretion, unrealized derivative losses, impairment charges, exploration expense",
        "Selecting comparable companies for O&G: using reserves and daily production instead of revenue/EBITDA size",
        "Treasury Stock Method for calculating diluted equity value in an E&P context",
    ],
    "debt_financing": [
        "Revolver mechanics: credit card analogy, draw formula, no amortization, floating rate, maintenance covenants",
        "Term Loan A vs Term Loan B: differences in rate, amortization, tenor, and investor base",
        "Senior Notes: fixed rate, bullet maturity, no prepayment, incurrence covenants — when companies use them",
        "Mezzanine debt: PIK interest mechanics — IS expense, CF add-back, BS balance increases each year",
        "Seniority waterfall in bankruptcy: revolver > TLA > TLB > senior notes > sub notes > mezz > equity",
        "Maintenance covenants: Debt/EBITDA and EBITDA/Interest thresholds, who requires them and why",
        "Incurrence covenants: restrictions on additional debt, asset sales, acquisitions, capex — tied to high-yield debt",
        "PIK Toggle notes: how interest can switch between cash pay and accrual to principal",
        "Reserve-based lending (RBL) in E&P: borrowing base tied to PV of proved reserves, redetermination risk",
        "Optional debt repayment waterfall: revolver first, then TLA, then TLB, formula mechanics",
        "Mandatory vs optional repayment formulas for term loans in an LBO or E&P context",
        "Floating vs fixed interest rates: L+spread mechanics, impact when rates rise or fall",
        "Secured vs unsecured debt: collateral, recovery rates, and how it affects interest rates",
        "How debt draw affects BS and CFF but not IS at inception — only interest hits IS later",
    ],
    "dcf": [
        "Unlevered Free Cash Flow formula: EBIT - taxes + D&A + SBC - delta WC - CapEx → gives Enterprise Value",
        "Levered Free Cash Flow: Pre-Tax Income - taxes + D&A + SBC - delta WC - CapEx → gives Equity Value",
        "WACC formula: weighted average of cost of equity, after-tax cost of debt, and cost of preferred",
        "Cost of Equity via CAPM: Risk-Free Rate + ERP * Levered Beta",
        "Unlevering and relevering beta: formulas, why you use median unlevered beta of comps then relever",
        "Terminal Value via Multiples Method: final year EBITDA * exit multiple from comps",
        "Terminal Value via Gordon Growth: FCF * (1+g) / (r-g), why g is often 0% for depleting O&G assets",
        "Mid-year discount convention: using 0.5, 1.5, 2.5 for discount periods instead of 1, 2, 3",
        "O&G DCF specifics: 10% industry discount rate, EBITDAX terminal multiple, commodity price sensitivity",
        "Why traditional DCFs often fail for E&P: high capex reduces FCF, over-reliance on terminal value",
        "Discounting Terminal Value: PV = TV / (1+r)^n, using final period for n",
        "From Enterprise Value to implied share price: add cash, subtract debt/preferred/minority, divide by diluted shares",
        "Sensitivity tables in O&G DCF: vary commodity prices and discount rate, not revenue growth",
        "Stock-Based Compensation as a non-cash expense added back in FCF calculation",
    ],
    "nav_modeling": [
        "NAV vs DCF: asset-level vs corporate-level, no new exploration/acquisition, finite reserve life",
        "Reserve categories: PDP, PDNP, PUD, PROB, POSS — definitions and typical recovery probabilities",
        "Reserve credits: risk-adjusting cash flows by reserve category (90%+ Proved, 50% Probable, 10% Possible)",
        "1P, 2P, 3P NAV: which reserve categories each includes and when you'd use each",
        "Price deck scenarios: Strip Pricing from NYMEX futures, SEC Pricing from trailing 12-month average, custom High/Mid/Low",
        "PDP decline rate estimation: using Goal Seek to solve for a fixed rate that depletes reserves over expected life",
        "EUR (Estimated Ultimate Recovery) per well: definition, how it drives reserve life and type curves",
        "IP Rate (Initial Production Rate): ambiguity in definition, why Year 1 production is a % of IP*365",
        "D&C Costs (Drilling & Completion): capex per well, does not include LOE or maintenance, drives total CapEx",
        "Working Interest mechanics: proportional split of revenue, opex, and capex among well owners",
        "Royalty rate: landowner gets % of revenue but pays ZERO expenses; Revenue Interest = 1 - Royalty Rate",
        "Gross vs Net production/wells/acres: Net = Gross * Working Interest (before royalties typically)",
        "Net Type Curve: Gross production * (1 - Royalty Rate); multiplied by net wells drilled for annual aggregation",
        "Why you divide operating expenses by (1 - Royalty Rate) when using royalty-adjusted revenue in NAV",
        "Well spacing: acreage / wells, used to estimate drilling locations and cross-check company plans",
        "Drilling schedules: more wells when prices high, fewer when low, constrained by total locations",
        "IDC vs TDC in NAV tax: intangible drilling costs expensed immediately, tangible capitalized and MACRS depreciated",
        "Tax basis of Net PP&E = Book PP&E - DTL/Tax Rate — reflects accelerated tax depreciation already taken",
        "Hedging in NAV: swaps fix price, puts set floor, collars set floor+ceiling — volume and price components",
        "Undeveloped acreage valuation: $/acre by region, added to PV of reserves in NAV",
        "PV-10: standardized reserve value at 10% discount using SEC pricing, disclosed in annual filings",
    ],
    "ma_modeling": [
        "Stock Purchase vs Asset Purchase vs 338(h)(10): who sells, what transfers, tax treatment differences",
        "Goodwill creation formula: Equity Purchase Price - Book Value + Existing Goodwill - Write-Ups - DTL + DTA Write-Down + New DTL",
        "PP&E and Intangibles write-ups in purchase price allocation: how they affect book and tax depreciation/amortization",
        "New DTL in stock purchase = Total Asset Write-Up * Tax Rate; zero in asset/338(h)(10) — why the difference",
        "DTA write-down from lost NOLs: full write-off in asset/338(h)(10), Section 382 limit in stock purchase",
        "Sources & Uses: must balance; sources = cash + stock + debt + assumed items; uses = equity value + fees + refinanced debt",
        "Combined Balance Sheet adjustments: wipe seller equity, add write-ups, create goodwill, adjust DTL/DTA",
        "Acquisition effects on combined IS: foregone interest on cash, new interest on debt, intangibles amortization, PP&E depreciation",
        "Revenue synergies: higher ASP or cross-selling; must deduct associated COGS at seller's gross margin",
        "Expense synergies: headcount cuts, building consolidation, CapEx reduction and corresponding lower depreciation",
        "Accretion/Dilution: combined EPS vs buyer standalone EPS; accretive = higher, dilutive = lower",
        "Contribution analysis: Buyer % of EBITDA implies ownership split and seller valuation",
        "Book vs Cash taxes in merger model: add back book-only amortization, subtract tax-deductible items, apply NOLs",
        "Debt schedule in merger model: mandatory repayment + optional repayment in seniority order",
        "Goodwill: never amortized for book purposes; amortized 15yr for tax in asset/338(h)(10) only",
        "Financing fees: capitalized on BS and amortized over debt life (not expensed immediately under new rules)",
    ],
    "ukcs_tax": [
        "UKCS headline tax stack: 30% RFCT + 10% SC + 38% EPL = 78%, and why you must not apply it as a flat rate",
        "Ring Fence Corporation Tax (RFCT): what the ring fence isolates and why it exists",
        "100% first-year allowances (FYA) on qualifying UKCS development capex for RFCT",
        "Supplementary Charge: why financing costs are excluded from the SC base",
        "SC Investment Allowance: 62.5% of qualifying spend, reduces SC only, activation rules",
        "EPL as a separate levy: 38% rate, its own loss pool, losses cannot cross into RFCT/SC",
        "EPL loss mechanics: 12-month carryback, 3-year terminal carryback, carryforward rules",
        "Why decommissioning expenditure is NOT deductible for EPL and how that affects terminal-year economics",
        "Decommissioning relief under RFCT and SC: immediate 100% relief and extended carryback to 17 Apr 2002",
        "Legacy PRT refunds: PRT at 0% rate but historic payments refundable through decommissioning losses on old fields",
        "Decommissioning Relief Deeds (DRDs): purpose, the 2013 regime lock-in, relevance to transactions",
        "RFES (Ring Fence Expenditure Supplement): 10% uplift for pre-production companies, up to 10 periods",
        "Cash tax timing on UKCS: 9 months + 1 day baseline, quarterly instalments for large companies",
        "NSTA pre-tax economics vs commercial after-tax DCF: why they give different answers",
        "Common UKCS modeling mistakes: flat 78%, finance costs in SC, decomm in EPL, ignoring SC IA",
        "Proposed OGPM: 35% revenue-based tax above $90/bbl threshold, not yet enacted vs EPL current law",
        "How tariff income from infrastructure access is treated across RFCT, SC, and EPL",
        "Calculating after-tax NPV for a UKCS field with separate RFCT / SC / EPL schedules",
    ],
}


def pick_mixed_guidance():
    """Randomly select a category and a specific sub-topic for variety."""
    category = random.choice(list(MIXED_SUB_TOPICS.keys()))
    sub_topic = random.choice(MIXED_SUB_TOPICS[category])
    category_label = {
        "ep_accounting": "E&P Accounting",
        "three_statement": "3-Statement Modeling",
        "valuation": "Valuation",
        "deferred_tax": "Deferred Tax",
        "ukcs_tax": "UKCS Tax Regime",
        "og_ev_metrics": "O&G EV & Key Metrics",
        "debt_financing": "Debt & Financing",
        "dcf": "DCF Analysis",
        "nav_modeling": "NAV Modeling",
        "ma_modeling": "M&A / Merger Modeling",
    }[category]
    return (
        f"Category: {category_label}.\n"
        f"Specific sub-topic you MUST base this question on: {sub_topic}\n"
        f"Do NOT deviate to a different sub-topic. Build the question squarely around the sub-topic above."
    )


LETTERS = ["A", "B", "C", "D"]


def build_options(result):
    """Assign and shuffle A/B/C/D from the model's text-based answer lists.

    Expects: correct_answer (str), wrong_answers (list of 3 str).
    Produces: options dict {A..D}, correct letter.
    """
    correct_text = result["correct_answer"].strip()
    wrong_texts = [w.strip() for w in result["wrong_answers"][:3]]

    items = [(True, correct_text)] + [(False, t) for t in wrong_texts]
    random.shuffle(items)

    options = {}
    correct_letter = "A"
    for letter, (is_correct, text) in zip(LETTERS, items):
        options[letter] = text
        if is_correct:
            correct_letter = letter

    return {
        "question": result["question"],
        "options": options,
        "correct": correct_letter,
        "explanation": result["explanation"],
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/question", methods=["POST"])
def generate_question():
    data = request.json or {}
    topic = data.get("topic", "mixed")
    difficulty = data.get("difficulty", "intermediate")

    if topic == "mixed":
        topic_guidance = pick_mixed_guidance()
    else:
        topic_guidance = TOPIC_PROMPTS.get(topic, pick_mixed_guidance())

    user_prompt = f"""Generate a single multiple-choice quiz question.

Topic focus: {topic_guidance}
Difficulty: {difficulty}

Requirements:
- The question should test practical understanding, not just definitions
- Include realistic numbers where appropriate (e.g., journal entries, calculations)
- Make wrong answers plausible but clearly wrong to someone who knows the material
- The explanation should teach the concept, referencing journal entries and statement impacts where relevant
- Do NOT use option letters (A, B, C, D) anywhere in the explanation. Refer to the correct answer by its full text instead.

Return valid JSON with exactly this structure:
{{
  "question": "The question text",
  "correct_answer": "The full text of the correct answer",
  "wrong_answers": ["Wrong answer 1", "Wrong answer 2", "Wrong answer 3"],
  "explanation": "Detailed explanation of why the correct answer is right and why each wrong answer is wrong. Reference the answers by their text, NOT by letter. Reference journal entries, statement impacts, and E&P concepts."
}}"""

    is_reasoning = MODEL.startswith("o")

    if is_reasoning:
        messages = [
            {
                "role": "user",
                "content": f"You are an expert quiz master for Oil & Gas E&P financial accounting, 3-statement modeling, and valuation. Use this knowledge base to craft questions:\n\n{KNOWLEDGE_BASE}\n\n---\n\n{user_prompt}"
            }
        ]
    else:
        messages = [
            {
                "role": "system",
                "content": f"You are an expert quiz master for Oil & Gas E&P financial accounting, 3-statement modeling, and valuation. Use this knowledge base to craft questions:\n\n{KNOWLEDGE_BASE}"
            },
            {"role": "user", "content": user_prompt}
        ]

    try:
        api_kwargs = {
            "model": MODEL,
            "messages": messages,
            "response_format": {"type": "json_object"},
        }
        if not is_reasoning:
            api_kwargs["temperature"] = 0.9

        response = client.chat.completions.create(**api_kwargs)

        result = json.loads(response.choices[0].message.content)

        required = {"question", "correct_answer", "wrong_answers", "explanation"}
        if not required.issubset(result.keys()):
            return jsonify({"error": "Invalid response structure from AI"}), 500
        if len(result["wrong_answers"]) < 3:
            return jsonify({"error": "Not enough wrong answers generated"}), 500

        return jsonify(build_options(result))

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
