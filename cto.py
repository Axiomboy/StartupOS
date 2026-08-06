class CTO:

    def think(self, tasks):

        if len(tasks) == 0:
            return "Nothing to build."

        return f"Engineering priority:\n{tasks[0]['task']}"