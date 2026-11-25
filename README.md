Mombasa Microfinance - Loan Repayment Analysis
A microfinance institution in Mombasa wants to understand its loan repayment data before presenting to board members.

What we looked at
150 fictional loan records with:

loan_id - e.g. MSA-001
amount_kes - loan size in Kenyan Shillings
days_to_first_repayment - days from disbursement to first repayment
county - Mombasa, Kwale, Kilifi, Tana River, Lamu, Taita-Taveta
Key findings
What is the typical loan amount?
Median (typical loan): 34,328 KES - half of loans are below this, half above.
Mean (average): 52,012 KES - higher than the median because a few very large loans pull it up.
Standard deviation: 62,353 KES - loans vary a lot.
Quartiles: 25% of loans are below 24,227 KES, 75% are below 49,733 KES.
Range: Smallest loan 3,466 KES, largest loan 337,346 KES.
Use the median (34,328 KES) when telling the board what a "typical" loan looks like.

Are there unusually large or small loans?
Yes. Using the IQR method (below Q1 - 1.5IQR or above Q3 + 1.5IQR, upper fence = 87,993 KES):

14 outliers, all unusually large - no unusually small loans:
MSA-009, MSA-015, MSA-020, MSA-027, MSA-032, MSA-042, MSA-048, MSA-078, MSA-082, MSA-091, MSA-095, MSA-102, MSA-126, MSA-132

These range from 96,941 KES to 337,346 KES. The board should check whether these are approved large loans, group loans, or data errors before including them in averages.

Is there a link between loan size and days to first repayment?
Correlation: 0.73

For the board: In plain language, bigger loans tend to take longer before the first repayment comes in, so larger loans need a bit more patience and closer follow-up in the first few weeks.

This is a strong positive link, but it does not prove that a bigger loan causes a delay - larger borrowers may simply agree a longer grace period.

Chart
Histogram of loan amounts
Most loans cluster between 10,000 and 60,000 KES, with a long tail of a few very large loans on the right. That is why the mean is higher than the median.

How to run
pip install pandas numpy matplotlib
python loan_analysis.py
Files
loan_analysis.py - full analysis
loan_amounts_histogram.png - histogram
loan_data.csv - generated dataset (optional)
