class RiskAgent:
    def analyze(self, update: str):

        risks = []

        text = update.lower()

        if "delay" in text:
            risks.append("Schedule delay identified")

        if "budget" in text:
            risks.append("Budget risk detected")

        if "vendor" in text:
            risks.append("Vendor dependency risk")

        if "compliance" in text:
            risks.append("Compliance review required")

        risk_level = "Low"

        if len(risks) >= 3:
            risk_level = "High"
        elif len(risks) > 0:
            risk_level = "Medium"

        return {
            "risk_level": risk_level,
            "risks": risks
        }
