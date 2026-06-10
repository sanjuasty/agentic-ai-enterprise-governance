class ReportingAgent:
    def generate(
        self,
        execution_result,
        risk_result,
        governance_result
    ):

        summary = f"""
====================================
EXECUTIVE PMO STATUS REPORT
====================================

PROGRAM STATUS:
{execution_result['delivery_status']}

EXECUTION SUMMARY:
{execution_result['status_summary']}

KEY UPDATE:
{execution_result['key_update']}

RISK LEVEL:
{risk_result['risk_level']}

IDENTIFIED RISKS:
{risk_result['risks']}

GOVERNANCE STATUS:
{governance_result['governance_status']}

EXECUTIVE ESCALATION:
{governance_result['executive_escalation']}

RECOMMENDATION:
Continue weekly governance review.

====================================
"""

        return summary
