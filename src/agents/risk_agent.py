class RiskAgent:
    def analyze(self, update: str):
        risks = []

        if "delay" in update.lower():
            risks.append("Schedule delay risk detected")

        if "budget" in update.lower():
            risks.append("Budget impact risk possible")

        return {
            "risk_level": "Medium" if risks else "Low",
            "risks": risks
        }
