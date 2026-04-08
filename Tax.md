Below is a modeling-first pack for a UK Continental Shelf (UKCS) upstream E&P model. The biggest mistake in UKCS models is to collapse tax into one headline rate. You should build separate schedules for RFCT, Supplementary Charge, EPL, legacy PRT/decommissioning effects, and cash tax timing. That is the difference between a rough deck number and a decision-grade model. 
1) What the current UKCS fiscal regime is
Today’s permanent upstream regime is 30% Ring Fence Corporation Tax (RFCT) plus 10% Supplementary Charge (SC). PRT is still legally present for older fields but its rate is 0%; it remains relevant mainly because decommissioning losses on old PRT fields can generate repayments of historic PRT. 
On top of that, there is the Energy Profits Levy (EPL). The current EPL rate is 38%, it has applied at that rate since 1 November 2024, and under current law it runs until 31 March 2030, unless the Energy Security Investment Mechanism (ESIM) ends it earlier. For profits exposed to EPL, the simple headline stack is therefore often described as 78% = 30% RFCT + 10% SC + 38% EPL, but in modeling you should not tax a single base at 78% because the bases and relief rules are not identical. 
There is also a live future-regime uncertainty. At Budget 2025, the government announced a proposed successor regime called the Oil and Gas Price Mechanism (OGPM): a 35% revenue-based tax above threshold prices of $90/bbl oil and 90p/therm gas, intended to replace EPL when EPL ends or sooner if ESIM is triggered. But as of now, that is an announced future policy, not the current enacted regime; the government said it intends to legislate in Finance Bill 2026-27. 
A further nuance: the OBR March 2026 forecast assumes prices drop below the ESIM thresholds in Q2 and Q3 2027, so it assumes EPL stops raising tax from end-September 2027. That is a forecast assumption, not law. In a valuation model, treat it as a scenario, not as base law unless you deliberately choose to align with the OBR case. 
2) The model architecture you should build
At minimum, build these tabs or schedules:
1.	Production and pricing: oil, gas, NGL/condensate, tariffs, hedges if any. 
2.	Revenue: gross sales, tariff income, royalty only if doing very old historical modeling. Royalty was abolished from 1 January 2003, so most modern models ignore it. 
3.	Opex: split field opex, tariffs/transport, G&A, emissions/carbon, and financing. 
4.	Capex: split development capex, facilities, wells, tie-backs, de-bottlenecking, decarbonisation capex, decommissioning capex. 
5.	RFCT tax schedule. 
6.	SC tax schedule, including the SC Investment Allowance. 
7.	EPL schedule, with its own loss pool and current allowance rules. 
8.	Decommissioning / terminal loss / PRT refund schedule. 
9.	Tax payment timing schedule. 
10.	A separate regulatory economics view if you want to mirror NSTA submissions, because NSTA economics are not the same thing as commercial after-tax valuation. 
3) RFCT: how to think about it in the model
The ring fence treats UK upstream extraction and oil rights activities as a separate trade, so profits from the ring-fence trade are not meant to be reduced by losses from other activities or by excessive interest charges outside the intended upstream tax base. RFCT is charged at 30%. 
For modeling purposes, RFCT is your closest thing to the “main upstream tax base.” It will include normal ring-fence trading profits and also chargeable gains on ring-fence assets, although there are important special cases such as developed-area licence swaps and reinvestment relief conditions. PRT paid is deductible in computing ring-fence profits, which matters only for relevant legacy assets. 
For capex, most qualifying plant and machinery used in the ring-fence trade benefits from 100% first-year allowances, which is one reason UKCS models often show very fast tax relief on development capex. Where first-year treatment is not available, fallback writing-down allowances exist. 
4) Supplementary Charge: similar, but not the same base
The Supplementary Charge is 10% and is charged on adjusted ring-fence profits. The crucial modeling point is that financing costs are excluded from the SC base. Many simplified models miss this and mechanically copy the RFCT base into SC. 
SC also has a separate Investment Allowance (IA) regime. Under the basin-wide rules, qualifying expenditure generates IA equal to 62.5% of that expenditure, and the allowance reduces SC only, not RFCT. It is activated when the relevant field has production income. This matters a lot for long-lead projects and tie-backs. 
If your asset also earns tariff income from infrastructure access or related services, pay attention: tariff receipts can be relevant income for these purposes, and infrastructure-led UKCS assets can model differently from simple stand-alone producers. 
5) EPL: build it as a separate tax engine
Treat EPL as a standalone levy schedule, not just “another percentage on top.” Since 1 November 2024, the current rules are: 38% rate, end date 31 March 2030, investment allowance removed, and decarbonisation allowance reduced to 66%. RFCT and SC continue underneath it. 
The levy still allows 100% first-year allowances for qualifying capital expenditure, but the old EPL investment allowance is gone under the current post-November-2024 rules. 
Losses under EPL are also their own world. EPL losses cannot cross over into RFCT or SC. In general, EPL losses can be carried back 12 months, terminal levy losses can be carried back 3 years, carryforward is allowed while the ring-fence trade continues, and levy group relief is available between 75% group companies. 
The other major trap is decommissioning: decommissioning expenditure is not deductible for EPL, and because of that there is no DRD-style protection for EPL. If you deduct decomm across all three taxes, your terminal-year after-tax values will be materially wrong. 
6) Decommissioning, legacy PRT, and terminal relief
For RFCT and SC, decommissioning expenditure normally gets immediate 100% relief, and the UK regime has unusually important carryback mechanics for decommissioning and terminal losses. 
There are two layers you should model here:
•	Corporate tax carryback: pre-cessation decommissioning or abandonment losses can be carried back, and certain decommissioning / terminal losses have extended carryback provisions reaching back to 17 April 2002 for qualifying periods. 
•	Legacy PRT refunds: for fields that were approved before 16 March 1993, PRT is now at 0%, but losses can still be carried back against historic PRT payments, which is why PRT is still economically relevant in old-field decommissioning models. HMRC’s own published statistics continue to show PRT repayments driven by decommissioning. 
If you are working on a mature UKCS asset package, also check whether Decommissioning Relief Deeds (DRDs) are in place. Their purpose is to provide certainty over a minimum level of decommissioning tax relief based on the 2013 regime, which is important for security arrangements and transaction modeling. 
7) Pre-profit explorers and developers: RFES
If the company is pre-production or still in the exploration/development stage, look at Ring Fence Expenditure Supplement (RFES). RFES was designed to increase the value of unused ring-fence losses and expenditure for companies that have not yet reached taxable income. For accounting periods beginning on or after 1 January 2012, the RFES rate is 10%, and it can apply for up to 10 accounting periods. 
That can matter a lot in a farm-in or pre-FID valuation where you are comparing “tax value of sunk spend” across different development timing scenarios. 
8) Asset sales, related-party pricing, and market-value traps
If you are modeling infrastructure sharing, related-party marketing, or asset transactions, there are extra UKCS-specific traps.
For crude oil, LPG, and condensate, statutory market values may have to be used where disposals are not at arm’s length. For arm’s-length sales, you use actual sale proceeds; for non-arm’s-length transactions, statutory valuation rules can override the booked transfer price. 
On acquisitions and disposals, chargeable gains on ring-fence assets generally sit inside the ring fence and are subject to RFCT and SC, but there are specific reliefs and no-gain/no-loss style rules in some licence swap situations. If you are valuing a corporate deal rather than a simple field DCF, you should build a separate transaction-tax module rather than burying gains or losses in operating cash flow. 
9) Cash tax timing matters more than in many other jurisdictions
Do not stop at “P&L tax.” UKCS projects are often owned by large groups, and cash tax timing can move NPV meaningfully.
As a baseline, corporation tax is normally due 9 months and 1 day after the end of the accounting period. But large companies and very large companies pay by quarterly instalments, with the earlier instalment pattern applying sooner for very large groups. Since EPL is administered as corporation tax, its payment mechanics follow the CT framework. 
For a serious valuation, you should therefore calculate:
•	tax accrual by regime, 
•	cash payment profile by regime, 
•	carryback refunds timing, 
•	terminal-year decommissioning tax recoveries timing. 
10) NSTA economics are not the same as investor economics
If part of your goal is to mirror how UK projects are screened by the regulator, know that the NSTA Standard Economics Template (SET) is fundamentally a pre-tax UK welfare/economic view, not your commercial after-tax investor DCF. The NSTA asks operators to provide economics for field and incremental developments in SET form. 
NSTA’s published approach is to assess economic recovery using a pre-tax concept of value, with 10% real discounting for most costs and revenues, while carbon costs are brought in using UK government greenhouse-gas values and the HM Treasury social discount rate, not your own internal carbon price deck. 
So for professional-quality work, build two views:
•	a commercial after-tax DCF for investment decisions; and 
•	a regulatory / SET-style pre-tax economics case for NSTA-facing work. 
11) A practical modeling blueprint
A robust UKCS model usually works best if every revenue and cost line carries a few flags:
•	deductible for RFCT? 
•	deductible for SC? 
•	deductible for EPL? 
•	qualifies for 100% FYA? 
•	generates SC Investment Allowance? 
•	qualifies for EPL decarbonisation allowance? 
•	is it decommissioning? 
•	is it tariff-related? 
•	does it belong to a legacy PRT field? 
Then run the model in this order:
1.	Revenue and opex. 
2.	Capital allowances / qualifying capex treatment. 
3.	RFCT base and tax. 
4.	SC base, then apply SC IA. 
5.	EPL base, allowances, separate losses. 
6.	Decommissioning and terminal carryback / refund logic. 
7.	Cash tax timing. 
8.	Sensitivities on oil, gas, capex, opex, start-up delay, decommissioning cost, and a future-regime scenario for ESIM / OGPM. 
12) The biggest mistakes to avoid
•	Using a flat 78% rate on accounting profit instead of separate RFCT / SC / EPL bases. 
•	Deducting finance costs from SC. 
•	Deducting decommissioning from EPL. 
•	Forgetting legacy PRT refunds on old fields. 
•	Ignoring SC Investment Allowance. 
•	Ignoring quarterly instalment timing. 
•	Mixing up NSTA pre-tax economics with commercial after-tax valuation. 
•	Hard-coding post-2027 or post-2030 tax without separating current law from announced future policy. 
13) Best source pack to keep open while building
The most useful primary sources for this are:
•	HMRC’s Oil Taxation Manual and CT600 guidance for ring-fence and SC mechanics. 
•	HMRC’s published rates and allowances annexes for current rates and ESIM thresholds. 
•	HM Treasury / Budget 2025 materials on the proposed OGPM. 
•	HMRC’s Oil and gas tax statistics / receipts and repayments materials for PRT and decommissioning context. 
•	NSTA FDP / SET guidance and carbon valuation notes for regulator-style economics. 
This is enough to build a real model. The next best step is to lay out an actual Excel tab structure with formulas and line items for a UKCS E&P model, including the RFCT / SC / EPL schedules and decommissioning carryback logic.

