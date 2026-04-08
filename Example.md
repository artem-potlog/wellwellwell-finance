I’m structuring this around upstream-specific accounting, because for E&P the links between statements are driven by capex, DD&A, reserves, decommissioning, and the exploration policy choice.

Thought for 2m 23s

Below is a practical three-statement map for an upstream E&P company.

I’ll use these simplifying assumptions so the mechanics stay clean:

accounting is shown on a successful efforts-type basis for exploration examples
ignore income tax
ignore FX
use simple numbers
cash flow statement is discussed mainly in the usual modeling logic:
CFO = operating cash flow
CFI = investing cash flow
CFF = financing cash flow

Also, one key point:

The cash flow statement is not a separate accounting ledger.
It is a rearrangement of the income statement plus balance sheet movements to explain why cash on the balance sheet changed.

1) Overall overview: how IS, BS and CF are connected
A. What each statement is
Income Statement (IS)

Shows performance over a period:

revenue from oil/gas sales
royalties / production taxes
lease operating expense
transportation / processing
G&A
exploration expense
DD&A
impairment
interest
tax

It answers: Did the company make money this period?

Balance Sheet (BS)

Shows the company’s position at a point in time.

For E&P, the most important balance sheet lines are usually:

Assets

cash
accounts receivable
inventory (if any)
exploration & evaluation assets
oil & gas PP&E / development assets
accumulated DD&A / impairment allowance

Liabilities

accounts payable
accrued expenses
debt
asset retirement obligation / decommissioning provision
interest payable

Equity

share capital / APIC
retained earnings

It answers: What does the company own, owe, and what is left for shareholders right now?

Cash Flow Statement (CF)

Shows actual cash movement during the period, split into:

Operating

collections from production sales
payments to suppliers
LOE
royalties
G&A
interest (often here in models; under IFRS presentation can vary by policy)

Investing

seismic
exploration drilling
development drilling
facilities
acquisitions / disposals

Financing

debt drawdown / repayment
equity issuance
dividends

It answers: Where did cash come from and where did it go?

B. The core connection

The three statements are tied by a few fundamental bridges.

1. Net income flows into equity

At period-end:

Closing retained earnings = Opening retained earnings + Net income - Dividends

So the IS ultimately updates the equity section of the BS.

2. Cash flow explains the change in cash

On the BS:

Closing cash = Opening cash + CFO + CFI + CFF

So the CF statement explains exactly why the cash line on the BS moved.

3. Accrual accounting creates timing differences

This is the most important modeling idea.

Examples:

you can book revenue before cash is collected → creates A/R
you can book expense before cash is paid → creates A/P or accruals
you can spend cash on a well and not hit IS immediately → it goes to PP&E
later that PP&E is released to IS through DD&A
you can recognize non-cash expense (DD&A, impairment, accretion) with no immediate cash movement

So:

IS = economic performance
BS = where those uncollected/unpaid/capitalized items sit
CF = when cash actually moved
C. Why this matters especially for E&P

For an E&P company, three-statement logic is dominated by:

big capex before production
exploration accounting policy
DD&A driven by reserves / unit of production
impairment risk when prices/reserves fall
decommissioning obligations
debt-funded development cycles

This is why an E&P company can have situations like:

negative cash flow but low IS expense now because spend is capitalized
positive EBITDA but weak cash because receivables or capex absorb cash
large accounting loss with little current cash effect because of impairment
no P&L impact from debt draw, but big cash inflow on CF and bigger liabilities on BS
D. One very useful mental model

Every transaction first goes through journal entries.

Each journal entry has:

a debit
a credit

That double-entry then flows into the statements.

In practice:

if you debit an expense, IS goes down
if you credit revenue, IS goes up
if you debit an asset, BS asset goes up
if you credit a liability, BS liability goes up
later, IS closes into retained earnings
CF picks up only the cash leg of the story
2) Ten specific E&P examples with full double-entry detail
Example 1. Sale of produced oil on credit, then collection of cash

Assume:

oil sold for 100
inventory carrying value = 60
customer pays later
Step 1: recognize the sale

Dr Accounts Receivable 100
Cr Oil & Gas Revenue 100

What each side means
Debit A/R 100
BS asset increases
company now has a claim on the buyer
Credit Revenue 100
IS revenue increases
net income increases by 100 before other costs
at period-end that increases retained earnings on BS
Step 2: recognize the cost of inventory sold

Dr Cost of Sales 60
Cr Inventory 60

What each side means
Debit Cost of Sales 60
IS expense increases
net income decreases by 60
Credit Inventory 60
BS asset decreases
product has left the warehouse / tank and been sold
Step 3: collect cash from the customer

Dr Cash 100
Cr Accounts Receivable 100

What each side means
Debit Cash 100
BS cash increases
Credit A/R 100
BS receivable decreases
claim is settled
Net statement effect

IS

Revenue +100
Cost of Sales -60
Profit +40

BS

Cash +100
A/R ends at 0 after collection
Inventory -60
Retained earnings +40

CF

CFO +100 when cash is collected
E&P interpretation

This is the simplest production monetization loop:
produce → sell → recognize margin → collect cash

Example 2. Royalty / production tax accrual and later payment

Assume royalty or production tax for the period is 15.

Step 1: accrue royalty expense

Dr Royalty / Production Tax Expense 15
Cr Royalty Payable 15

What each side means
Debit royalty expense 15
IS expense increases
net income falls by 15
Credit royalty payable 15
BS liability increases
company owes the government / mineral owner
Step 2: pay the royalty

Dr Royalty Payable 15
Cr Cash 15

What each side means
Debit royalty payable 15
BS liability decreases
Credit cash 15
BS cash decreases
Net statement effect

IS

Expense -15

BS

Cash -15 after payment
payable returns to 0
retained earnings -15

CF

CFO -15
E&P interpretation

This is a classic upstream item.
Production may look profitable at revenue level, but royalties and production taxes are often one of the first cash drains below revenue.

Example 3. Lease operating expense (LOE) invoice and payment

Assume field operating services invoice = 20.

Step 1: book vendor invoice

Dr Lease Operating Expense 20
Cr Accounts Payable 20

What each side means
Debit LOE 20
IS expense increases
net income decreases
Credit A/P 20
BS liability increases
supplier has not yet been paid
Step 2: pay supplier

Dr Accounts Payable 20
Cr Cash 20

What each side means
Debit A/P 20
BS liability decreases
Credit Cash 20
BS asset decreases
Net statement effect

IS

Expense -20

BS

Cash -20 after payment
payable back to 0
retained earnings -20

CF

CFO -20
E&P interpretation

This is ordinary field opex: chemicals, lifting, maintenance, water handling, contractor support, etc.

Example 4. Drill and complete a development well

Assume development drilling and completion cost = 150.

Step 1: capitalize the well cost

Dr Oil & Gas PP&E (Development Asset) 150
Cr Accounts Payable 150

What each side means
Debit PP&E 150
BS long-lived asset increases
no immediate IS expense
cost is capitalized because it creates future economic benefit
Credit A/P 150
BS liability increases
contractor is owed money
Step 2: pay the contractor

Dr Accounts Payable 150
Cr Cash 150

What each side means
Debit A/P 150
liability decreases
Credit Cash 150
cash decreases
Net statement effect

IS

no immediate effect

BS

PP&E +150
Cash -150 after payment
no immediate retained earnings effect

CF

CFI -150
E&P interpretation

This is the key upstream modeling point:

Cash left the business now, but IS is not hit now.

Instead, the well cost sits on BS and will hit IS later through DD&A or impairment.

Example 5. DD&A on a producing field

Assume DD&A for the period = 30.

Step 1: record DD&A

Dr DD&A Expense 30
Cr Accumulated DD&A 30

What each side means
Debit DD&A expense 30
IS expense increases
net income decreases
Credit accumulated DD&A 30
contra-asset on BS increases
net book value of oil & gas assets decreases
Net statement effect

IS

Expense -30

BS

Net PP&E -30
retained earnings -30

CF

no current cash movement
under indirect CF logic, DD&A is added back in CFO, because it reduced net income but did not use cash now
E&P interpretation

This is how capitalized well cost from Example 4 gradually moves from BS to IS.

For upstream, DD&A is often linked to:

production volumes
reserve base
unit-of-production method

So reserves matter directly for accounting.

Example 6. Exploratory well: initially capitalized, later determined dry hole

Assume exploration well cost = 80.

Step 1: drill the exploratory well

Dr Exploration & Evaluation Asset / Exploratory Well 80
Cr Cash 80

What each side means
Debit E&E asset 80
BS asset increases
cost is parked on BS while technical evaluation is ongoing
Credit cash 80
cash decreases
Step 2: later conclude the well is dry / unsuccessful

Dr Exploration Expense (Dry Hole) 80
Cr Exploration & Evaluation Asset 80

What each side means
Debit exploration expense 80
IS expense increases
net income decreases
Credit E&E asset 80
BS asset decreases
capitalized cost is written off
Net statement effect

IS

Exploration expense -80 when dry hole is determined

BS

Cash -80
E&E asset returns to 0
retained earnings -80

CF

initial drilling cash outflow: CFI -80
later dry-hole expense: non-cash
E&P interpretation

This is one of the most important upstream accounting differences.

Under successful efforts, a failed exploration well eventually hits the IS as expense.
Cash is the same regardless of accounting policy; what changes is timing of P&L vs BS.

Example 7. Asset retirement obligation (ARO) / decommissioning provision

Assume present value of abandonment obligation at field development = 25.

Step 1: recognize initial ARO

Dr Oil & Gas PP&E 25
Cr ARO / Decommissioning Liability 25

What each side means
Debit PP&E 25
BS asset increases
abandonment cost is capitalized as part of field development cost
Credit ARO liability 25
BS liability increases
company recognizes future abandonment obligation
Step 2: recognize annual accretion on the liability

Assume accretion for the year = 2.

Dr Accretion Expense 2
Cr ARO Liability 2

What each side means
Debit accretion expense 2
IS expense increases
net income decreases
Credit ARO liability 2
BS liability increases
carrying amount grows as settlement date gets closer
Step 3: later settle the abandonment

Assume actual cash paid = 27.

Dr ARO Liability 27
Cr Cash 27

What each side means
Debit ARO liability 27
BS liability decreases / is settled
Credit cash 27
BS cash decreases
Net statement effect

IS

no P&L at initial recognition
accretion expense -2 over time

BS

PP&E +25 initially
ARO liability +25 initially, then +2 accretion, then -27 settlement
cash -27 when paid

CF

actual abandonment payment is a cash outflow
presentation can vary by policy, but operationally it is a real cash drain tied to field life cycle
E&P interpretation

This is very upstream-specific and economically important.
A mature field may have decent operating cash flow but still carry a large future abandonment burden.

Example 8. Reserve-based lending (RBL): draw and principal repayment

Assume:

company draws 200
later repays 50 principal
Step 1: draw the facility

Dr Cash 200
Cr Long-Term Debt 200

What each side means
Debit cash 200
BS cash increases
Credit debt 200
BS liability increases
Step 2: repay principal

Dr Long-Term Debt 50
Cr Cash 50

What each side means
Debit debt 50
BS liability decreases
Credit cash 50
BS asset decreases
Net statement effect

IS

no immediate IS effect from draw or principal repayment

BS

cash net +150
debt net +150

CF

draw: CFF +200
repayment: CFF -50
E&P interpretation

This is the purest financing example:

debt changes BS and CF
but does not hit IS at inception
only the interest hits IS

This is why a levered E&P can show strong cash inflow from financing even when operations are weak.

Example 9. Interest accrual and payment on debt

Assume interest expense for the period = 12.

Step 1: accrue interest

Dr Interest Expense 12
Cr Interest Payable 12

What each side means
Debit interest expense 12
IS expense increases
net income decreases
Credit interest payable 12
BS liability increases
cash not paid yet
Step 2: pay interest

Dr Interest Payable 12
Cr Cash 12

What each side means
Debit interest payable 12
liability decreases
Credit cash 12
cash decreases
Net statement effect

IS

Interest expense -12

BS

cash -12 after payment
interest payable back to 0
retained earnings -12

CF

cash payment is usually modeled in CFO
under IFRS, presentation policy can differ, but in most practical operating models it is tracked very visibly as a debt service cash cost
E&P interpretation

This is where financing starts affecting P&L.
The debt itself did not hit IS in Example 8, but its cost does hit IS here.

Example 10. Impairment of producing assets after price drop or reserve downgrade

Assume impairment = 90.

Step 1: recognize impairment

Dr Impairment Expense 90
Cr PP&E / Impairment Allowance 90

What each side means
Debit impairment expense 90
IS expense increases sharply
net income decreases
Credit PP&E or impairment allowance 90
BS asset carrying amount decreases
Net statement effect

IS

Expense -90

BS

net PP&E -90
retained earnings -90

CF

no immediate cash impact
under indirect CF logic, impairment is added back in CFO because it reduced accounting profit but did not use cash now
E&P interpretation

This is extremely common in upstream when:

prices fall
reserves are downgraded
costs rise
development plans are delayed

An E&P may report a big accounting loss even though no cash left the company at that moment.

3) What these 10 examples teach you

These examples show the core rules.

Rule 1: Revenue and expense do not equal cash
sale can create A/R before cash
opex can create A/P before payment
Rule 2: Capex hits cash first, profit later

Development drilling:

cash outflow now
BS asset now
IS expense later via DD&A or impairment

This is probably the single most important difference between an industrial cash model and a simple P&L view.

Rule 3: Non-cash expenses matter a lot in E&P

Examples:

DD&A
impairment
exploration write-off
accretion of ARO

These hit IS without immediate cash.

Rule 4: Financing changes BS and CF first, IS later
debt draw → BS + CF only
principal repayment → BS + CF only
interest → IS + CF
Rule 5: E&P accounting is heavily driven by life cycle

Typical pattern:

Acquire acreage / seismic → explore → appraise → develop → produce → decline → abandon

Each phase changes which statement takes the main hit.

4) A compact three-statement cheat sheet for E&P
When something usually hits IS first
revenue
LOE
royalties
G&A
exploration write-off
DD&A
impairment
interest
When something usually hits BS first
development well capex
facilities capex
exploratory cost before outcome is known
A/R, A/P, accruals
debt draw
ARO liability
When something hits CF only through timing
collection of receivables
payment of payables
capex payment
debt draw / repayment
abandonment spend
5) The single best way to think about three-statement modeling for E&P

Think in this order:

1. What is the business event?

Example: drilled a well, sold oil, drew debt, booked impairment.

2. What is the journal entry?

What gets debited and credited?

3. Does it hit:
IS now?
BS now?
cash now?
4. If it does not hit cash now, where is it parked?

Usually in:

A/R
A/P
PP&E
liability accrual
E&E asset

That is the whole system.

6) One sentence summary

For an E&P company:

The income statement shows value creation/destruction over time, the balance sheet stores the unfinished parts of that story, and the cash flow statement shows when the money actually moved.

If you want, I can turn this into a full three-statement E&P model map with a line-by-line bridge such as:

production → revenue
revenue → A/R / cash
capex → PP&E
PP&E → DD&A
exploration → E&E / expense
debt → interest / repayments
ARO → accretion / abandonment cash

and present it as a clean modeling template.

Do some more complicated examples with DTA and DTL and with ARO and accretion 

I’m going to do this in the way modelers usually need it: book entry, tax treatment, temporary difference, DTA/DTL entry, then the impact on IS, BS, and CF.

Thought for 2m 43s

Yes — let’s go one level deeper.

For E&P, deferred taxes become especially important because book accounting and tax accounting often diverge on:

development capex and depreciation/DD&A
impairment
abandonment / ARO
accretion
dry hole treatment
decommissioning relief timing

I’ll do this in a modeling-friendly way:

quick refresher on DTA / DTL
then 5 more complicated E&P examples
in each example:
business event
book entry
tax treatment
temporary difference
DTA/DTL entry
effect on IS, BS, CF

I will assume:

tax rate = 30% unless stated otherwise
ignore FX
ignore other minor taxes
assume a “normal corporate tax” framework, not PSC-specific quirks
for ARO, assume tax deduction happens only when abandonment cash is actually spent
for simplicity, I will ignore some standard-specific exceptions and focus on the mechanics a modeler needs
1) Refresher: what DTA and DTL really mean
Deferred Tax Liability (DTL)

A DTL usually means:

you paid less tax now than your book P&L suggests, so you’ll pay more later

Classic E&P example:

book DD&A = 100
tax depreciation = 300
taxable income is lower than book income
current tax is lower now
that tax saving is temporary
so a DTL is created
Deferred Tax Asset (DTA)

A DTA usually means:

you recognized expense in book now, but tax deduction comes later

Classic E&P examples:

impairment booked now, deductible only on disposal
abandonment liability booked now, deductible only when cash is spent
accrued expenses booked now, tax deductible only when paid
NOLs
The tax line on the income statement

Very important:

Income tax expense on IS = current tax expense ± deferred tax expense

Where:

current tax = based on taxable income under tax rules
deferred tax = adjustment for temporary timing differences between book and tax
2) Example 1 — DTL from accelerated tax depreciation on a producing well

This is one of the most common upstream deferred tax patterns.

Assume:

development well cost = 1,000
booked as PP&E
Year 1 book DD&A = 100
Year 1 tax depreciation = 300
pre-DD&A, pre-tax operating profit = 500
tax rate = 30%
Step 1. Capitalize the well
Journal entry

Dr Oil & Gas PP&E 1,000
Cr Cash 1,000

Meaning
debit PP&E: long-lived asset on BS goes up
credit cash: BS cash goes down
Statement effect
IS: no immediate effect
BS: PP&E +1,000; Cash -1,000
CF: CFI -1,000
Step 2. Record book DD&A
Journal entry

Dr DD&A Expense 100
Cr Accumulated DD&A 100

Meaning
debit DD&A expense: IS expense up
credit accumulated DD&A: contra-asset up; net PP&E down
Statement effect
IS: expense -100
BS: net PP&E -100; retained earnings later down
CF: no current cash effect
Step 3. Compute book profit and taxable income
Book
operating profit before DD&A = 500
less DD&A = 100
book pre-tax income = 400
Tax
operating profit before depreciation = 500
less tax depreciation = 300
taxable income = 200
Step 4. Record current tax

Current tax = 200 × 30% = 60

Journal entry

Dr Income Tax Expense — Current 60
Cr Income Tax Payable 60

Meaning
debit current tax expense: IS tax expense up
credit tax payable: BS liability up
Step 5. Record deferred tax liability

If book pre-tax income is 400, “normal” tax at 30% would be 120.

But current tax is only 60, because tax depreciation was faster than book DD&A.

Difference = 60, so create a DTL 60.

Journal entry

Dr Income Tax Expense — Deferred 60
Cr Deferred Tax Liability 60

Meaning
debit deferred tax expense: raises tax expense on IS
credit DTL: BS liability up

This says:
“we got a temporary tax advantage now, but owe it back later.”

Step 6. Pay current tax
Journal entry

Dr Income Tax Payable 60
Cr Cash 60

Meaning
payable down
cash down
Final statement effect
IS
operating profit before DD&A: 500
DD&A: -100
pre-tax income: 400
current tax expense: -60
deferred tax expense: -60
total tax expense: -120
net income: 280
BS
PP&E gross +1,000
accumulated DD&A +100
cash -1,060 total from capex and taxes
DTL +60
retained earnings +280
CF
CFI -1,000
CFO -60 for current tax paid
deferred tax creation is non-cash
Core logic

This example creates a DTL because:

tax deduction happened faster than book expense
tax paid today is lower than book tax expense
the company “borrowed from the tax authority” temporarily
3) Example 2 — DTA from impairment booked now but not tax-deductible yet

Very relevant for E&P when:

oil price falls
reserves are downgraded
development is delayed
asset carrying value is written down

Assume:

carrying value of producing asset = 600
book impairment = 200
tax law says impairment is not deductible until disposal / sale
operating profit before impairment and tax = 300
tax rate = 25% in this example
Step 1. Record impairment
Journal entry

Dr Impairment Expense 200
Cr PP&E / Impairment Allowance 200

Meaning
debit impairment expense: IS expense up
credit asset or allowance: BS asset carrying amount down
Statement effect
IS: impairment expense -200
BS: net PP&E -200
CF: no current cash effect
Step 2. Compute book and tax profit
Book
operating profit before impairment = 300
less impairment = 200
book pre-tax income = 100
Tax
impairment ignored for tax now
taxable income remains 300

Current tax = 300 × 25% = 75

Step 3. Record current tax
Journal entry

Dr Income Tax Expense — Current 75
Cr Income Tax Payable 75

Step 4. Record deferred tax asset

If book pre-tax income is 100, book tax at 25% would be 25.

But current tax is 75.

That means the company paid 50 more tax now than book economics imply, because tax law did not allow the deduction yet.

So recognize DTA = 50.

Journal entry

Dr Deferred Tax Asset 50
Cr Income Tax Benefit — Deferred 50

Meaning
debit DTA: BS asset up
credit deferred tax benefit: reduces tax expense on IS
Step 5. Pay the tax
Journal entry

Dr Income Tax Payable 75
Cr Cash 75

Final statement effect
IS
operating profit before impairment: 300
impairment: -200
pre-tax income: 100
current tax expense: -75
deferred tax benefit: +50
total tax expense: -25
net income: 75
BS
PP&E -200
DTA +50
cash -75 from tax payment
retained earnings +75
CF
CFO -75 for tax paid
impairment and deferred tax are non-cash
Core logic

This example creates a DTA because:

book took the pain now
tax deduction comes later
company paid “too much” tax today relative to book
that future tax benefit is stored as an asset
4) Example 3 — Initial recognition of ARO: asset + liability + DTL + DTA

Now let’s do the more interesting upstream case.

Assume:

a new field is developed
present value of future abandonment obligation = 100
tax deduction will be available only when abandonment is actually paid
tax rate = 30%

When ARO is recognized, book accounting usually does two things:

recognizes a liability
capitalizes the same amount into the related asset

So you get both:

an ARO liability
an ARO asset embedded in PP&E

This is exactly why ARO often creates both DTA and DTL.

Step 1. Recognize the ARO itself
Journal entry

Dr Oil & Gas PP&E 100
Cr ARO Liability 100

Meaning
debit PP&E: asset increases
credit ARO liability: future abandonment obligation recognized
Statement effect
IS: no immediate effect
BS: PP&E +100, ARO liability +100
CF: no immediate cash effect
Step 2. Tax analysis of the asset side

The ARO asset is on book at 100.

Assume tax law gives no tax basis yet for this amount, because deduction only comes when abandonment cash is spent.

So:

carrying amount of asset = 100
tax base of asset = 0
taxable temporary difference = 100
DTL = 30
Journal entry

Dr Income Tax Expense — Deferred 30
Cr Deferred Tax Liability 30

Meaning
this asset is on book now, but tax relief comes later
so from the asset side, you get a DTL
Step 3. Tax analysis of the liability side

The ARO liability is on book at 100.

When the company eventually settles it, tax law should allow deduction for that spend.

So the liability creates a future deductible amount.

That usually means:

carrying amount of liability = 100
tax base = 0
deductible temporary difference = 100
DTA = 30
Journal entry

Dr Deferred Tax Asset 30
Cr Income Tax Benefit — Deferred 30

Meaning
future tax deduction is expected when the obligation is settled
so from the liability side, you get a DTA
Net effect at inception
IS
deferred tax expense 30
deferred tax benefit 30
net P&L effect = 0
BS
PP&E +100
ARO liability +100
DTL +30
DTA +30
CF
no cash effect
Core logic

At ARO inception:

the asset side tends to create a DTL
the liability side tends to create a DTA

They often start equal.

5) Example 4 — Year 1 after ARO recognition: DD&A on ARO asset + accretion on liability + current tax + deferred tax movements

This is the full moving-parts example.

Continuing from Example 3, assume in Year 1:

ARO asset opening carrying amount = 100
ARO liability opening carrying amount = 100
DD&A on ARO asset = 20
accretion on ARO liability = 10
operating profit before these two items and before tax = 200
tax law still allows no deduction yet for either DD&A on the ARO asset or accretion
tax rate = 30%
Step 1. Record DD&A on the ARO asset
Journal entry

Dr DD&A Expense 20
Cr Accumulated DD&A 20

Meaning
debit DD&A expense: IS expense up
credit accumulated DD&A: net carrying amount of ARO asset falls from 100 to 80
Step 2. Record accretion on the ARO liability
Journal entry

Dr Accretion Expense 10
Cr ARO Liability 10

Meaning
debit accretion expense: IS expense up
credit ARO liability: liability grows from 100 to 110

This reflects unwinding of discount over time.

Step 3. Compute book and tax profit
Book
operating profit before ARO-related charges = 200
DD&A = -20
accretion = -10
book pre-tax income = 170
Tax

Assume neither item is deductible yet.

So taxable income remains 200.

Current tax = 200 × 30% = 60

Step 4. Record current tax
Journal entry

Dr Income Tax Expense — Current 60
Cr Income Tax Payable 60

Step 5. Re-measure the DTL on the ARO asset

Opening ARO asset carrying amount = 100
After DD&A = 80

Tax base still assumed = 0

So DTL should now be:

80 × 30% = 24

But opening DTL was 30.

So DTL must decrease by 6.

Journal entry

Dr Deferred Tax Liability 6
Cr Income Tax Benefit — Deferred 6

Meaning
DTL release creates deferred tax benefit
as the asset gets depreciated for book, the taxable temporary difference shrinks
Step 6. Re-measure the DTA on the ARO liability

Opening liability = 100
After accretion = 110

Tax base still assumed = 0

So DTA should now be:

110 × 30% = 33

Opening DTA was 30.

So DTA must increase by 3.

Journal entry

Dr Deferred Tax Asset 3
Cr Income Tax Benefit — Deferred 3

Meaning
future deductible amount got larger because the liability got larger
therefore DTA increases
Step 7. Optional: pay current tax
Journal entry

Dr Income Tax Payable 60
Cr Cash 60

Final statement effect
IS

Pre-tax:

operating profit = 200
DD&A = -20
accretion = -10
pre-tax income = 170

Tax:

current tax expense = -60
deferred tax benefit from DTL release = +6
deferred tax benefit from DTA increase = +3
total tax expense = -51

Net income:

170 - 51 = 119
BS
ARO asset net carrying amount falls from 100 to 80
ARO liability rises from 100 to 110
DTL falls from 30 to 24
DTA rises from 30 to 33
cash falls by 60 if tax is paid
retained earnings rise by 119
CF
current tax paid: CFO -60
DD&A: non-cash
accretion: non-cash
deferred tax movements: non-cash
Core logic

This is the most important ARO/deferred tax pattern:

DD&A on ARO asset gradually releases the DTL
accretion on ARO liability gradually increases the DTA
neither one necessarily affects current tax cash until actual abandonment spend occurs
6) Example 5 — Final abandonment cash payment and reversal of ARO-related DTA

Now assume several years later:

ARO liability carrying amount before settlement = 110
related DTA = 33
the ARO asset is already fully depreciated, so related DTL is already zero
actual abandonment cash paid = 115
the extra 5 is recognized as loss on settlement
tax deduction is allowed when cash is spent
operating profit before settlement and tax = 200
tax rate = 30%
Step 1. Settle the ARO
Journal entry

Dr ARO Liability 110
Dr Loss on ARO Settlement 5
Cr Cash 115

Meaning
debit liability 110: removes booked obligation
debit loss 5: actual spend exceeded carrying amount
credit cash 115: cash paid to plug and abandon
Step 2. Compute book and tax profit
Book
operating profit before settlement = 200
loss on ARO settlement = -5
book pre-tax income = 195
Tax

Tax law allows full deduction of actual spend 115 now.

So taxable income = 200 - 115 = 85

Current tax = 85 × 30% = 25.5

Step 3. Record current tax
Journal entry

Dr Income Tax Expense — Current 25.5
Cr Income Tax Payable 25.5

Step 4. Reverse the DTA on the liability

Before settlement:

liability-related DTA = 33

After settlement:

liability is gone
future deductible amount is gone
so DTA must go to zero
Journal entry

Dr Income Tax Expense — Deferred 33
Cr Deferred Tax Asset 33

Meaning
the future tax benefit is no longer “future” — it has now been used through the current tax deduction
so the DTA reverses
Step 5. Pay current tax
Journal entry

Dr Income Tax Payable 25.5
Cr Cash 25.5

Final statement effect
IS

Pre-tax:

operating profit = 200
settlement loss = -5
pre-tax income = 195

Tax:

current tax expense = -25.5
deferred tax expense = -33
total tax expense = -58.5

Net income:

195 - 58.5 = 136.5
BS
ARO liability goes to 0
DTA goes to 0
cash down by 115 settlement plus 25.5 tax if paid
retained earnings rise by 136.5
CF
abandonment cash payment -115
tax paid -25.5
DTA reversal is non-cash
Core logic

At settlement:

current tax becomes low because deduction finally arrives
the DTA that had been sitting on the BS gets reversed
the future tax benefit becomes a current tax benefit
7) One extra combined example — accrued abandonment work before cash payment

This is slightly different from classic discounted ARO accounting, but useful because it behaves like many “book now, tax later” liabilities.

Assume:

environmental remediation expense accrued = 40
not yet tax deductible until paid
tax rate = 30%
Step 1. Accrue the expense
Journal entry

Dr Abandonment / Remediation Expense 40
Cr Accrued Liability 40

Meaning
expense hits IS now
liability sits on BS
no cash yet
Step 2. Record DTA

Because tax deduction comes only when cash is paid:

deductible temporary difference = 40
DTA = 12
Journal entry

Dr Deferred Tax Asset 12
Cr Income Tax Benefit — Deferred 12

Step 3. Pay the contractor later
Journal entry

Dr Accrued Liability 40
Cr Cash 40

Now the tax deduction is claimed, so DTA reverses.

Journal entry

Dr Income Tax Expense — Deferred 12
Cr Deferred Tax Asset 12

Core logic

This is the “liability-side DTA” intuition in its simplest form.

8) What to remember in E&P specifically
A. DTL usually comes from assets

Common upstream causes:

tax depreciation faster than book DD&A
tax deductions for IDC / development spend faster than book expense
ARO asset recognized on book before tax deduction

That usually means:
current tax < book tax now
→ DTL

B. DTA usually comes from liabilities or book-only losses

Common upstream causes:

impairment not yet deductible
ARO liability deductible only when settled
accrued abandonment or remediation expense deductible on payment
booked losses or NOLs

That usually means:
current tax > book tax now
or
future tax deduction expected
→ DTA

C. ARO is tricky because it often creates both at once

At inception:

capitalized ARO asset → tends toward DTL
ARO liability → tends toward DTA

Then over time:

DD&A on the ARO asset → DTL releases
accretion on the ARO liability → DTA grows
final cash settlement → DTA reverses via current deduction
D. Deferred taxes are non-cash

This is crucial for modeling.

A DTA/DTL entry:

changes tax expense on IS
changes BS
does not move cash directly

Cash taxes are driven by:

current tax payable
and when that payable is actually paid
9) The clean modeling formulas
Income statement

Total tax expense = Current tax expense + Deferred tax expense - Deferred tax benefit

or more simply:

Total tax expense = Current tax ± movement in DTA/DTL

Balance sheet
DTA sits in assets
DTL sits in liabilities
retained earnings absorb after-tax earnings
Cash flow

Under indirect method:

CFO starts from net income
then adjust for:

non-cash DD&A
non-cash impairment
non-cash accretion
movement in working capital
deferred tax movements do not create current cash

Cash taxes paid are tied to:

current tax payable settlement
10) The shortest possible intuition

For E&P:

DTL = tax relief came earlier than book expense
DTA = book expense came earlier than tax relief
ARO often gives both:
asset side = DTL
liability side = DTA
accretion usually increases the liability-side DTA
DD&A on the ARO asset usually releases the asset-side DTL

If you want, next I can build you a single integrated E&P mini-model for one field over 3 years that shows:

development capex
production revenue
DD&A
ARO inception
accretion
impairment
current tax
DTA/DTL roll-forward
and all 3 statements side by side.
Show me also two cases: Full cost and Successful efforts dry hole across the statements
Thought for 23s

Yes — this is one of the central accounting differences in E&P.

The most important takeaway first:

Full Cost vs Successful Efforts does not change cash.
It changes:

when the dry hole hits the income statement
whether the cost stays on the balance sheet
how the future DD&A / depletion profile looks
when impairment / ceiling-test pain may appear
1) Core difference in one sentence
Successful Efforts (SE)

A dry hole is expensed once it is determined unsuccessful.

Full Cost (FC)

A dry hole stays capitalized inside the country / cost-center pool and is expensed later through depletion or ceiling-test impairment.

2) The clean intuition across the 3 statements

Suppose an E&P company spends 100 drilling an exploratory well, and the well turns out dry.

Under Successful Efforts
IS: usually takes the loss now
BS: asset disappears
CF: cash outflow happened when drilled
Under Full Cost
IS: no immediate dry-hole expense
BS: asset remains in the full-cost pool
CF: same cash outflow happened when drilled

So:

SE = faster P&L pain
FC = later P&L pain
3) Assumptions for the examples

To keep it clean, assume:

dry hole drilling cost = 100
tax ignored
cash paid immediately
no working capital complications
in the FC case, the company already has other successful properties in the same cost center, so the dry-hole cost remains in the pool
later, under FC, assume 20 of that pooled cost is depleted in the next period
CASE 1 — Successful Efforts dry hole across the statements
A. Step 1 — drill the exploratory well

At the moment of drilling, even under SE, the company usually capitalizes the well while evaluation is ongoing.

Journal entry

Dr Exploratory Well / E&E Asset 100
Cr Cash 100

Double-entry meaning
Debit exploratory well asset 100
BS asset increases
this says: “we have incurred a cost that may still have future value”
Credit cash 100
BS cash decreases
real money left the company
Statement impact immediately after drilling
IS
no immediate expense yet
BS
Cash -100
E&E / exploratory asset +100
CF
CFI -100
B. Step 2 — later determine the well is dry

Now geological / commercial evaluation shows there is no proved commercial reserve base or no future economic benefit.

Journal entry

Dr Exploration Expense / Dry Hole Expense 100
Cr Exploratory Well / E&E Asset 100

Double-entry meaning
Debit exploration expense 100
IS expense increases
pre-tax income decreases by 100
retained earnings will decrease by 100 at period close
Credit exploratory asset 100
BS asset decreases
the previously capitalized cost is removed
Statement impact when declared dry
IS
Exploration expense -100
Net income -100 lower
BS
E&E asset goes from 100 to 0
Retained earnings -100
Cash already left earlier, so no new cash effect here
CF
no new cash movement now
under indirect CFO, this dry-hole write-off is non-cash at the moment of expense recognition, because the cash already went out when drilled
C. Successful Efforts — full period view
Income Statement
exploration expense = 100
EBITDA / EBIT / net income are lower now
Balance Sheet end of period
cash = -100
exploratory asset = 0
retained earnings = -100
Cash Flow Statement
CFI -100
no dry-hole cash impact in CFO at the write-off date
D. What this means economically

Under SE, management and investors see failure faster.

That is why SE often gives:

more volatile earnings
lower near-term profit when exploration is active
a “cleaner” separation between successful and unsuccessful exploration
CASE 2 — Full Cost dry hole across the statements

Now same operational fact:

company drills a well
cost = 100
well is dry

But under FC, this dry hole is not individually expensed immediately.
Instead, it stays in the full cost pool.

A. Step 1 — drill the exploratory well / add to the cost pool
Journal entry

Dr Full Cost Pool / Oil & Gas Properties 100
Cr Cash 100

Double-entry meaning
Debit full cost pool 100
BS asset increases
all acquisition, exploration, and development costs in the cost center are accumulated
Credit cash 100
BS cash decreases
Statement impact immediately
IS
no expense
BS
Cash -100
Oil & gas properties / FC pool +100
CF
CFI -100
B. Step 2 — determine the well is dry

Here is the critical difference:

Under FC, the company generally does not write off this specific dry hole directly to IS.

Journal entry

No immediate dry-hole expense entry

The asset remains in the pool.

Statement impact
IS
no direct dry-hole expense now
BS
full-cost pool remains +100
CF
no new cash movement
C. Step 3 — later recognize depletion from the pooled cost

Suppose in the next period, because the company has production from other successful wells in the same cost center, 20 of the pool is depleted.

Journal entry

Dr DD&A / Depletion Expense 20
Cr Accumulated DD&A 20

Double-entry meaning
Debit DD&A expense 20
IS expense increases
net income decreases by 20
Credit accumulated DD&A 20
BS contra-asset increases
net PP&E decreases by 20
Statement impact
IS
DD&A expense -20
BS
net FC pool carrying amount falls from 100 to 80
retained earnings down 20
CF
no current cash effect
under indirect CFO, DD&A is added back because non-cash
D. Full Cost — full period 1 and later-period view
Period 1 (when well is drilled and found dry)
Income Statement
no dry-hole expense
Balance Sheet end of period
cash = -100
FC pool asset = +100
equity unchanged from this event alone
Cash Flow Statement
CFI -100
Later period (through depletion)
Income Statement
DD&A gradually recognizes the cost, e.g. -20
Balance Sheet
net asset declines from 100 to 80
Cash Flow Statement
DD&A is non-cash
4) Side-by-side comparison
A. At the moment the well is determined dry
Successful Efforts

Entry

Dr Dry Hole Expense 100
Cr Exploratory Asset 100
Full Cost

Entry

no immediate expense entry
Statement effect at that point
Item	Successful Efforts	Full Cost
IS expense now	100	0
BS asset remaining	0	100
Cash	same	same
CF impact at this point	none	none
B. Over the life of the asset pool
Successful Efforts
dry hole hit IS immediately
nothing left from that well to deplete later
Full Cost
dry hole stays capitalized
cost is recognized later via depletion or ceiling-test write-down
5) Full journal flow side by side
Successful Efforts
Step 1 — drill

Dr Exploratory Asset 100
Cr Cash 100

Step 2 — determine dry

Dr Dry Hole Expense 100
Cr Exploratory Asset 100

Final result
IS: expense 100 now
BS: cash down 100, no asset left
CF: CFI -100
Full Cost
Step 1 — drill

Dr Full Cost Pool 100
Cr Cash 100

Step 2 — determine dry

No immediate entry

Step 3 — later deplete part of pool

Dr DD&A Expense 20
Cr Accumulated DD&A 20

Final result at end of first period
IS: no dry-hole expense yet
BS: cash down 100, asset still 100
CF: CFI -100
Later result
IS: cost recognized gradually through DD&A
BS: asset declines gradually
6) How the two methods affect the statements in practice
Income Statement
Successful Efforts
lower earnings now
higher volatility
exploration failures visible immediately
Full Cost
smoother earnings early on
less immediate exploration expense
cost pushed into future DD&A / impairment
Balance Sheet
Successful Efforts
smaller asset base after dry hole
lower capital employed
Full Cost
larger asset base
more costs remain capitalized
risk of later ceiling-test hit
Cash Flow Statement
Both methods

Cash is identical:

CFI -100 when drilled

That is why you should never confuse:

accounting profit
with
cash burn
7) Important FC point: ceiling test

Under FC, a dry hole may avoid immediate expense, but that does not mean the cost disappears forever.

If the capitalized pool becomes too high relative to:

PV of reserves
standardized measure / ceiling value
commodity prices
tax effects
abandonment costs

then the company may have to book a ceiling-test impairment.

That would look like:

Journal entry

Dr Impairment Expense X
Cr Oil & Gas Properties / Valuation Allowance X

So under FC, pain can come later as a larger write-down instead of a specific dry-hole expense now.

8) Mini two-period numeric comparison

Let’s make it even clearer.

Assume:

dry hole cost = 100 in Year 1
under FC, 20 is depleted in Year 2
no tax
Year 1
Successful Efforts

IS

exploration expense = 100
net income lower by 100

BS end-Year 1

cash -100
no asset from this well
retained earnings -100

CF

CFI -100
Full Cost

IS

no expense

BS end-Year 1

cash -100
FC asset +100
retained earnings unchanged

CF

CFI -100
Year 2
Successful Efforts
nothing left from that dry hole
no further expense from it
Full Cost

IS

DD&A expense = 20

BS

net asset falls to 80
retained earnings lower by 20

CF

no cash effect from DD&A
9) Best modeling intuition

When you compare E&P companies, ask:

Under Successful Efforts:

“Which exploration costs were written off immediately?”

Under Full Cost:

“How much unsuccessful exploration is still hidden inside the pool and will emerge later via DD&A or ceiling test?”

That is one of the main reasons EV/EBITDA, net income, book value, and asset intensity can differ between otherwise similar operators.

10) Short bottom line
Successful Efforts dry hole
capitalize while evaluating
once confirmed dry: expense immediately
BS asset removed
cash unchanged versus FC
Full Cost dry hole
capitalize into pool
no immediate dry-hole expense
cost remains on BS
later hits IS through depletion or ceiling-test impairment

If you want, I can next do a single side-by-side 3-statement mini model for:

Year 1 drilling dry hole
Year 2 successful discovery elsewhere in same basin
Year 2 production and DD&A
showing exactly how SE vs FC diverge in EBITDA, EBIT, assets, and equity.
What does it mean
under indirect CFO, this dry-hole write-off is non-cash at the moment of expense recognition, because the cash already went out when drilled
Thought for a couple of seconds

It means this:

When the company recognized the dry-hole expense on the income statement, it did not pay cash at that same moment.

The cash had already been paid earlier, when the well was drilled.

So in the indirect cash flow statement, you:

start with net income
net income already includes the dry-hole expense
but that expense is non-cash in this period
so you add it back in CFO
The timeline
Period 1: drilling happens

Journal entry:

Dr Exploratory Asset 100
Cr Cash 100

What happened:

cash went out now
no expense yet
asset was created on BS

So in Period 1:

CFI = -100
IS = no dry-hole expense yet
Period 2: well declared dry

Journal entry:

Dr Dry Hole Expense 100
Cr Exploratory Asset 100

What happened:

IS gets expense now
asset is removed now
but no cash moves now

So in Period 2:

net income is lower by 100
but cash is not lower by 100 in Period 2

That is why, under the indirect method, CFO adds it back.

Why add it back?

Because indirect CFO starts from net income, not from cash receipts/payments.

Suppose in Period 2:

net income = -100, only because of dry-hole expense
no other items

If you stopped there, you would incorrectly think operations consumed 100 cash in Period 2.

But they did not.
The cash left in Period 1.

So CFO reconciliation is:

Net income: -100
Add back dry-hole write-off: +100
CFO impact: 0
Very simple intuition

The dry-hole expense in Period 2 is just an accounting release of an old asset into expense.

It is not a new payment.

So:

expense? yes
cash now? no
therefore non-cash in the period of write-off
Compare the two entries
1. Cash event

Dr Exploratory Asset 100
Cr Cash 100

This is when money actually leaves.

2. Non-cash expense event

Dr Dry Hole Expense 100
Cr Exploratory Asset 100

This is only:

moving value from BS to IS
no cash involved
On the cash flow statement
Period 1
CFI -100
Period 2

Indirect CFO:

start with net income lowered by dry-hole expense
add back dry-hole expense +100
so no CFO cash impact from the write-off itself
A helpful rule

Whenever an expense is recorded by:

debiting expense
crediting an asset, not cash

then that expense is usually non-cash at that moment.

Examples:

DD&A
impairment
dry-hole write-off after prior capitalization
One-line summary

It means: the P&L takes the loss now, but the cash left earlier, so in indirect CFO you reverse that expense out of current-period operating cash flow.

What if the company is doing successful efforts but also shows In investing activities the line: Development costs, capitalized exploration costs and dry hole expense

Thought for 1m 8s

It is not a contradiction.

In a successful efforts company, you can absolutely see:

Operating activities: add-back of dry hole expense
Investing activities: cash outflow line that includes dry hole expense

because those two lines are talking about different things.

What each line means
In CFO: “Dry hole expense”

This is an income statement expense that reduced net income.

Under the indirect method, CFO starts from net income, so if dry hole expense reduced NI, the company may add it back to CFO to remove that non-operating/non-current-period cash effect from operating cash flow.

This add-back means:

“Yes, we recognized expense in earnings, but that is not the operating cash outflow of this reconciliation step.”

In CFI: “Development costs, capitalized exploration costs and dry hole expense”

This is about the actual cash spent on drilling / exploration / development activities.

So here “dry hole expense” usually means:

cash spent on exploratory wells that turned out dry, or exploration spending associated with dry holes.

That cash outflow belongs in investing.

Why both can appear at once

Because in successful efforts, a dry hole often goes through two stages:

Stage 1: money is spent

Dr Exploratory well / E&E asset 100
Cr Cash 100

This is the cash event.

BS: cash down, asset up
CF: CFI -100
Stage 2: later, the well is declared dry

Dr Dry hole expense 100
Cr Exploratory well / E&E asset 100

This is the expense recognition event.

IS: expense up
BS: asset removed
no cash now

So on the cash flow statement:

the cash spend is shown in investing
the expense, because it reduced NI but did not use cash at that moment, is added back in CFO
Simple numerical example

Suppose in one year the company drills a dry exploratory well for 100, and determines it is dry in the same year.

Journal entries
1. Spend the cash

Dr Exploratory Asset 100
Cr Cash 100

2. Write it off

Dr Dry Hole Expense 100
Cr Exploratory Asset 100

Income statement
Dry hole expense = 100
Net income is lower by 100
Cash flow statement
CFO, indirect method

Start with net income, which already includes -100 dry hole expense.

Then add back:

Dry hole expense +100

So CFO is not dragged down by that accounting write-off.

CFI
exploratory/drilling cash spend = -100

Net cash change from this item = -100, which is correct.

Why this is actually necessary

If they did not add back dry hole expense in CFO, and also showed the drilling cash in CFI, the same dry hole would effectively hurt cash flow twice:

once through lower net income in CFO
once again through investing cash outflow

That would be wrong.

So the add-back in CFO is there to make sure the cash outflow is shown once, in the right section.

The subtle point

Do not assume the CFO add-back and the CFI dry-hole component are always a perfect one-for-one match in the same year.

There are two possibilities:

Case A — drilled and declared dry in the same year

Then:

CFO add-back this year
CFI outflow this year
Case B — drilled in Year 1, declared dry in Year 2

Then:

Year 1: CFI outflow
Year 2: dry hole expense on IS and add-back in CFO
no new cash outflow in Year 2 from that write-off

So the two lines are related conceptually, but not always perfectly tied by period.

Applied to your screenshot

Your screenshot shows:

in Operating activities: Dry hole expense 44
in Investing activities: Development costs, capitalized exploration costs and dry hole expense (3,190)

Interpretation:

44 = accounting expense recognized in earnings this year
(3,190) = total cash spent this year on development, capitalized exploration, and dry-hole-related drilling/exploration cash outlays

So this is fully consistent with successful efforts.

Short version

The line in investing does not mean the company is using full cost.

It means:

successful efforts determines when the dry hole hits earnings
the cash spent to drill it is still shown in investing cash flows

So:

IS/BS treatment = successful efforts
cash classification = investing outflow for exploration/development spend

If you want, I can draw this as a 3-column bridge: journal entries → IS/BS → CFO/CFI, using the exact dry-hole example from the screenshot.

Step 2: recognize annual accretion on the liability

Assume accretion for the year = 2.

Dr Accretion Expense 2
Cr ARO Liability 2

What each side means
Debit accretion expense 2
IS expense increases

At this step of ARO, how does the balance balances?
net income decreases
Credit ARO liability 2
BS liability increases
carrying amount grows as settlement date gets closer
Thought for 10s

It balances because the other side is equity, through current-period earnings / retained earnings.

That is the key idea.

The entry

Dr Accretion Expense 2
Cr ARO Liability 2

At first glance you may think:

liability goes up by 2
but where is the offset on the balance sheet?

The offset is:

expense reduces net income
lower net income reduces retained earnings / equity

So after the period is closed, the BS effect is:

ARO liability +2
retained earnings -2

Net effect: balance sheet still balances.

Why this works
Income statement side

Debit Accretion Expense 2

expense goes up
pre-tax income goes down by 2
net income goes down by 2
Balance sheet side

Credit ARO Liability 2

liability goes up by 2

Then, because net income is lower by 2:

equity goes down by 2

So:

Liabilities +2
Equity -2

Total RHS net change = 0?
Not quite the right way to think.

Better to think in full:

Before closing, the debit sits in a temporary expense account.
After closing, that expense flows into retained earnings.

So the full balance is:

Assets = Liabilities + Equity

with:

no asset change
liability +2
equity -2

That looks like RHS unchanged overall? No — because equity is reduced by 2 while liability increased by 2, so total RHS is unchanged. Exactly.

The cleanest way to see it

Use the expanded accounting equation:

Assets = Liabilities + Equity + Revenues - Expenses

Now apply the entry:

Liability +2
Expense +2

Equation becomes:

left side unchanged
right side: liability up 2, but expenses also up 2, and expenses are subtracted

So:
+2 - 2 = 0

Balanced.

Mini numeric example

Assume before accretion:

Balance sheet
Assets = 100
Liabilities = 40
Equity = 60

Balanced:
100 = 40 + 60

Now book accretion:

Dr Accretion Expense 2
Cr ARO Liability 2

Immediately:

ARO liability becomes 42
Accretion expense on IS = 2

If this is the only P&L item for the period, then:

net income = -2
retained earnings / equity become 58

So end-of-period BS is:

Assets = 100
Liabilities = 42
Equity = 58

Balanced:
100 = 42 + 58

Another important point

This entry does not use cash.

So accretion is:

a real expense on the IS
a real increase in liability on the BS
but non-cash on CF

Under indirect CFO, you usually add back the accretion expense because it reduced net income without reducing current-period cash.

Intuition in plain English

Accretion means:

“The future abandonment obligation is getting closer in time, so its present value must grow.”

That growth is recognized as:

expense on the IS
bigger liability on the BS

And the balancing item is:

lower profits
therefore lower equity
One-line answer

At the accretion step, the entry balances because the credit increases the ARO liability, and the debit reduces current earnings, which reduces equity by the same amount.

With ARO can't we just Dr Asset with FV? 
Thought for 8s

Yes — at initial recognition, broadly that is exactly the idea, except one important correction:

It is usually:

Dr Asset
Cr ARO Liability

but the amount is typically the present value of the future abandonment obligation, not the future value.

At inception

Suppose:

expected abandonment cash in 10 years = 100
present value today = 40

Then at initial recognition:

Dr Oil & Gas Asset 40
Cr ARO Liability 40

This means:

the field/well/facility asset includes the unavoidable retirement cost
the company also recognizes the obligation to settle it later

So yes: at day 1, you do capitalize the ARO into the asset.

But after that, no — you do not keep debiting the asset

After initial recognition, two different mechanics start:

1. The asset is depreciated / depleted

Because the capitalized ARO amount is part of the long-lived asset.

Example:

Dr DD&A
Cr Accumulated DD&A

2. The liability is accreted

Because the present value of the obligation grows as time passes and discount unwinds.

Example:

Dr Accretion Expense
Cr ARO Liability

So the later annual increase in the ARO is not normally:

Dr Asset
Cr ARO Liability

It is:

Dr Expense
Cr Liability

Why not debit the asset again every year?

Because accretion is not creating a new productive asset.

It is just saying:

“We are one year closer to paying the abandonment cash, so the discounted liability must grow.”

That growth comes from passage of time, not from:

new capex
better facilities
added reserves
a new economic benefit

So it belongs in expense, not in asset.

The clean intuition
Initial entry

You capitalize the retirement cost because it is part of what it takes to put the asset into service.

So:

asset up
liability up
Later accretion

No new asset is being built.
Only the obligation is getting closer.

So:

expense up
liability up
Small numeric example

Expected abandonment cash in 3 years = 133.1
Discount rate = 10%
Present value today = 100

Day 1

Dr PP&E 100
Cr ARO Liability 100

End of Year 1 accretion

Liability grows by 10:

Dr Accretion Expense 10
Cr ARO Liability 10

Liability now = 110

End of Year 2 accretion

Dr Accretion Expense 11
Cr ARO Liability 11

Liability now = 121

End of Year 3 accretion

Dr Accretion Expense 12.1
Cr ARO Liability 12.1

Liability now = 133.1

Then when you actually abandon:

Dr ARO Liability 133.1
Cr Cash 133.1

One more nuance

If estimates change later — for example:

abandonment cost estimate rises
timing changes
discounting assumptions change under the relevant framework

then there can be a remeasurement that may adjust the asset as well.

But that is a re-estimation case, not ordinary annual accretion.

Short answer

So:

Yes, at initial recognition you generally Dr Asset / Cr ARO liability.
No, for annual accretion you generally do Dr Accretion Expense / Cr ARO liability.
And the amount at inception is usually present value, not future value.

If you want, I can show the full 5-year roll-forward of:
initial ARO + DD&A of ARO asset + accretion of liability + final settlement in one table