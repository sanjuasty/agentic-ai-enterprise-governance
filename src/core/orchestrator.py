from agents.execution_agent import ExecutionAgent
from agents.risk_agent import RiskAgent
from agents.governance_agent import GovernanceAgent
from agents.reporting_agent import ReportingAgent


class PMOOrchestrator:

    def __init__(self):

        self.execution_agent = ExecutionAgent()
        self.risk_agent = RiskAgent()
        self.governance_agent = GovernanceAgent()
        self.reporting_agent = ReportingAgent()

    def run(self, update):

        execution_result = self.execution_agent.analyze(update)

        risk_result = self.risk_agent.analyze(update)

        governance_result = self.governance_agent.analyze(update)

        report = self.reporting_agent.generate(
            execution_result,
            risk_result,
            governance_result
        )

        return report
